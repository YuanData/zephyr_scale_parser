import numpy as np
import pandas as pd
import pandas_read_xml as pdx


class CasesParser:
    """
    A class for parsing Zephyr Scale test cases from XML files and exporting them to an Excel file.
    """

    def __init__(self, zs_key: str):
        """
        Initialize CasesParser object.

        :param zs_key: The Zephyr Scale key.
        """
        self.zs_key = zs_key
        self.df = None
        self.labels_lst = None
        self.writer = None
        self.output_file = None

    def read_xml_file(self, input_file: str):
        """
        Read an XML file and parse the data.

        :param input_file: The path of the input XML file.
        """
        self.df = pdx.read_xml(f'input_files/{input_file}', ['project', 'testCases'])
        self.df = pdx.auto_flatten(self.df)

    def init_df(self):
        """
        Initialize the DataFrame with the parsed data.
        """
        self.df.rename(columns={'testCase|@key': 'Key', 'testCase|priority': 'Priority', 'testCase|name': 'Name',
                                'testCase|labels': 'Labels', 'testCase|folder': 'Folder', 'testCase|status': 'Status',
                                'testCase|createdBy': 'CreatedBy', 'testCase|createdOn': 'CreatedOn'}, inplace=True)
        self.df = self.df[['Priority', 'Key', 'Name', 'Labels', 'CreatedBy', 'CreatedOn', 'Folder', 'Status']]
        self.df['Labels'] = np.where(self.df['Labels'].isnull(), {'label': 'Empty_Label'}, self.df['Labels'])
        self.df['Labels'] = self.df['Labels'].apply(lambda d: d['label'])
        self.df['CreatedOn'] = self.df['CreatedOn'].str[:10]
        self.explode_labels()

    def explode_labels(self):
        """
        Explode the 'Labels' column and create a separate column for each label.
        """
        df_labels = self.df[['Key', 'Labels']].copy()
        df_labels['Int_1'] = 1
        df_labels = df_labels.explode('Labels')
        labels_set = set(df_labels.Labels.to_list())
        self.labels_lst = sorted(list(labels_set))

        df_labels.set_index(['Key', 'Labels'], inplace=True)
        df_labels = df_labels.unstack()
        df_labels.columns = df_labels.columns.droplevel()

        self.df.set_index('Key', inplace=True)
        self.df = pd.concat([self.df, df_labels], axis=1)
        self.df.reset_index(inplace=True)

    def write_labels(self):
        """
        Write the list of labels to the Excel file.
        """
        df = pd.DataFrame(self.labels_lst, columns=['Labels'])
        df.to_excel(self.writer, sheet_name='LabelSet', index=False)

    def export_xlsx(self, output_file: str):
        """
        Export the parsed data to an Excel file.

        :param output_file: The path of the output Excel file.
        """
        self.writer = pd.ExcelWriter(f'./output_files/{output_file}', engine='openpyxl')

        self.df.to_excel(self.writer, sheet_name='Sheet1', index=False)
        self.write_labels()

        self.writer.save()
