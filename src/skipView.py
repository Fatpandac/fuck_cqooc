import flet as ft


def skip_view(page: ft.Page):
    page.views.append(
        ft.View(
            "/skip",
            [
                ft.Text("Fuckcqooc", size=50),
            ]
        )
    )
