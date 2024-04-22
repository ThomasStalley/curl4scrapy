import re
from urllib.parse import unquote

from js import console


def main(*args):
    """. . ."""
    curl_input_text = Element("curl").element.value
    scrapy_output_text = pipeline(curl_input_text)
    Element("scrapy").element.innerText = scrapy_output_text


def pipeline(text):
    """. . ."""

    def _get_url(text: str) -> str:
        """. . ."""
        url_pattern = r"(http\S+)"
        if url_search := re.search(url_pattern, text):
            url = url_search.group(1)
        else:
            url = "__url__"
        return url

    def _get_method(text: str) -> str:
        """. . ."""
        if method_search := re.search(r"(-X|--request) (\S+)", text):
            method = method_search.group(1)
        elif re.search(r"--data(-binary|-raw|-urlencode)?", text):
            method = "POST"
        else:
            method = "GET"
        return method

    def _get_body(text: str) -> str:
        """. . ."""
        body = "__body__"
        return body

    def _get_headers(text: str) -> str:
        """. . ."""
        headers_pattern = r"(-H|--header) [\'\"](.+)[\'\"]"
        if headers_search := re.search(headers_pattern, text):
            headers = headers_search.group(1)
        else:
            headers = "__headers__"
        return headers

    def _get_cookies(text: str) -> str:
        """. . ."""
        cookies = "__cookies__"
        return cookies

    def _get_scrapy_text(url: str, method: str, body: str, headers: str, cookies: str) -> str:
        """. . ."""
        scrapy_text = f"url={url}       "
        scrapy_text += "callback=self.get_data,       "
        scrapy_text += f"method={method}       "
        scrapy_text += f"headers={headers}       "
        scrapy_text += f"body={body}       "
        scrapy_text += f"cookies={cookies}       "
        scrapy_text += "dont_filter=True       "
        return scrapy_text

    curl_text = unquote(text)
    url = _get_url(curl_text)
    method = _get_method(curl_text)
    body = _get_body(curl_text)
    headers = _get_headers(curl_text)
    cookies = _get_cookies(curl_text)
    scrapy_text = _get_scrapy_text(url, method, body, headers, cookies)
    return scrapy_text
