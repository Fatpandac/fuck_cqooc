# -*- coding: utf-8 -*-
class User:

    __xsid = None
    __id = None
    __username = None
    __pwd = None
    __name = None
    __avatar = None

    def __init__(self, username: str, pwd: str) -> None:
        self.__username = username
        self.__pwd = pwd

    def set_xsid(self, xsid: str) -> None:
        self.__xsid = xsid

    def get_xsid(self) -> str:
        return self.__xsid

    def set_id(self, id: int) -> None:
        self.__id = id

    def get_id(self) -> int:
        return self.__id

    def set_username(self, username: str) -> None:
        self.__username = username

    def get_username(self) -> str:
        return self.__username

    def set_pwd(self, pwd: str) -> None:
        self.__pwd = pwd

    def get_pwd(self) -> str:
        return self.__pwd

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_avatar(self, avatar: str):
        self.__avatar = avatar

    def get_avatar(self) -> str:
        return self.__avatar

    def get_info(self) -> dict:
        return {
            "xsid": self.__xsid,
            "id": self.__id,
            "username": self.__username,
            "pwd": self.__pwd,
            "name": self.__name,
            "avatar": self.__avatar,
        }
