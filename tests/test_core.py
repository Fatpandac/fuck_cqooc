# -*- coding: utf-8 -*-
from src.core.core import Core

import os


ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")


def test_core_login_success():
    core = Core(username, password)
    res = core.login()
    assert res["code"] == 200
    assert res["msg"] == "登录成功"


def test_core_login_fail():
    username = "test"
    password = "1234567"
    core = Core(username, password)
    res = core.login()
    assert res["code"] == 400
    assert res["msg"] == "登录失败"
    assert res["status"] == "fail"
