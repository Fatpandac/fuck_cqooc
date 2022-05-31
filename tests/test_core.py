# -*- coding: utf-8 -*-
from src.core import Core

import os


# ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

username = os.environ.get("USERS")
password = os.environ.get("PASSWORD")


def test_login_success():
    if (username is None) or (password is None):
        print("!!! 请设置环境变量：USERS 和 PASSWORD !!!")
    core = Core(username, password)
    res = core.login()
    assert res["code"] == 200
    assert res["msg"] == "登录成功"


def test_login_fail():
    username_fail = "test"
    password_fail = "1234567"
    core = Core(username_fail, password_fail)
    res = core.login()
    assert res["code"] == 400
    assert res["msg"] == "登录失败，可能需要官网登录后重试"
    assert res["status"] == "fail"


def test_get_info():
    core = Core(username, password)
    res = core.get_user_info()
    assert res["username"] == username
    assert res["pwd"] == password
    assert res["xsid"] is None
    assert res["id"] is None
    assert res["name"] is None


def test_get_course():
    core = Core(username, password)
    core.login()
    res = core.get_course()
    assert res["code"] == 200
    assert res["status"] == "ok"
    assert res["data"] is not None


def test_get_course_lessons():
    core = Core(username, password)
    core.login()
    res = core.get_course_lessons(core.get_course()["data"][0]["courseId"])
    assert res["code"] == 200
    assert res["status"] == "ok"
    assert res["data"] is not None
