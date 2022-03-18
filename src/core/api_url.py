# -*- coding: utf-8 -*-

import time


class ApiUrl:
    def __get_ts(self) -> int:
        return int(time.time() * 1000)

    def id_api(self, xsid: str) -> str:
        return (
            "http://www.cqooc.com/user/session"
            + f"?xsid={xsid}&ts={self.__get_ts()}"
        )

    def info_api(self) -> str:
        return (
            "http://www.cqooc.com/account/session/api/profile/get"
            + f"?ts={self.__get_ts()}"
        )

    def get_nonce_api(self):
        return f"http://www.cqooc.net/user/login?ts={self.__get_ts()}"

    def login_api(self, username: str, hash: str, nonce: str, cn: str) -> str:
        return (
            "http://www.cqooc.com/user/login"
            + f"?username={username}&password={hash}"
            + f"&nonce={nonce}&cnonce={cn}"
        )

    def course_api(self, id: str, limit: int) -> str:
        return (
            "http://www.cqooc.com/json/mcs?sortby=id&reverse=true&del=2"
            + f"&courseType=2&ownerId={id}&limit={limit}"
            + f"&ts={self.__get_ts()}"
        )

    def lessons_api(
        self, course_id: str, start: int = 0, limit: int = 100
    ) -> str:
        return (
            "http://www.cqooc.com/json/mooc/lessons"
            + f"?limit={limit}&start={start}&sortby=selfId&reverse=false"
            + f"&courseId={course_id}&ts={self.__get_ts()}"
        )

    def lessons_status_api(
        self, course_id: str, username: str, start: int = 0, limit: int = 100
    ) -> str:
        return (
            "http://www.cqooc.com/json/learnLogs"
            + f"?limit={limit}&start={start}&courseId={course_id}"
            + f"&select=sectionId&username={username}&ts={self.__get_ts()}"
        )
