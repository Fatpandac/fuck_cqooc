# -*- coding: utf-8 -*-
from src.request import Request
from src.user import User
from src.msg import Msg
from src.test import test
from src.processer import Processer
from src.api_url import ApiUrl

import json


class Core:
    def __init__(self, username: str, pwd: str) -> None:
        self.__processer = Processer()
        self.__request = Request()
        self.__api_url = ApiUrl()
        self.__user = User(username, pwd)

    def __process_user_info(self) -> None:
        id_res = self.__request.do_get(
            self.__api_url.id_api(self.__user.get_xsid())
        )
        id_data = json.loads(id_res.text)
        self.__user.set_id(id_data["id"])

        info_res = self.__request.do_get(self.__api_url.info_api())
        info_data = json.loads(info_res.text)
        self.__user.set_name(info_data["name"])
        self.__user.set_avatar(
            self.__request.get_host() + info_data["headimgurl"]
        )

    def login(self) -> dict:
        nonce_res = self.__request.do_get(self.__api_url.get_nonce_api())
        data = json.loads(nonce_res.text)
        cn = test.cnonce()
        hash = test.getEncodePwd(
            data["nonce"] + test.getEncodePwd(self.__user.get_pwd()) + cn
        )
        login_res = self.__request.do_post(
            self.__api_url.login_api(
                self.__user.get_username(), hash, data["nonce"], cn
            )
        )
        data = json.loads(login_res.text)
        login_success = data["code"] == 0
        if login_success:
            self.__user.set_xsid(data["xsid"])
            self.__request.set_headers("Cookie", f'xsid={data["xsid"]}')
            self.__process_user_info()
            return Msg().processing("登录成功", 200, data)
        else:
            return Msg().processing("登录失败，可能需要官网登录后重试", 400, data)

    def get_user_info(self) -> dict:
        return Msg().processing("登录成功", 200, self.__user.get_info())

    def get_course(self, limit: int = 20) -> dict:
        course_res = self.__request.do_get(
            self.__api_url.course_api(self.__user.get_id(), limit),
            headers={
                "Referer": "http://www.cqooc.com/my/learn",
                "Host": "www.cqooc.com",
            },
        )
        course_data = self.__processer.process_course_data(course_res)
        self.__user.set_course_data(course_data.copy())
        return Msg().processing("获取课程成功", 200, self.__user.get_course_data())

    def get_course_lessons(self, course_id: str) -> dict:
        mcs_id_res = self.__request.do_get(
            self.__api_url.mcs_id_api(self.__user.get_id(), course_id),
            headers={
                "Referer": "http://www.cqooc.com/my/learn",
                "Host": "www.cqooc.com",
            },
        )
        mcs_id_data = json.loads(mcs_id_res.text)
        self.__user.set_mcs_id(mcs_id_data["data"][0]["id"])
        lessons_res = self.__request.do_get(
            self.__api_url.lessons_api(course_id),
            headers={
                "Referer": "http://www.cqooc.com/learn"
                + f"/mooc/structure?id={course_id}",
                "host": "www.cqooc.com",
            },
        )
        lessons_status_res = self.__request.do_get(
            self.__api_url.lessons_status_api(
                course_id, self.__user.get_username()
            ),
            headers={
                "Referer": (
                    "http://www.cqooc.com/learn/mooc/progress"
                    + f"?id={course_id}"
                ),
                "host": "www.cqooc.com",
            },
        )
        lessons_data = self.__processer.process_lessons_data(
            self.__user.get_username(), lessons_res, lessons_status_res
        )
        self.__user.set_lessons_data(lessons_data.copy())
        return Msg().processing(
            "获取课程课时成功", 200, self.__user.get_lessons_data()
        )

    def skip_section(self, section_id: str) -> dict:
        section_data = list(
            filter(
                lambda d: d["id"] == section_id,
                self.__user.get_lessons_data()["data"],
            )
        )[0]
        post_data = self.__processer.process_section_data(
            section_data, self.__user.get_mcs_id()
        )
        skip_res = self.__request.do_post(
            self.__api_url.skip_section_api(),
            data=json.dumps(post_data),
            headers={
                "Referer": "http://www.cqooc.com/learn/mooc/structure?id="
                + section_data["courseId"],
                "Host": "www.cqooc.com",
            },
        )
        status_code = json.loads(skip_res.text)["code"]
        if status_code == 2:
            return Msg().processing("已经跳过该课程", 200)
        elif status_code == 0:
            return Msg().processing("跳过课程成功", 200)
        elif status_code == 1:
            return Msg().processing("非法操作", 400)
        else:
            return Msg().processing("跳过课程失败", 400)
