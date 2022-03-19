# -*- coding: utf-8 -*-
from src.processer import Processer

section_data = {
    "chapterId": "23129809",
    "courseId": "2321421322",
    "ownerId": "21345567",
    "sectionId": "231298",
    "username": "2312421321213",
}
mcs_id = "231298"


def test_process_section_data():
    processer = Processer()
    post_data = processer.process_section_data(section_data, mcs_id)
    assert post_data["chapterId"] == "23129809"
    assert post_data["courseId"] == "2321421322"
    assert post_data["ownerId"] == 21345567
    assert post_data["sectionId"] == "231298"
    assert post_data["username"] == "2312421321213"
    assert post_data["parentId"] == "231298"
    assert post_data["action"] == 0
    assert post_data["category"] == 2
