# utils/excel_utils.py
import openpyxl
import os

class ExcelUtils:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Excel file not found: {file_path}")
        self.file_path = file_path
        self.workbook = openpyxl.load_workbook(file_path)

    def get_cell_value(self, sheet_name, cell):
        """
        Get value of a specific cell.
        Example: get_cell_value("Sheet1", "A1")
        """
        sheet = self.workbook[sheet_name]
        return sheet[cell].value

    def get_row_values(self, sheet_name, row_number):
        """
        Get all cell values from a specific row as a list
        """
        sheet = self.workbook[sheet_name]
        return [cell.value for cell in sheet[row_number]]

    def get_column_values(self, sheet_name, column_letter):
        """
        Get all cell values from a specific column as a list
        """
        sheet = self.workbook[sheet_name]
        return [cell.value for cell in sheet[column_letter]]

    def get_all_values(self, sheet_name):
        """
        Return all data in the sheet as a list of lists
        """
        sheet = self.workbook[sheet_name]
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(list(row))
        return data
