# _*_ coding: utf-8 _*_

"""
util_parse.py by xianhu
"""

import re
import urllib.parse

__all__ = [
    "get_string_num",
    "get_string_strip",
    "get_url_legal",
    "get_url_params",
]


def get_string_num(string):
    """
    get a float number from a string
    """
    string_temp = get_string_strip(string.upper().replace(",", ""), replace_char="")
    string_re = re.search(r"(?P<num>\d+(\.\d+)?)", string_temp, flags=re.IGNORECASE)
    return float(string_re.group("num")) if string_re else 0.0


def get_string_strip(string, replace_char=" "):
    """
    get a string which striped \t, \r, \n from a string, also change None to ""
    """
    return re.sub(r"\s+", replace_char, string, flags=re.IGNORECASE).strip() if string else ""


def get_url_legal(url, base_url, encoding=None):
    """
    get a legal url from a url, based on base_url
    """
    url_join = urllib.parse.urljoin(base_url, url, allow_fragments=True)
    return urllib.parse.quote(url_join, safe="%/:=&?~#+!$,;'@()*[]|", encoding=encoding)


def get_url_params(url, keep_blank_value=False, encoding="utf-8"):
    """
    get main_part(a string) and query_part(a dictionary) from a url
    """
    url_frags = urllib.parse.urlparse(url, allow_fragments=True)
    main_part = urllib.parse.urlunparse((url_frags.scheme, url_frags.netloc, url_frags.path, url_frags.params, "", ""))
    query_part = urllib.parse.parse_qs(url_frags.query, keep_blank_values=keep_blank_value, encoding=encoding)
    return main_part, query_part
