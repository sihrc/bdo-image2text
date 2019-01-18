import requests
import socket

from urllib.parse import unquote_plus as urllib_unquote_plus
from urllib.error import HTTPError, URLError


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def get_content_from_url(url):
    url = urllib_unquote_plus(url).strip()
    headers = dict(HEADERS)
    return requests.get(url, headers=headers, timeout=5).content
