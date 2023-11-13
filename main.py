import requests
import re
from typing import List, Union

from requests import Response
from requests.exceptions import RequestException


def download_webpage(url: str) -> str:
    """
    Downloads the content of a web page given its URL.

    :param url: The URL of the web page to download.
    :type url: str
    :return: The content of the web page as a string.
    :rtype: str
    :raises RequestException: If an error occurs during the HTTP request.
    """
    try:
        response: Response = requests.get(url)
        response.raise_for_status()
    except RequestException as e:
        raise e

    return response.text


def find_phone_numbers(text: str) -> List[str]:
    """
    Finds and returns phone numbers in the given text.

    :param text: The text to search for phone numbers.
    :type text: str
    :return: A list of phone numbers in the format 8KKKNNNNNNN.
    :rtype: List[str]
    """
    phone_number_pattern: str = r'8\d{3}\d{7}'
    phone_numbers: List[Union[str, None]] = re.findall(phone_number_pattern, text)
    return phone_numbers


def main():
    # Example usage
    urls: List[str] = [
        "https://hands.ru/company/about",
        "https://repetitors.info"
    ]

    for url in urls:
        try:
            webpage_content: str = download_webpage(url=url)
            phone_numbers: List[str] = find_phone_numbers(text=webpage_content)
            print(phone_numbers)
        except Exception as e:
            print(f"An error occurred while processing {url}: {str(e)}")


if __name__ == '__main__':
    main()
