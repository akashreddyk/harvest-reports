"""

"""
import configparser

from utils.export import export_to_xlsx
from utils.formatter import filter_entries, reform_data
from utils.harvest import get_time_entries
#from src.utils.summary_processor import summary_report


def initialize_global_variables(file_path: str):
    """

    :param file_path:
    :return:
    """
    config = configparser.ConfigParser()
    config.read_file(open(file_path))

    global HARVEST_TIME_ENTRIES_API
    global ACCOUNT_ID
    global BEARER_TOKEN
    global START_DATE
    global END_DATE
    global WORKING_DAYS
    global HOLIDAYS_AND_LEAVE
    global SCHEMA
    global FILE_NAME
    global HEADERS_SUMMARY
    global HEADERS_OVERVIEW

    ACCOUNT_ID = config['HARVEST']['account_id']
    HARVEST_TIME_ENTRIES_API = config['HARVEST']['harvest_time_entries_api']
    BEARER_TOKEN = config['HARVEST']['bearer_token']

    START_DATE = config['REPORT']['start_date']
    END_DATE = config['REPORT']['end_date']
    WORKING_DAYS = config['REPORT']['working_days']
    HOLIDAYS_AND_LEAVE = config['REPORT']['holidays_and_leave']

    FILE_NAME = config['OUTPUT']['file_name']

    SCHEMA = eval(config['SCHEMA']['schema_detailed'])
    HEADERS_SUMMARY = eval(config['SCHEMA']['headers_summary'])
    HEADERS_OVERVIEW = eval(config['SCHEMA']['headers_overview'])


if __name__ == "__main__":
    file_path = "src/config/config.ini"
    initialize_global_variables(file_path)

    time_entries = get_time_entries(HARVEST_TIME_ENTRIES_API, ACCOUNT_ID, BEARER_TOKEN)
    filtered_data = filter_entries(START_DATE, END_DATE, time_entries)
    detailed_header, reformed_data = reform_data(filtered_data)
    # TODO calculate the summary report
    # TODO export the summary report
    export_to_xlsx(reformed_data, FILE_NAME)
