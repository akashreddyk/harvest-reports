
def filter_entries(start_date: str, end_date: str, entries: dict):
    """

    :param month_val:
    :return:
    """
    filtered_data = []
    data = entries["time_entries"]
    for entry in data:
        if start_date <= entry["spent_date"] <= end_date:
            filtered_data.append(entry)
    return filtered_data


def reform_data(raw_data: dict) -> dict:
    """

    :param raw_data:
    :param schema:
    :return:

    required fields - "Date","Client","Project","Project Code","Task Notes","Hours","Billable?","Invoiced?","Approved?","First Name","Last Name","Employee?"

    """

    static_header = ["Date","Client","Project","Project Code","Task Notes","Hours","Billable?","Invoiced?","Approved?","First Name","Last Name","Employee?"]
    data = [static_header]
    for entry in raw_data:
        temp = [entry["spent_date"], entry["client"]["name"], entry["project"]["name"],
                entry["project"]["code"], entry["task"]["name"], entry["hours"], entry["billable"], entry["invoice"], "", entry["user"]["name"], ""]
        data.append(temp)
    return static_header, data