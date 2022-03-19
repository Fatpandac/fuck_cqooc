# -*- coding: utf-8 -*-
class Msg:
    def __init__(self):
        self.__sussess = {
            "code": 200,
            "status": "ok",
        }
        self.__fail = {
            "code": 400,
            "status": "fail",
        }

    def processing(self, msg: str, code: int, res: dict = {}) -> dict:
        if code == 200:
            res["code"] = self.__sussess["code"]
            res["status"] = self.__sussess["status"]
            res["msg"] = msg
        else:
            res["code"] = self.__fail["code"]
            res["status"] = self.__fail["status"]
            res["msg"] = msg
            res["data"] = None

        return res
