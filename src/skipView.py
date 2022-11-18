# -*- coding: utf-8 -*-
import flet as ft


def skip_view(page: ft.Page):
    # TODO: 添加列表搜索框
    courseList = ft.ListView(
        width=200,
    )
    taskList = ft.ListView(
        expand=True,
    )

    def disabled_course_list_button(index: int):
        """设置禁用按钮"""
        for buttonIndex, textButton in enumerate(courseList.controls.copy()):
            textButton.disabled = True if index == buttonIndex else False
        page.update()

    def choose_course(e):
        index, course_id = e.control.dat
        disabled_course_list_button(index)
        # 获取课程任务列表
        task_list = page.core.get_course_lessons(course_id).get("data")
        taskList.controls.clear()
        for task in task_list:
            taskList.controls.append(
                ft.Checkbox(
                    label="没有描述"
                    if task.get("title") is None
                    else task.get("title"),
                    value=False if task.get("status") == 0 else True,
                    disabled=False if task.get("status") == 0 else True,
                    data=task.get("sectionId"),
                )
            )
        page.update()

    course_dict = page.core.get_course()
    if course_dict.get("code") == 200:
        page.course_list = course_dict.get("data")
        for index, course_item in enumerate(page.course_list):
            courseList.controls.append(
                ft.TextButton(
                    text=course_item.get("title"),
                    style=ft.ButtonStyle(
                        shape={
                            "hovered": ft.RoundedRectangleBorder(),
                            "": ft.RoundedRectangleBorder(),
                        }
                    ),
                    data=(index, course_item.get("courseId")),
                    on_click=choose_course,
                    disabled=False,
                ),
            )
    else:
        # TODO: 提示课程获取异常
        pass

    def skip(e):
        chooseResults = filter(
            lambda x: x is not None,
            map(
                lambda x: x.data if x.value and not x.disabled else None,
                taskList.controls.copy(),
            ),
        )
        print(list(chooseResults))

    def reverse_selection(e):
        chooseAll = taskList.controls.copy()
        for i in chooseAll:
            i.value = not i.value if i.disabled is False else i.value
        page.update()

    page.views.append(
        ft.View(
            "/skip",
            [
                ft.Row(
                    [
                        ft.Text("选择需要刷课的课程", size=30),
                        ft.Row(
                            [
                                ft.FilledButton(
                                    "全选",
                                    icon=ft.icons.ALL_INBOX,
                                    on_click=reverse_selection,
                                ),
                                ft.FilledButton(
                                    "Fuck",
                                    icon=ft.icons.DONE,
                                    on_click=skip,
                                ),
                            ],
                            alignment="center",
                            spacing=50,
                        ),
                    ],
                    alignment="spaceBetween",
                ),
                ft.Row(
                    [courseList, ft.VerticalDivider(width=5), taskList],
                    expand=True,
                ),
            ],
        )
    )
