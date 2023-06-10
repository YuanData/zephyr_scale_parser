from typing import List, Dict, Union

import pandas as pd

from cases_parser import CasesParser

ra = range
id_ = 'id'
tc = 'TestClass'
ti = 'TestItem'
ts = 'TestScope'
ke = 'Key'
acc = 'accumulation'

PLAN_OF_BLOG = [
    {id_: '1.1.1', tc: 'Account Manage', ti: 'Login', ts: 'UI Layout', ke: [246]},
    {id_: '1.1.2', tc: 'Account Manage', ti: 'Login', ts: 'Functional', ke: [12, 33, 247, 261]},
    {id_: '1.1.3', tc: 'Account Manage', ti: 'Login', ts: 'Security Check', ke: [*ra(249, 256)]},
    {id_: '1.2.1', tc: 'Account Manage', ti: 'SignUp', ts: 'UI Layout', ke: [643]},
    {id_: '1.2.2', tc: 'Account Manage', ti: 'SignUp', ts: 'Functional', ke: [13, 35, 248, *ra(644, 648)]},
    {id_: '1.2.3', tc: 'Account Manage', ti: 'SignUp', ts: 'API', ke: [667, 678]},
    {id_: '1.2.4', tc: 'Account Manage', ti: 'SignUp', ts: 'Signup Enhancement', ke: [839, 840]},
    {id_: '1.3.2', tc: 'Account Manage', ti: 'SMS Services', ts: 'Security Check', ke: [*ra(814, 818)]},
    {id_: '1.4.1', tc: 'Account Manage', ti: 'Forgot PW', ts: 'UI Layout', ke: [257, 258]},
    {id_: '1.4.2', tc: 'Account Manage', ti: 'Forgot PW', ts: 'Functional', ke: [256, 260, *ra(263, 266), 267, 270]},
    {id_: '1.5.1', tc: 'Account Manage', ti: 'LogOut', ts: 'Functional', ke: [650]},
    {id_: '2.1.1', tc: 'User Settings', ti: 'Profile', ts: 'UI Layout', ke: [626]},
    {id_: '2.1.2', tc: 'User Settings', ti: 'Profile', ts: 'Public Information', ke: [*ra(627, 632)]},
    {id_: '2.1.3', tc: 'User Settings', ti: 'Profile', ts: 'Private Information', ke: [*ra(632, 637)]},
    {id_: '2.1.4', tc: 'User Settings', ti: 'Profile', ts: 'Notifications', ke: [640, 641, 698]},
    {id_: '3.1.1', tc: 'User Profile', ti: 'User Information', ts: 'ALL', ke: [294, *ra(341, 346)]},
    {id_: '3.2.1', tc: 'User Profile', ti: 'My Analysis', ts: 'ALL', ke: [*ra(346, 353), 359, 362]},
    {id_: '3.3.1', tc: 'User Profile', ti: 'Followers', ts: 'ALL', ke: [360, 361, 363, *ra(365, 368), 371]},
    {id_: '3.4.1', tc: 'User Profile', ti: 'Following', ts: 'ALL', ke: [*ra(373, 382)]},
    {id_: '3.5.1', tc: 'User Profile', ti: 'Saved', ts: 'ALL', ke: [*ra(386, 394)]},
    {id_: '3.6.1', tc: 'User Profile', ti: 'Notification', ts: 'ALL', ke: [*ra(400, 404), *ra(408, 412), 481]},
    {id_: '3.6.2', tc: 'User Profile', ti: 'Notification', ts: 'Likes', ke: [*ra(482, 485), 525, 533]},
    {id_: '3.6.3', tc: 'User Profile', ti: 'Notification', ts: 'Comments', ke: [*ra(485, 488), 526, 534]},
    {id_: '3.6.4', tc: 'User Profile', ti: 'Notification', ts: 'Mentions', ke: [*ra(488, 491), 527, 535]},
    {id_: '3.6.5', tc: 'User Profile', ti: 'Notification', ts: 'Position Status Updates', ke: [*ra(509, 536), 528, ]},
    {id_: '3.6.6', tc: 'User Profile', ti: 'Notification', ts: 'Subscription', ke: [*ra(512, 515), 529, 537]},
    {id_: '3.6.7', tc: 'User Profile', ti: 'Notification', ts: 'Followers', ke: [*ra(515, 519), 530, 538]},
    {id_: '3.6.8', tc: 'User Profile', ti: 'Notification', ts: 'Hop Topics', ke: [*ra(519, 522), 531, 539]},
    {id_: '3.6.9', tc: 'User Profile', ti: 'Notification', ts: 'Suggested Analysis', ke: [*ra(522, 525), 532, 540]},
    {id_: '4.1.1', tc: 'Home Page', ti: 'Top Bar', ts: 'ALL', ke: [*ra(428, 434)]},
    {id_: '4.2.1', tc: 'Home Page', ti: 'Category Post Analysis', ts: 'ALL', ke: [42, 440, 442, *ra(710, 717)]},
    {id_: '4.3.1', tc: 'Home Page', ti: 'Bottom', ts: 'ALL', ke: [450, 451, 717]},
    {id_: '4.4.1', tc: 'Home Page', ti: 'Breaking News Block', ts: 'ALL', ke: [*ra(856, 859)]},
    {id_: '4.5.1', tc: 'Home Page', ti: 'Related News Block', ts: 'ALL', ke: [*ra(861, 864)]},
    {id_: '4.6.1', tc: 'Home Page', ti: 'Category News Block', ts: 'ALL', ke: [*ra(866, 869)]},
    {id_: '5.1.1', tc: 'Blog', ti: 'Blog User Profile', ts: 'User Profile Window', ke: [*ra(412, 415), 416]},
    {id_: '5.1.2', tc: 'Blog', ti: 'Blog User Profile', ts: 'User Profile Page', ke: [415, *ra(417, 425)]},
    {id_: '5.2.1', tc: 'Blog', ti: 'Post Analysis Page', ts: 'Thumbnail View', ke: [*ra(543, 546), 558, 559]},
    {id_: '5.2.2', tc: 'Blog', ti: 'Post Analysis Page', ts: 'Detail Page', ke: [*ra(546, 552)]},
    {id_: '5.2.3', tc: 'Blog', ti: 'Post Analysis Page', ts: 'Reactions', ke: [293, 296, *ra(310, 320), 328]},
    {id_: '5.2.4', tc: 'Blog', ti: 'Post Analysis Page', ts: 'Save Analysis', ke: [560, 571]},
    {id_: '5.2.4', tc: 'Blog', ti: 'Post Analysis Page', ts: 'Share to Friends', ke: [*ra(561, 568)]},
    {id_: '5.2.5', tc: 'Blog', ti: 'Post Analysis Page', ts: 'Position Status', ke: [*ra(175, 181), 576, 577]},
    {id_: '5.2.6', tc: 'Blog', ti: 'Post Analysis Page', ts: 'Comments', ke: [*ra(568, 571), 579]},
    {id_: '5.3.1', tc: 'Blog', ti: 'Tags', ts: 'ALL', ke: [39, 477, 478, 690, 691, *ra(695, 698)]},
    {id_: '5.4.1', tc: 'Blog', ti: 'Search', ts: 'ALL', ke: [654, 657, 664]},
    {id_: '5.4.1', tc: 'Blog', ti: 'API', ts: 'ALL', ke: [*ra(665, 793)]},
]


class BLOGParser(CasesParser):
    """
    A class for parsing BLOG test cases from XML files and exporting them to an Excel file.
    This class inherits from CasesParser.
    """

    def __init__(self, zs_key: str):
        """
        Initialize BLOGParser object.

        :param zs_key: The Zephyr Scale key.
        """
        super().__init__(zs_key)
        self.plan = None

    def add_plan(self, plan: List[Dict[str, Union[str, List[int]]]]):
        """
        Add plan data to the DataFrame.

        :param plan: The plan data.
        """
        self.plan = plan
        for d in self.plan:
            zs_keys = [f'{self.zs_key}{number}' for number in d['ke']]
            self.df.loc[self.df['Key'].isin(zs_keys), 'id_'] = d['id_']
            self.df.loc[self.df['Key'].isin(zs_keys), 'tc'] = d['tc']
            self.df.loc[self.df['Key'].isin(zs_keys), 'ti'] = d['ti']
            self.df.loc[self.df['Key'].isin(zs_keys), 'ts'] = d['ts']

    def write_plan(self):
        """
        Write the plan data to the Excel file.
        """
        df = self.df.copy()
        df.sort_values(['id_', 'Key'], inplace=True)
        df['acc'] = df.groupby(['tc']).cumcount() + 1
        df.set_index(['tc', 'ti', 'ts', 'Key'], inplace=True)
        df = df[['id_', 'acc', 'Priority', 'Name', 'CreatedOn', 'Non-automated', 'Automatable', 'Automated',
                 'Labels', 'Folder', 'CreatedBy', 'Status']]
        df.to_excel(self.writer, sheet_name='plan')

    def write_pivot(self):
        """
        Write the pivot data to the Excel file.
        """
        df = self.df.copy()
        df.sort_values(['id_', 'Key'], inplace=True)
        df['acc'] = df.groupby(['tc']).cumcount() + 1
        df = df[['tc', 'ti', 'ts', 'Key', 'id_', 'acc', 'Priority', 'Name', 'CreatedOn', 'Non-automated', 'Automatable',
                 'Automated', 'Labels', 'Folder', 'CreatedBy', 'Status']]
        df.to_excel(self.writer, sheet_name='pivot', index=False)

    def export_xlsx(self, output_file):
        """
        Export the parsed BLOG cases data to an Excel file.
        Overrides the export_xlsx method from CasesParser.

        :param output_file: The path of the output Excel file.
        """
        self.writer = pd.ExcelWriter(f'./output_files/{output_file}', engine='openpyxl')

        self.write_plan()
        self.write_pivot()
        self.write_labels()

        self.writer.save()


if __name__ == '__main__':
    blog_parser = BLOGParser(zs_key='BLOG')
    blog_parser.read_xml_file('blog_test_cases.xml')
    blog_parser.init_df()

    # Filter by label
    blog_parser.df = blog_parser.df[
        (blog_parser.df['Blog'] == 1)
        & (blog_parser.df['Mobile_Mode'] != 1)
        & (blog_parser.df['Tablet_Mode'] != 1)
        & (blog_parser.df['Admin'] != 1)]

    blog_parser.add_plan(PLAN_OF_BLOG)

    blog_parser.df = blog_parser.df[~blog_parser.df['id'].isnull()]

    blog_parser.export_xlsx('BLOG_TestCases.xlsx')
