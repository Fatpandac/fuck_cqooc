# -*- coding: utf-8 -*-

from src.core.request import Request


ua = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
    + "/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
)

proxies = {
    "http": "",
    "https": "",
}

proxiesURI = "http://127.0.0.1:8889"


def test_get_ua():
    request = Request()
    assert request.get_headers()["User-Agent"] == ua


def test_set_cookie_into_headers():
    request = Request()
    request.set_headers("cookie", "12345678")
    assert request.get_headers()["cookie"] == "12345678"


def test_del_cookie():
    request = Request()
    request.set_headers("cookie", "12345678")
    request.del_headers("cookie")
    assert "cookie" not in request.get_headers()


def test_get_proxies():
    request = Request()
    assert request.get_proxies() == proxies


def test_set_proxies():
    request = Request()
    request.set_proxies("http", proxiesURI)
    assert request.get_proxies()["http"] == proxiesURI
    request.set_proxies("http", "")


def test_do_get():
    request = Request()
    res = request.do_get(
        "https://www.google.com",
        proxies={
            "http": "http://127.0.0.1:8889",
            "https": "http://127.0.0.1:8889",
        },
    )
    assert res.status_code == 200


def test_do_post():
    request = Request()
    res = request.do_post(
        "https://sm.ms/api/v2",
        headers={
            "User-Agent": ua,
        },
        proxies={
            "http": "http://127.0.0.1:8889",
            "https": "http://127.0.0.1:8889",
        },
    )
    print(res.request.headers)
    assert res.status_code == 200
