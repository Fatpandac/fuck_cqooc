# -*- coding: utf-8 -*-
from src.core.msg import Msg

sussess = {"code": 200, "status": "ok", "msg": "成功"}

fail = {"code": 400, "status": "fail", "msg": "失败"}


def test_prosecess_sussess():
    msg = Msg().processing(sussess["msg"], sussess["code"])
    assert msg["code"] == sussess["code"]
    assert msg["status"] == sussess["status"]
    assert msg["msg"] == sussess["msg"]


def test_prosecess_fail():
    msg = Msg().processing(fail["msg"], fail["code"])
    assert msg["code"] == fail["code"]
    assert msg["status"] == fail["status"]
    assert msg["msg"] == fail["msg"]
