from requests import get
from requests import utils

def currency_rates(url, content_name):
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    # print(content)
    # print(type(content))

    content_name_index = content.find(f"<CharCode>{ content_name.upper()}</CharCode>")
    # print(content_name_index)
    if content_name_index != -1:
        tag_open = content.find("<Value>", content_name_index)
        # print(tag_open)
        tag_close = content.find("</Value>", tag_open)
        tag_value_length = 7
        currency = float(content[tag_open + tag_value_length: tag_close].replace(",", "."))
        return currency

if __name__ == "__main__":
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    print(currency_rates(url, "EuR"))
    print(currency_rates(url, "AUD"))
    print(currency_rates(url, "GBP"))
    print(currency_rates(url, "USd"))