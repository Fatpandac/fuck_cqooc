# -*- coding: utf-8 -*-
import requests


class Request:

    __host = "http://www.cqooc.com"

    def __init__(self):
        self.__headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            + " AppleWebKit/537.36 (KHTML, like Gecko) "
            + "Chrome/79.0.3945.130 Safari/537.36",
        }
        self.__proxies = {
            "http": "",
            "https": "",
        }

    def set_headers(self, name: str, value: str) -> None:
        self.__headers[name] = value

    def del_headers(self, name: str) -> None:
        del self.__headers[name]

    def get_headers(self) -> dict:
        return self.__headers

    def set_proxies(self, name: str, value: str) -> None:
        self.__proxies[name] = value

    def get_proxies(self) -> dict:
        return self.__proxies

    def get_host(self) -> str:
        return self.__host

    def do_get(
        self, url: str, headers: dict = None, proxies: dict = None
    ) -> requests.Response:
        self_headers = self.__headers.copy()
        if headers is not None:
            for key in headers:
                self_headers[key] = headers[key]
        self_proxies = self.__proxies.copy()
        if proxies is not None:
            for key in proxies:
                self_proxies[key] = proxies[key]
        return requests.get(url, headers=self_headers, proxies=self_proxies)

    def do_post(
        self,
        url: str,
        data: dict = None,
        headers: dict = None,
        proxies: dict = None,
    ) -> requests.Response:
        self_headers = self.__headers.copy()
        if headers is not None:
            for key in headers:
                self_headers[key] = headers[key]
        self_proxies = self.__proxies.copy()
        if proxies is not None:
            for key in proxies:
                self_proxies[key] = proxies[key]
        return requests.post(
            url, data=data, headers=self_headers, proxies=self_proxies
        )
