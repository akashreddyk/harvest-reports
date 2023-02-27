import csv
import openpyxl


def export_to_csv(data: dict, file_name: str):
    """

    :param data:
    :return:
    """
    with open(file_name, 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerows(data)


def export_to_xlsx(data: list, file_name: str):
    """

    :param data:
    :return:
    """
    wb = openpyxl.Workbook()

    # create the first sheet
    detailed_report = wb.create_sheet('Detailed Report')

    # remove default sheet
    sheet = wb.get_sheet_by_name('Sheet')
    wb.remove_sheet(sheet)

    # append data to the sheet
    for row in data:
        detailed_report.append(row)

    wb.save(file_name)