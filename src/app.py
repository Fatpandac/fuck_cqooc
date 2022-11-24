# -*- coding: utf-8 -*-
from loginView import login_view
from skipView import skip_view

import flet as ft
import tempfile
import os
import logging
from logging.handlers import RotatingFileHandler

folder_path = f"{tempfile.gettempdir()+os.sep}fuckcqooc"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
else:
    # Empty the folder
    for file in os.listdir(folder_path):
        os.remove(folder_path + os.sep + file)

log_location = f"{folder_path+os.sep}fuckcqooc.log"
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(
    log_location, "a", maxBytes=1024 * 1024 * 5, backupCount=5
)
logger.addHandler(handler)
logging.info(f"Started logging to file {log_location}.")

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

    def view_pop():
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.core = None
    page.log_folder_path = folder_path
    page.title = "Fuckcqooc"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.fonts = font_family
    page.on_route_change = on_route_change
    page.on_view_pop = view_pop
    page.window_min_width = 800
    page.window_width = 800
    page.window_height = 600
    page.window_min_height = 600
    page.go(page.route)


ft.app(target=main, assets_dir="../assets")
