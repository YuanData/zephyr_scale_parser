"""
This script demonstrates the usage of the CasesParser test class to parse cases from an XML file and export them to an Excel file.
"""
from cases_parser import CasesParser

if __name__ == '__main__':
    app_parser = CasesParser(zs_key='APP')
    app_parser.read_xml_file('app_test_cases_export.xml')
    app_parser.init_df()
    app_parser.export_xlsx('APP_TestCases.xlsx')
