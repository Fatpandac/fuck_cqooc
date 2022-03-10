# -*- coding: utf-8 -*-

from src.core.config import Config


ua = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
    + "/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
)

proxies = {
    "http": "",
    "https": "",
}

proxiesURI = "http://127.0.0.1:8080"

pwd = "12345678"
username = "test"


def test_get_pwd():
    config = Config(pwd, username)
    assert config.get_pwd() == pwd


def test_get_username():
    config = Config(pwd, username)
    assert config.get_username() == username


def test_get_ua():
    config = Config(pwd, username)
    assert config.get_headers()["User-Agent"] == ua


def test_set_cookie_into_headers():
    config = Config(pwd, username)
    config.set_headers("cookie", "12345678")
    assert config.get_headers()["cookie"] == "12345678"


def test_del_cookie():
    config = Config(pwd, username)
    config.del_headers("cookie")
    assert "cookie" not in config.get_headers()


def test_get_proxies():
    config = Config(pwd, username)
    assert config.get_proxies() == proxies


def test_set_proxies():
    config = Config(pwd, username)
    config.set_proxies("http", proxiesURI)
    assert config.get_proxies()["http"] == proxiesURI
    config.set_proxies("http", "")
