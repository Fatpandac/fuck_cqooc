# -*- coding: utf-8 -*-
from loginView import login_view
from skipView import skip_view
from reportView import report_view

import flet as ft
import logging
import tempfile
import os

log_location = f"{tempfile.gettempdir()+os.sep}fuckcqooc.log"
logging.basicConfig(
    filename=log_location,
    filemode="w",
    level=logging.INFO,
)
logging.info(f"Started logging to file {log_location}.")

exception: BaseException
font_family = {
    "Noto Sans SC": "/fonts/NotoSansSC-Regular.otf",
    "JetBrains Mono": "/fonts/JetBrainsMono-Regular.ttf",
}


def main(page: ft.Page):
    logging.info("Init main page")

    def on_route_change(e):
        page.views.clear()
        login_view(page)
        if e.route == "/course":
            skip_view(page)
        page.update()

    def on_error(e):
        logging.error("error")

    def view_pop():
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.core = None
    page.title = "Fuckcqooc"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.fonts = font_family
    page.on_route_change = on_route_change
    page.on_view_pop = view_pop
    page.on_error = on_error
    page.window_min_width = 800
    page.window_width = 800
    page.window_height = 600
    page.window_min_height = 600
    page.go(page.route)


def report(page: ft.Page):
    def on_route_change(e):
        page.views.clear()
        report_view(page)
        page.update()

    page.exception = exception
    page.log = log_location
    page.fonts = font_family
    page.title = "Fuckcqooc"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.on_route_change = on_route_change
    page.window_min_width = 800
    page.window_width = 800
    page.window_height = 600
    page.window_min_height = 600
    page.go(page.route)


try:
    ft.app(target=main, assets_dir="../assets")
except BaseException as e:
    exception = e
    ft.app(target=report, assets_dir="../assets")
