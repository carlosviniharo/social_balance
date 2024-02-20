from openpyxl import load_workbook
import pandas as pd


def extract_excel_to_json(excel_file):
    # Open the excel file.
    workbook_two = load_workbook(excel_file)
    checklistsheet = workbook_two["Check list"]
    df = pd.DataFrame(checklistsheet.values)
    return df.to_json()
