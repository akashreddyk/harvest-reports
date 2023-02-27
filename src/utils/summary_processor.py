from datetime import datetime

# TODO: Summary report code has to be completed.

# def summary_report(data, start_date: str, end_date: str, working_days: float, holidays: float):
#     """
#     """
#     # calculate weeks in the month
#     weeks_included: list[str] = count_weeks(start_date, end_date)
#     # Calculate totals per week
#     week_totals = {}
#     for entry in data:
#         print(entry['spent_date'])
#         date_obj = datetime.strptime(entry['spent_date'], "%Y-%m-%d")
#         week_number = date_obj.isocalendar()[1]
#         if week_number in week_totals.keys():
#             week_totals[week_number] = week_totals[week_number] + entry['hours']
#         else:
#             week_totals[week_number] = entry["hours"]
#     # validation check
#
#
# def count_weeks(start_date: str, end_date: str) -> list[int]:
#     """
#     """
#     # Convert the date to a datetime object
#     start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
#     end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
#
#     # Get the week number of the day
#     start_week_number = start_date_obj.isocalendar()[1]
#     end_week_number = end_date_obj.isocalendar()[1]
#     weeks_included = []
#     print(f" This is the start week: {start_week_number}")
#     print(f" This is the end week: {end_week_number}")
#     counter = start_week_number
#     while counter <= end_week_number:
#         if counter not in weeks_included:
#             weeks_included.append(counter)
#         counter = counter + 1
#
#     return weeks_included
#
#
# def calculate_total_per_week(data):
#     """
#
#     :param data:
#     :return:
#     """
#     # TODO: to be completed
