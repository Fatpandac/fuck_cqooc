# -*- coding: utf-8 -*-
class Config:

    __ua = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
        + "/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    )

    __headers = {
        "User-Agent": __ua,
    }
    __proxies = {
        "http": "",
        "https": "",
    }

    def __init__(self, pwd: str, username: str):
        self.__pwd = pwd
        self.__username = username

    def get_pwd(self):
        return self.__pwd

    def get_username(self):
        return self.__username

    def set_headers(self, name: str, value: str):
        self.__headers[name] = value

    def del_headers(self, name: str):
        del self.__headers[name]

    def get_headers(self):
        return self.__headers

    def set_proxies(self, name: str, value: str):
        self.__proxies[name] = value

    def get_proxies(self):
        return self.__proxies
