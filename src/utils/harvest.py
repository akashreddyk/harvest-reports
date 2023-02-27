import requests


def get_time_entries(api_url: str, account_id: int, bearer_token: str) -> dict:
    """

    :param api_url:
    :param account_id:
    :param bearer_token:
    :return:
    """
    headers = {"Authorization": f"Bearer {bearer_token}", "Harvest-Account-Id": account_id}

    return requests.get(api_url, headers=headers).json()