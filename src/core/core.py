# -*- coding: utf-8 -*-
from src.core.config import Config
from src.core.user import User
from src.core.test import test

import time
import requests
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
        id_res = requests.get(
            id_api,
            headers=self.__config.get_headers(),
            proxies=self.__config.get_proxies(),
        )
        id_data = json.loads(id_res.text)
        self.__user.set_id(id_data["id"])

        info_api = (
            "http://www.cqooc.com/account/session/api/profile/get"
            + f"?ts={self.__get_ts()}"
        )
        info_res = requests.get(
            info_api,
            headers=self.__config.get_headers(),
            proxies=self.__config.get_proxies(),
        )
        info_data = json.loads(info_res.text)
        self.__user.set_name(info_data["name"])
        self.__user.set_avatar(info_data["headimgurl"])

    def login(self) -> dict:
        nonce_res = requests.get(
            f"http://www.cqooc.net/user/login?ts={self.__get_ts()}",
            proxies=self.__config.get_proxies(),
        )
        data = json.loads(nonce_res.text)
        cn = test.cnonce()
        hash = test.getEncodePwd(
            data["nonce"] + test.getEncodePwd(self.__user.get_pwd()) + cn
        )
        apiUrl = (
            "http://www.cqooc.com/user/login"
            + f"?username={self.__user.get_username()}"
            + f'&password={hash}&nonce={data["nonce"]}&cnonce={cn}'
        )
        login_res = requests.post(
            apiUrl,
            headers=self.__config.get_headers(),
            proxies=self.__config.get_proxies(),
        )
        data = json.loads(login_res.text)
        login_success = data["code"] == 0
        if login_success:
            self.__user.set_xsid(data["xsid"])
            self.__config.set_headers("Cookie", f'xsid={data["xsid"]}')
            self.__process_user_info()
            data["code"] = 200
            data["msg"] = "登录成功"
            return data
        else:
            return {"status": "fail", "code": 400, "msg": "登录失败"}
