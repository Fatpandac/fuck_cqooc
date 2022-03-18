# -*- coding: utf-8 -*-

from src.core.api_url import ApiUrl

import time


def get_ts():
    return int(time.time() * 1000)


xsid = "xsid"
id = "id"
username = "username"
hash = "hash"
nonce = "nonce"
cn = "cn"
course_id = "course_id"
start = 0
limit = 100


def test_id_api():
    api_url = ApiUrl()
    assert api_url.id_api(xsid) == (
        "http://www.cqooc.com/user/session" + f"?xsid={xsid}&ts={get_ts()}"
    )


def test_info_api():
    api_url = ApiUrl()
    assert api_url.info_api() == (
        "http://www.cqooc.com/account/session/api/profile/get"
        + f"?ts={get_ts()}"
    )


def test_nonce_api():
    api_url = ApiUrl()
    assert api_url.get_nonce_api() == (
        "http://www.cqooc.net/user/login" + f"?ts={get_ts()}"
    )


def test_login_api():
    api_url = ApiUrl()
    assert api_url.login_api(username, hash, nonce, cn) == (
        "http://www.cqooc.com/user/login"
        + f"?username={username}&password={hash}"
        + f"&nonce={nonce}&cnonce={cn}"
    )


def test_course_api():
    api_url = ApiUrl()
    assert api_url.course_api(id, limit) == (
        "http://www.cqooc.com/json/mcs?sortby=id&reverse=true&del=2"
        + f"&courseType=2&ownerId={id}&limit={limit}"
        + f"&ts={get_ts()}"
    )


def test_lessons_api():
    api_url = ApiUrl()
    assert api_url.lessons_api(course_id) == (
        "http://www.cqooc.com/json/mooc/lessons"
        + f"?limit={limit}&start={start}&sortby=selfId&reverse=false"
        + f"&courseId={course_id}&ts={get_ts()}"
    )


def test_lessons_status_api():
    api_url = ApiUrl()
    assert api_url.lessons_status_api(course_id, username) == (
        "http://www.cqooc.com/json/learnLogs"
        + f"?limit={limit}&start={start}&courseId={course_id}&select=sectionId"
        + f"&username={username}&ts={get_ts()}"
    )
