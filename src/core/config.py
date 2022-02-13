# -*- coding: utf-8 -*-
class Config:
    def __init__(self, xsid):
        if xsid:
            self.__xsid = self.__set_xsid(xsid)
        else:
            if self.__get_xsid():
                self.__xsid = self.__get_xsid()
            else:
                raise Exception("No XSID found")
        self.__ua = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
            + "/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        )
        self.__headers = {
            "User-Agent": self.__ua,
            "Cookie": f"xsid={self.__xsid};",
        }

    def __set_xsid(self, xsid) -> str:
        with open("./cookies.txt", "w") as f:
            f.write(xsid)
        return xsid

    def __get_xsid(self) -> str:
        try:
            with open("./cookies.txt", "r") as f:
                return f.read()
        except FileNotFoundError:
            return None

    def get_headers(self) -> dict:
        return self.__headers
