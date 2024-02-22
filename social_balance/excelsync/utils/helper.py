from openpyxl import load_workbook
import pandas as pd

from principles.models import Vindicators


def extract_excel_to_json(excel_file):
    # Open the excel file.
    workbook_two = load_workbook(excel_file)
    df = pd.DataFrame()
    for principle_sheet in workbook_two:
        df = pd.DataFrame(principle_sheet.values)
        indicators = Vindicators.objects.all()
        # indicators.get(codigoindicador=df.tolist())
        checklistsheet = principle_sheet
        df = pd.DataFrame(checklistsheet.values)

    return df.to_json()
