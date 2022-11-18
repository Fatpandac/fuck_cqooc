# -*- coding: utf-8 -*-
import flet as ft


def skip_view(page: ft.Page):
    courseList = ft.ListView(
        width=200,
    )
    taskList = ft.ListView(
        expand=True,
    )

    def choose_course(e):
        taskList.controls.clear()
        for i in range(e.control.data):
            taskList.controls.append(
                ft.Checkbox(
                    label=f"Unchecked by default checkbox {i}",
                    value=False,
                    data=i,
                )
            )
        page.update()

    for i in range(20):
        courseList.controls.append(
            ft.Column(
                [
                    ft.TextButton(
                        text="README.md",
                        style=ft.ButtonStyle(
                            shape={
                                "hovered": ft.RoundedRectangleBorder(),
                                "": ft.RoundedRectangleBorder(),
                            }
                        ),
                        width=200,
                        data=i,
                        on_click=choose_course,
                    ),
                ]
            )
        )

    def skip(e):
        chooseResults = filter(
            lambda x: x is not None,
            map(
                lambda x: x.data if x.value else None, taskList.controls.copy()
            ),
        )
        print(list(chooseResults))

    def choose_all(e):
        chooseAll = taskList.controls.copy()
        for i in chooseAll:
            i.value = not i.value
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
                                    on_click=choose_all,
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
