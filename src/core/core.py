# -*- coding: utf-8 -*-
from src.core.config import Config
from src.core.user import User
from src.core.msg import Msg
from src.core.test import test

import time
import json


class Core:
    def __init__(self, username: str, pwd: str) -> None:
        self.__config = Config()
        self.__user = User(username, pwd)

    def __get_ts(self) -> int:
        return int(time.time() * 1000)

    def __process_user_info(self) -> None:
        id_api = (
            "http://www.cqooc.com/user/session"
            + f"?xsid={self.__user.get_xsid()}&ts={self.__get_ts()}"
        )
        id_res = self.__config.do_get(id_api)
        id_data = json.loads(id_res.text)
        self.__user.set_id(id_data["id"])

        info_api = (
            "http://www.cqooc.com/account/session/api/profile/get"
            + f"?ts={self.__get_ts()}"
        )
        info_res = self.__config.do_get(info_api)
        info_data = json.loads(info_res.text)
        self.__user.set_name(info_data["name"])
        self.__user.set_avatar(info_data["headimgurl"])

    def login(self) -> dict:
        get_nonce_api = f"http://www.cqooc.net/user/login?ts={self.__get_ts()}"
        nonce_res = self.__config.do_get(get_nonce_api)
        data = json.loads(nonce_res.text)
        cn = test.cnonce()
        hash = test.getEncodePwd(
            data["nonce"] + test.getEncodePwd(self.__user.get_pwd()) + cn
        )
        loginUrl = (
            "http://www.cqooc.com/user/login"
            + f"?username={self.__user.get_username()}"
            + f'&password={hash}&nonce={data["nonce"]}&cnonce={cn}'
        )
        login_res = self.__config.do_post(loginUrl)
        data = json.loads(login_res.text)
        login_success = data["code"] == 0
        if login_success:
            self.__user.set_xsid(data["xsid"])
            self.__config.set_headers("Cookie", f'xsid={data["xsid"]}')
            self.__process_user_info()
            return Msg().prosecess("登录成功", 200, data)
        else:
            return Msg().prosecess("登录失败", 400, data)

    def get_user_info(self) -> dict:
        return self.__user.get_info()

    def get_course(self, limit: int = 20) -> dict:
        class_url = (
            "http://www.cqooc.com/json/mcs?sortby=id&reverse=true&del=2"
            + f"&courseType=2&ownerId={self.__user.get_id()}&limit={limit}"
            + f"&ts={self.__get_ts()}"
        )
        course_res = self.__config.do_get(
            class_url,
            headers={
                "Referer": "http://www.cqooc.com/my/learn",
                "Host": "www.cqooc.com",
            },
        )
        class_data = json.loads(course_res.text)
        return Msg().prosecess("获取成功", 200, class_data)

    def get_course_lessons(
        self, course_id: str, start: int = 0, limit: int = 200
    ) -> dict:
        lessons_url = (
            "http://www.cqooc.com/json/mooc/lessons"
            + f"?limit={limit}&start=0&sortby=selfId&reverse=false"
            + f"&courseId={course_id}&ts={int(time.time() * 1000)}"
        )
        lessons_res = self.__config.do_get(
            lessons_url,
            headers={
                "referer": "http://www.cqooc.com/learn"
                + "/mooc/structure?id=334569063",
                "host": "www.cqooc.com",
            },
        )
        lessons_data = json.loads(lessons_res.text)
        return Msg().prosecess("获取成功", 200, lessons_data)
