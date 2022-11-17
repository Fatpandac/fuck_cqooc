import flet as ft
from hackcqooc.core import Core


def login_view(page: ft.page):
    account = ft.TextField(label="帐号", hint_text="请输入帐号",
                           max_lines=1, width=400)
    password = ft.TextField(
        label="密码",
        hint_text="请输入密码",
        password=True,
        can_reveal_password=True,
        max_lines=1,
        width=400,
    )

    def login(_e):
        def login_show_snack_bar(text):
            return page.show_snack_bar(
                ft.SnackBar(
                    open=True,
                    content=ft.Text(text),
                    bgcolor=ft.colors.ERROR,
                )
            )

        if not account.value:
            login_show_snack_bar("请输入帐号")
        elif not password.value:
            login_show_snack_bar("请输入密码")
        else:
            page.core = Core(account.value, password.value)
            login_res = page.core.login()
            if login_res["status"] == "ok":
                print(f"帐号: {account.value}, 密码: {password.value}")
                page.go("/course")
            else:
                login_show_snack_bar(login_res["msg"])

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
