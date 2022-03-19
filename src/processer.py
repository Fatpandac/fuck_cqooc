# -*- coding: utf-8 -*-

import json
import requests


class Processer:
    def process_course_data(self, course_res: requests.Response) -> dict:
        res_course_data = json.loads(course_res.text)
        course_data = {}
        course_data["meta"] = res_course_data["meta"]
        course_data["data"] = []
        for course in res_course_data["data"]:
            course_data["data"].append(
                {
                    "courseId": course["courseId"],
                    "ownerId": course["ownerId"],
                    "title": course["course"]["title"],
                }
            )
        return course_data

    def process_lessons_data(
        self,
        username: str,
        lessons_res: requests.Response,
        lessons_status_res: requests.Response,
    ) -> dict:
        lessons_res_data = json.loads(lessons_res.text)
        lessons_status_res_data = json.loads(lessons_status_res.text)
        lessons_data = {}
        lessons_data["meta"] = lessons_res_data["meta"]
        lessons_data["data"] = []
        for lesson in lessons_res_data["data"]:
            lessons_data["data"].append(
                {
                    "title": lesson["title"],
                    "sectionId": lesson["id"],
                    "category": lesson["category"],
                    "chapterId": lesson["chapterId"],
                    "courseId": lesson["courseId"],
                    "ownerId": lesson["ownerId"],
                    "parentId": lesson["parentId"],
                    "id": lesson["id"],
                    "username": username,
                }
            )
        # add status
        lesson_status = [
            i["sectionId"] for i in lessons_status_res_data["data"]
        ]
        for lesson in lessons_data["data"]:
            if lesson["sectionId"] in lesson_status:
                lesson["status"] = 1
            else:
                lesson["status"] = 0
        # sort by sectionId
        lessons_data["data"] = sorted(
            lessons_data["data"], key=lambda x: x["sectionId"]
        )
        return lessons_data

    def process_section_data(self, section_data: dict, mcs_id: str) -> dict:
        post_data = {}
        post_data["action"] = 0
        post_data["category"] = 2
        post_data["chapterId"] = section_data["chapterId"]
        post_data["courseId"] = section_data["courseId"]
        post_data["ownerId"] = int(section_data["ownerId"])
        post_data["parentId"] = mcs_id
        post_data["sectionId"] = section_data["sectionId"]
        post_data["username"] = section_data["username"]
        return post_data
