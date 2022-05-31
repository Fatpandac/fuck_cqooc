# -*- coding: utf-8 -*-

from src.core import Core
import os
import json

username = os.environ.get("USERS")
password = os.environ.get("PASSWORD")


def print_dict(d):
    print(json.dumps(d, indent=2, ensure_ascii=False))


def print_red_sentence(sentence):
    print(f"\033[31m{sentence}\033[0m")


def print_green_sentence(sentence):
    print(f"\033[32m{sentence}\033[0m")


def main():
    # Step 1, init object
    print_red_sentence("\nStep 1, init object")
    print_green_sentence(f"core = Core({username}, {password})")
    core = Core(username, password)

    # Stpe 2
    print_red_sentence("\nStpe 2, login to the cqooc, get cookies")
    print_green_sentence("core.login()")
    print_dict(core.login())

    # Stpe 3
    print_red_sentence("\nStep 3, get the course list")
    print_green_sentence("core.get_course()")
    print_dict(core.get_course())

    # Stpe 4
    print_red_sentence("\nStpe 4, get lesson list by course id")
    print_green_sentence("core.get_lesson_list(course_id)")
    lesson_data = core.get_course_lessons(
        core.get_user_info()["course_data"]["data"][0]["courseId"]
    )
    print_lesson_data = lesson_data.copy()
    print_lesson_data["data"] = [
        lesson_data["data"][0],
        lesson_data["data"][1],
        lesson_data["data"][2],
        "...",
    ]
    print_dict(print_lesson_data)

    # Last step
    print_red_sentence("\nLast step,skip lesson by section id")
    print_green_sentence("core.skip_lesson(section_id)")
    section_id = lesson_data["data"][0]["sectionId"]
    print_dict(core.skip_section(section_id))


if __name__ == "__main__":
    main()
