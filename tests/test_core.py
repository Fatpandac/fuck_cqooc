# -*- coding: utf-8 -*-
from src.core.core import Core

import os


# ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")


def test_login_success():
    core = Core(username, password)
    res = core.login()
    assert res["code"] == 200
    assert res["msg"] == "登录成功"


def test_login_fail():
    username = "test"
    password = "1234567"
    core = Core(username, password)
    res = core.login()
    assert res["code"] == 400
    assert res["msg"] == "登录失败"
    assert res["status"] == "fail"


def test_get_info():
    core = Core(username, password)
    res = core.get_user_info()
    assert res["username"] == username
    assert res["pwd"] == password
    assert res["xsid"] is None
    assert res["id"] is None
    assert res["name"] is None
    assert res["avatar"] is None


def test_get_class():
    core = Core(username, password)
    core.login()
    res = core.get_class()
    assert res["code"] == 200
    assert res["status"] == "ok"
    assert res["data"] is not None
