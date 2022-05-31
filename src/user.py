# -*- coding: utf-8 -*-
class User:

    __xsid = None
    __id = None
    __username = None
    __pwd = None
    __name = None
    __course_data = None
    __lessons_data = None
    __mcs_id = None

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

    def set_course_data(self, course_data: dict) -> None:
        self.__course_data = course_data

    def get_course_data(self) -> dict:
        return self.__course_data

    def set_lessons_data(self, lessons_data: dict) -> None:
        self.__lessons_data = lessons_data

    def get_lessons_data(self) -> dict:
        return self.__lessons_data

    def set_mcs_id(self, mcs_id: str) -> None:
        self.__mcs_id = mcs_id

    def get_mcs_id(self) -> str:
        return self.__mcs_id

    def get_info(self) -> dict:
        return {
            "xsid": self.__xsid,
            "id": self.__id,
            "username": self.__username,
            "pwd": self.__pwd,
            "name": self.__name,
            "mcs_id": self.__mcs_id,
            "course_data": self.__course_data,
            "lessons_data": self.__lessons_data,
        }
