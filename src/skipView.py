# -*- coding: utf-8 -*-
from components import show_snack_bar

import flet as ft


def skip_view(page: ft.Page):
    # TODO: 添加列表搜索框
    courseList = ft.ListView(
        width=230,
    )
    taskList = ft.ListView(
        expand=True,
    )
    topTitle = ft.Text("请选择需要刷课的课程", size=30)

    def disabled_course_list_button(index: int):
        """设置禁用按钮"""
        for buttonIndex, textButton in enumerate(courseList.controls.copy()):
            textButton.disabled = True if index == buttonIndex else False
        page.update()

    def update_top_title(title: str):
        """更新当前页面标题"""
        topTitle.value = title
        page.update()

    def choose_course(e):
        index, course_id, title = e.control.data
        # 获取课程任务列表
        task_list = page.core.get_course_lessons(course_id).get("data")

        disabled_course_list_button(index)
        update_top_title(title)

        taskList.controls.clear()
        for task in task_list:
            title = "没有描述" if task.get("title") is None else task.get("title")
            taskList.controls.append(
                ft.Checkbox(
                    label=title,
                    value=False if task.get("status") == 0 else True,
                    disabled=False if task.get("status") == 0 else True,
                    data=task.get("sectionId"),
                )
            )
        page.update()

    def show_omit_title(title):
        """当 title 长度大于 16 时返回缩略内容，显示文字为14长度其余以 ... 替代"""
        return f"{title[:14]}..." if len(title) > 16 else title

    course_dict = page.core.get_course()
    if course_dict.get("code") == 200:
        page.course_list = course_dict.get("data")
        for index, course_item in enumerate(page.course_list):
            title = course_item.get("title")
            courseList.controls.append(
                ft.TextButton(
                    text=show_omit_title(title),
                    tooltip=title if len(title) > 16 else None,
                    style=ft.ButtonStyle(
                        shape={
                            "hovered": ft.RoundedRectangleBorder(),
                            "": ft.RoundedRectangleBorder(),
                        }
                    ),
                    data=(
                        index,
                        course_item.get("courseId"),
                        course_item.get("title"),
                    ),
                    on_click=choose_course,
                    disabled=False,
                ),
            )
    else:
        # TODO: 提示课程获取异常
        pass

    def skip(e):
        chooseResults = list(
            filter(
                lambda x: x is not None,
                map(
                    lambda x: x.data if x.value and not x.disabled else None,
                    taskList.controls.copy(),
                ),
            )
        )
        if len(chooseResults) == 0:
            show_snack_bar(page, "你还没有选择课程哟〜", ft.colors.ERROR)
        else:
            # TODO: 进行刷课
            pass
        print(chooseResults)

    def reverse_selection(e):
        task_list_controls = taskList.controls.copy()
        have_unfinish_task = any(
            map(lambda task: not task.disabled, task_list_controls)
        )

        if have_unfinish_task:
            for i in task_list_controls:
                i.value = not i.value if i.disabled is False else i.value
            page.update()
        else:
            show_snack_bar(page, "全部课程都已经刷完了 ^_^", ft.colors.GREEN)

    page.views.append(
        ft.View(
            "/skip",
            [
                ft.Container(
                    content=ft.Row(
                        [
                            topTitle,
                            ft.Row(
                                [
                                    ft.ElevatedButton(
                                        "全选",
                                        icon=ft.icons.ALL_INBOX,
                                        on_click=reverse_selection,
                                    ),
                                    ft.ElevatedButton(
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
                    padding=10,
                ),
                ft.Divider(
                    height=1,
                ),
                ft.Row(
                    [courseList, ft.VerticalDivider(width=1), taskList],
                    expand=True,
                    spacing=0,
                ),
            ],
            padding=0,
            spacing=0,
        )
    )
