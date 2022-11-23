# -*- coding: utf-8 -*-
from components import show_snack_bar

import flet as ft

from skipper import skipper as skp
from time import sleep
import logging


def skip_view(page: ft.Page):
    # TODO: 添加列表搜索框
    courseList = ft.ListView(
        width=230,
    )
    taskList = ft.ListView(
        expand=True,
    )
    taskIndicator = ft.Ref[ft.ProgressBar]()
    topTitle = ft.Ref[ft.Text]()

    def disabled_course_list_button(index: int):
        """设置禁用课程按钮"""
        for buttonIndex, textButton in enumerate(courseList.controls.copy()):
            textButton.disabled = True if index == buttonIndex else False
        page.update()

    def update_top_title(title: str):
        """更新当前页面标题"""
        topTitle.current.value = title
        page.update()

    def choose_course(e=None):
        if e is not None:
            # 调用来自点击事件，当前课程信息更新为新课程
            index, course_id, title = e.control.data
            page.current_course = [index, course_id, title]
        else:
            # 主动调用，使用之前保存的当前课程信息
            index, course_id, title = page.current_course
        # 获取课程任务列表
        taskIndicator.current.visible = True
        taskIndicator.current.value = None
        page.update()
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
        taskIndicator.current.visible = False
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

        def close_alert():
            """关闭对话框"""
            no_data_alert.open = False
            page.update()

        no_data_alert = ft.AlertDialog(
            modal=True,
            title=ft.Text("提示"),
            content=ft.Text(f"获取课程数据失败，错误代码是{course_dict.get('code')}。"),
            actions=[
                ft.TextButton("好", on_click=close_alert),
            ],
            actions_alignment="end",
        )
        page.dialog = no_data_alert
        no_data_alert.open = True
        page.update()

    page.isOnSkipping = False

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

        logging.info(f"Task List: {chooseResults}")
        logging.info(f"Value of isOnSkipping: {page.isOnSkipping}")

        if len(chooseResults) == 0:
            show_snack_bar(page, "你还没有选择课程哟〜", ft.colors.ERROR)
        elif page.isOnSkipping:
            show_snack_bar(page, "有刷课任务正在进行，请结束后再试〜", ft.colors.ERROR)
        else:

            def close_alert(e):
                """关闭对话框，恢复标题文字，并更新任务列表"""
                page.isOnSkipping = False
                success_dialog.open = False
                taskIndicator.current.visible = False
                taskIndicator.current.value = 0
                topTitle.current.value = page.current_course[2]
                choose_course()
                page.update()

            def start_skip_task():
                """执行刷课任务"""
                taskIndicator.current.value = 0
                while skipper.getState() is not True:
                    taskIndicator.current.value = (
                        taskIndicator.current.value + (1 / 1000)
                    )
                    topTitle.current.value = (
                        f"🕓 正在刷课中，当前第{skipper.current}个，"
                        + f"共{len(chooseResults)}个。"
                    )
                    page.update()
                    sleep(duration / 1000)

            def wait_indicator_finish():
                """处理任务完成但进度条没满的情况"""
                while taskIndicator.current.value < 1:
                    taskIndicator.current.value = (
                        taskIndicator.current.value + (1 / 1000)
                    )
                    page.update()
                    sleep(duration / 1000)

            taskIndicator.current.visible = True
            skipper = skp(page.core, chooseResults)
            skipper.start()
            page.isOnSkipping = True
            duration = 31 * len(chooseResults) if len(chooseResults) > 1 else 1

            start_skip_task()
            wait_indicator_finish()

            success_dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("任务完成"),
                content=ft.Text(
                    f"任务结束。执行了{len(chooseResults)}个任务，"
                    + f"成功{skipper.success}个，失败{skipper.fail}个。"
                ),
                actions=[
                    ft.TextButton("好", on_click=close_alert),
                ],
                actions_alignment="end",
            )
            page.dialog = success_dialog
            success_dialog.open = True
            page.update()
        logging.info("Skip is finished.")

    def select_all(e):
        task_list_controls = taskList.controls.copy()
        have_unfinish_task = any(
            map(lambda task: not task.disabled, task_list_controls)
        )
        have_selection_some_task = len(
            list(filter(lambda task: task.value, task_list_controls))
        ) < len(task_list_controls)

        if have_unfinish_task:
            if have_selection_some_task:
                for task in task_list_controls:
                    task.value = True
            else:
                for i in task_list_controls:
                    i.value = not i.value if i.disabled is False else i.value
            page.update()
        else:
            show_snack_bar(page, "该课全部课程都已经刷完了 ^_^", ft.colors.GREEN)

    page.views.append(
        ft.View(
            "/skip",
            [
                ft.Stack(
                    [
                        ft.ProgressBar(
                            ref=taskIndicator, value=0, visible=False
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text(
                                        ref=topTitle,
                                        value="请选择需要刷课的课程",
                                        size=30,
                                        font_family="Noto Sans SC",
                                    ),
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                "全选",
                                                icon=ft.icons.ALL_INBOX,
                                                on_click=select_all,
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
                    ]
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
