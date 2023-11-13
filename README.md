# ContactsParser

[![Python](https://img.shields.io/badge/Python-3.8-blue?logo=python)](https://www.python.org/)

This Python module provides functions for downloading web pages and finding phone numbers within text.

## Installation

To use this module, you need to have Poetry installed on your system. If you don't have Poetry, you can install it from the [official documentation](https://python-poetry.org/docs/).

Once you have Poetry installed, navigate to the module's root directory and run the following command:

```bash
poetry install
```

This will create a new virtual environment and install all the necessary dependencies.

## Usage

```python
import ContactsParser

# Download a web page
webpage_content = ContactsParser.download_webpage("https://example.com")

# Find phone numbers
phone_numbers = ContactsParser.find_phone_numbers(webpage_content)
print(phone_numbers)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contacts

For any questions or inquiries, feel free to reach out through the following channels:

[![Telegram](https://img.shields.io/badge/Telegram-%40skirtsfield-blue?logo=telegram)](https://t.me/skirtsfield)
[![Email](https://img.shields.io/badge/Email-wrkngskirt@gmail.com-blue?logo=gmail)](mailto:wrkngskirt@gmail.com)
