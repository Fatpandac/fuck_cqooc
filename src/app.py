# -*- coding: utf-8 -*-
from loginView import login_view
from skipView import skip_view

import flet as ft
import logging

logging.basicConfig(
    filename="fuckcqooc.log",
    filemode="w",
    level=logging.INFO,
)


def main(page: ft.Page):
    logging.info("Init main page")

    def on_route_change(e):
        page.views.clear()
        login_view(page)
        if e.route == "/course":
            skip_view(page)
        page.update()

    def view_pop():
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.core = None
    page.title = "Fuckcqooc"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.on_route_change = on_route_change
    page.on_view_pop = view_pop
    page.window_min_width = 800
    page.window_width = 800
    page.window_height = 600
    page.window_min_height = 600
    page.go(page.route)


ft.app(target=main)
