# -*- coding: utf-8 -*-
class Msg:

    __sussess = {
        "code": 200,
        "status": "ok",
    }

    __fail = {
        "code": 400,
        "status": "fail",
    }

    def prosecess(self, msg: str, code: int, res: dict = {}) -> dict:
        if code == 200:
            res["code"] = self.__sussess["code"]
            res["status"] = self.__sussess["status"]
            res["msg"] = msg
        else:
            res["code"] = self.__fail["code"]
            res["status"] = self.__fail["status"]
            res["msg"] = msg

        return res
