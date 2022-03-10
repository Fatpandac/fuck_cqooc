# -*- coding: utf-8 -*-
from src.core.config import Config
from src.core.test import test

import time
import requests
import json


class Core:
    def __init__(self, username: str, pwd: str):
        self.__config = Config(pwd, username)

    def login(self) -> dict:
        r = requests.get(
            f"http://www.cqooc.net/user/login?ts={int(time.time()*1000)}",
            proxies=self.__config.get_proxies(),
        )
        data = json.loads(r.text)
        cn = test.cnonce()
        hash = test.getEncodePwd(
            data["nonce"] + test.getEncodePwd(self.__config.get_pwd()) + cn
        )

        apiUrl = (
            "http://www.cqooc.com/user/login"
            + f"?username={self.__config.get_username()}"
            + f'&password={hash}&nonce={data["nonce"]}&cnonce={cn}'
        )
        r = requests.post(
            apiUrl,
            headers=self.__config.get_headers(),
            proxies=self.__config.get_proxies(),
        )
        data = json.loads(r.text)
        if data["code"] == 0:
            self.__config.set_headers("cookie", f'XSID={data["xsid"]};')
            data["code"] = 200
            data["msg"] = "登录成功"
            return data
        else:
            return {"status": "fail", "code": 400, "msg": "登录失败"}
