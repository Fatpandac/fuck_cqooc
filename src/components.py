# -*- coding: utf-8 -*-
import flet as ft


def show_snack_bar(page, text, color):
    return page.show_snack_bar(
        ft.SnackBar(
            open=True,
            content=ft.Text(text),
            bgcolor=color,
        )
    )
