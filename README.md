# Zephyr Scale Test Cases Parser
A Python script for parsing Zephyr Scale test cases from XML files and exporting them to an Excel file.  
可用於從XML文件解析Zephyr Scale測試用例並將其導出到Excel文件的Python專案。

## Requirements
- Python 3.7 or higher
- Required Python packages:
  - pandas
  - pandas_read_xml

## Usage
1. Run the script:
   ```bash
   python parse_blog_cases.py
   ```
2. The parsed cases data will be exported to an Excel in the output_files directory.

## Customization
We can customize the script to fit your specific requirements by modifying the following parts:  
可以通過修改以下部分來自訂化文件以滿足具體需求：
- Adding plan data: Customize the plan list in the script file to match your specific plan. Each dictionary in the list represents a plan entry, and you can modify the values of columns according to your needs.  
 添加計劃數據：自訂化文件中的計劃列表，以符合具體計劃。列表中的每個字典代表一個計劃項目，可以根據需要修改列的值。
- Additional processing: You can overwrite export_xlsx methods in the CasesParser class to perform any additional data processing or manipulation required for your specific use case.  
 額外處理：可以覆寫CasesParser類中的export_xlsx方法，以執行特定用例所需的任何額外數據處理或操作。

## Note
Make sure to adjust file paths and specific details according to your project structure and requirements.  
請確保根據項目結構和需求調整文件路徑和具體細節。