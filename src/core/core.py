# -*- coding: utf-8 -*-
class Core:
    def __init__(self, xsid=None):
        if xsid:
            self.__xsid = self.__set_xsid(xsid)
        else:
            if self.__get_xsid():
                self.__xsid = self.__get_xsid()
            else:
                raise Exception("No XSID found")

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

    def get_xsid(self) -> str:
        return self.__xsid
