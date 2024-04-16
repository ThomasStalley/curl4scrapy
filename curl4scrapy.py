from urllib.parse import unquote

from js import console


def main(*args):
    """. . ."""
    curl_input_text = Element("curl").element.value
    scrapy_output_text = curl4scrapy(curl_input_text)
    Element("scrapy").element.innerText = scrapy_output_text


def curl4scrapy(text: str) -> str:
    """. . ."""

    def _get_url(text: str) -> str:
        return text

    def _get_method(text: str) -> str:
        return text

    def _get_body(text: str) -> str:
        return text

    def _get_headers(text: str) -> str:
        return text

    def _get_cookies(text: str) -> str:
        return text

    def _get_scrapy(url: str, method: str, body: str, headers: str, cookies: str) -> str:
        scrapy_text = f"url={url} "
        scrapy_text += f"method={method} "
        scrapy_text += f"body={body} "
        scrapy_text += f"headers={headers} "
        scrapy_text += f"cookies={cookies}"
        return scrapy_text

    curl_text = unquote(text)
    url = _get_url(curl_text)
    method = _get_method(curl_text)
    body = _get_body(curl_text)
    headers = _get_headers(curl_text)
    cookies = _get_cookies(curl_text)
    scrapy_text = _get_scrapy(url, method, body, headers, cookies)
    return scrapy_text
