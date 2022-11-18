# -*- coding: utf-8 -*-
from components import show_snack_bar

import flet as ft
from hackcqooc.core import Core


def login_view(page: ft.page):
    account = ft.TextField(
        label="帐号", hint_text="请输入帐号", max_lines=1, width=400
    )
    password = ft.TextField(
        label="密码",
        hint_text="请输入密码",
        password=True,
        can_reveal_password=True,
        max_lines=1,
        width=400,
    )

    def login(_e):
        if not account.value:
            show_snack_bar(page, "请输入帐号", ft.colors.ERROR)
        elif not password.value:
            show_snack_bar(page, "请输入密码", ft.colors.ERROR)
        else:
            page.core = Core(account.value, password.value)
            login_res = page.core.login()
            if login_res["status"] == "ok":
                print(f"帐号: {account.value}, 密码: {password.value}")
                page.go("/course")
            else:
                show_snack_bar(page, login_res["msg"], ft.colors.ERROR)

    # View
    page.views.append(
        ft.View(
            "/",
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Fuckcqooc", size=50),
                                    account,
                                    password,
                                    ft.FilledButton(
                                        "登录",
                                        icon=ft.icons.LOGIN,
                                        on_click=login,
                                    ),
                                ],
                                alignment="center",
                            )
                        )
                    ],
                    alignment="center",
                    spacing=30,
                ),
            ],
            horizontal_alignment="center",
            vertical_alignment="center",
        )
    )
