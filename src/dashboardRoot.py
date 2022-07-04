# -*- coding: utf-8 -*-
from hackcqooc.core import Core

from sys import exit
import ttkbootstrap as ttk
from ttkbootstrap.constants import X
from ttkbootstrap.constants import YES
from ttkbootstrap.constants import LEFT
from ttkbootstrap.constants import NE
from ttkbootstrap.constants import BOTH
from ttkbootstrap.constants import HEADINGS
from ttkbootstrap.constants import END
from ttkbootstrap.constants import SUCCESS
from ttkbootstrap.constants import OUTLINE
from ttkbootstrap.constants import INFO
from ttkbootstrap.constants import STRIPED
from ttkbootstrap.constants import DISABLED
from ttkbootstrap.constants import NORMAL
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.dialogs import MessageDialog
from ttkbootstrap.icons import Icon
from src.exceptionHandler import exceptionHandler

from src.skipper import skipper


class dashboardRoot(ttk.Window):
    def __init__(self) -> None:
        super().__init__()

        self.core = None
        self.courseID = None

        # 设置基础视图
        self.title("fuck_cqooc")
        self.geometry("800x500")
        self.resizable(False, False)
        ttk.Style().theme_use("darkly")

        # 定义控件
        self.root = ttk.Frame(self, padding=10)
        self.setupLoginFrame()
        # 根
        self.root.pack(fill=X, expand=YES)

    def start(self) -> None:
        """启动登录界面"""
        self.mainloop()

    def setupLoginFrame(self) -> None:
        """设置登陆界面框架，需要首先保证根里面没有组件"""
        self.loginFrame = ttk.Frame(self.root)
        self.labelWelcome = ttk.Label(self.loginFrame, text="fuck_cqooc")

        self.usernameFrame = ttk.Frame(self.loginFrame)
        self.labelUsername = ttk.Label(
            self.usernameFrame, text="用户名:", width=6
        )
        self.varUsername = ttk.StringVar(self.usernameFrame)
        self.entryUsername = ttk.Entry(
            self.usernameFrame, width=200, textvariable=self.varUsername
        )

        self.passwordFrame = ttk.Frame(self.loginFrame)
        self.labelPassword = ttk.Label(self.passwordFrame, text="密码:", width=6)
        self.varPassword = ttk.StringVar(self.passwordFrame)
        self.entryPassword = ttk.Entry(
            self.passwordFrame,
            width=200,
            textvariable=self.varPassword,
            show="*",
        )

        self.buttonLogin = ttk.Button(
            self.loginFrame, text="登录", command=self.login, width=30
        )

        # 提示语部分
        self.labelWelcome.pack(pady=10)
        self.labelWelcome.config(font=("Microsoft Yahei", 15))

        # 用户名模块
        self.labelUsername.pack(side=LEFT, anchor=NE, pady=(10, 0), fill=X)
        self.entryUsername.pack(
            side=LEFT, padx=(10, 0), pady=(10, 0), expand=YES, fill=BOTH
        )
        self.usernameFrame.pack()

        # 密码模块
        self.labelPassword.pack(side=LEFT, anchor=NE, pady=(10, 0), fill=X)
        self.entryPassword.pack(
            side=LEFT, padx=(10, 0), pady=(10, 0), expand=YES, fill=BOTH
        )
        self.passwordFrame.pack()

        # 登录按钮
        self.buttonLogin.pack(pady=(10, 0))
        # 整个登录模块
        self.loginFrame.pack()

    def disposeLoginFrame(self) -> None:
        """清除登录框架"""
        self.loginFrame.destroy()

    def setupDashboardFrame(self) -> None:
        # 定义所有框架
        self.welcomeFrame = ttk.Frame(self.root)
        self.contentWrapperFrame = ttk.Frame(self.root)
        self.courseFrame = ttk.Frame(self.contentWrapperFrame)
        self.lessonFrame = ttk.Frame(self.contentWrapperFrame)
        self.actionFrame = ttk.Frame(self.root)
        self.progressFrame = ttk.Frame(self.root)

        # 放置所有框架
        self.welcomeFrame.pack()
        self.contentWrapperFrame.pack()
        self.courseFrame.pack(side=LEFT)
        self.lessonFrame.pack(side=LEFT)
        self.actionFrame.pack()
        self.progressFrame.pack(fill=X, expand=YES, pady=(20, 0))

        # 设置顶部状态提示语
        self.labelWelcome = ttk.Label(
            self.welcomeFrame, text=f"当前登录用户为{self.varUsername.get()}"
        )
        self.labelWelcome.config(font=("Microsoft Yahei", 15))
        self.labelWelcome.pack(side=LEFT, padx=(20, 0), pady=(0, 20))

        # 设置课程列表
        self.treeCourse = ttk.Treeview(
            master=self.courseFrame, columns=[0], show=HEADINGS, height=10
        )
        self.courseList = self.getCourseDict()["course"]
        for i in self.courseList:
            t = (i[0],)
            self.treeCourse.insert("", END, values=t)
        self.treeCourse.heading(0, text="课程名称")
        self.treeCourse.column(0, width=400)
        self.treeCourse.bind("<<TreeviewSelect>>", self.displayLessonsByEvent)
        self.treeCourse.pack(side=LEFT)

        # 设置任务列表
        self.treeLesson = ttk.Treeview(
            master=self.lessonFrame,
            columns=[0, 1, 2, 3],
            show=HEADINGS,
            height=10,
        )
        self.treeLesson.insert(
            "", END, values=("☐", "点击左侧列表课程来选择", "未完成", "1000")
        )
        self.treeLesson.heading(0, text="勾选")
        self.treeLesson.heading(1, text="任务名称")
        self.treeLesson.heading(2, text="完成情况")
        self.treeLesson.heading(3, text="sectionID")
        self.treeLesson.column(0, width=50)
        self.treeLesson.column(1, width=350)
        self.treeLesson.column(2, width=100)
        self.treeLesson.column(3, width=0)
        self.treeLesson["displaycolumns"] = [0, 1, 2]
        self.treeLesson.bind("<<TreeviewSelect>>", self.processCheckbox)
        self.treeLesson.pack(side=LEFT)

        # 设置功能按钮
        self.buttonExit = ttk.Button(
            master=self.actionFrame,
            text="退出",
            bootstyle=(INFO, OUTLINE),
            command=exit,
            width=10,
        )
        self.buttonSelectAll = ttk.Button(
            master=self.actionFrame,
            text="全选",
            bootstyle=(INFO, OUTLINE),
            width=10,
        )
        self.buttonProceed = ttk.Button(
            master=self.actionFrame, text="fuck", bootstyle=SUCCESS, width=10
        )
        self.buttonSelectAll.bind("<Button-1>", self.selectAll)
        self.buttonProceed.bind("<Button-1>", self.proceedTask)
        self.buttonExit.pack(side=LEFT, pady=(20, 0))
        self.buttonSelectAll.pack(side=LEFT, padx=(400, 0), pady=(20, 0))
        self.buttonProceed.pack(side=LEFT, padx=(50, 0), pady=(20, 0))

        # 设置进度条
        self.progressBar = ttk.Progressbar(
            master=self.progressFrame,
            orient=ttk.HORIZONTAL,
            value=0,
            bootstyle=(SUCCESS, STRIPED),
        )
        self.progressText = ttk.Label(master=self.progressFrame, text="")
        self.progressBar.pack(fill=X, padx=(30, 30), expand=YES)
        self.progressText.pack()

    def login(self) -> None:
        """登录"""
        username = self.varUsername.get()
        password = self.varPassword.get()
        if username == "" or password == "":
            Messagebox.show_error("用户名或密码不能为空。", "错误")
            return

        self.core = Core(username, password)
        try:
            loginResult = self.core.login()
        except Exception as ex:
            exceptionHandler(master=self, e=ex).start()

        self.buttonLogin["text"] = "登录"
        if loginResult["status"] == "ok":
            self.geometry("1000x500")
            self.disposeLoginFrame()
            self.setupDashboardFrame()
            infoMessage = "因为重庆高校在线课程平台服务器的管控策略，短时间跳过太多\000\n"
            infoMessage += "可能会遭到网站临时屏蔽。因此，跳过每个任务之间都会间隔一\000\n段时间。\n"
            infoMessage += "跳过某一门课程之前，请先注意这门课程是否已经结束。"
            MessageDialog(
                message=infoMessage,
                title="提示",
                parent=None,
                buttons=["我知道了:primary"],
                icon=Icon.info,
                localize=True,
            ).show(None)
        else:
            Messagebox.show_error(
                "登录失败。\n1. 你的用户名或密码可能有误\n2. 你可能需要前往网站手动登录，然后再试一次", "提示"
            )

    def getCourseDict(self) -> dict:
        courseDict = dict()
        courseList = list()
        courseData = self.core.get_course()
        courseDict["count"] = courseData["meta"]["total"]
        for i in courseData["data"]:
            courseList.append((i["title"], i["courseId"]))
        courseDict["course"] = courseList
        return courseDict

    def displayLessonsByEvent(self, e) -> None:
        selection = e.widget.item(e.widget.selection()[0])["values"]
        for i in self.courseList:
            if i[0] == selection[0]:
                courseID = i[1]
        self.courseID = courseID
        taskData = self.core.get_course_lessons(course_id=courseID)
        taskList = list()
        for i in taskData["data"]:
            if i["category"] not in ["2", "3"]:  # 判断是不是测验
                name = i["title"]
                status = "完成" if i["status"] == 1 else "未完成"
                sectionID = i["sectionId"]
                taskList.append(("☐", name, status, sectionID))
        # 清空列表
        for i in self.treeLesson.get_children():
            self.treeLesson.delete(i)
        for i in taskList:
            self.treeLesson.insert("", END, values=i)

    def displayLessonsById(self) -> None:
        taskData = self.core.get_course_lessons(course_id=self.courseID)
        taskList = list()
        for i in taskData["data"]:
            if i["category"] not in ["2", "3"]:  # 判断是不是测验
                name = i["title"]
                status = "完成" if i["status"] == 1 else "未完成"
                sectionID = i["sectionId"]
                taskList.append(("☐", name, status, sectionID))
        # 清空列表
        for i in self.treeLesson.get_children():
            self.treeLesson.delete(i)
        for i in taskList:
            self.treeLesson.insert("", END, values=i)

    def processCheckbox(self, e) -> None:
        selection = e.widget.item(e.widget.selection()[0])["values"]
        if selection[0] == "☐":
            selection[0] = "☑"
        elif selection[0] == "☑":
            selection[0] = "☐"
        e.widget.item(e.widget.selection()[0], values=tuple(selection))

    def selectAll(self, e) -> None:
        for i in self.treeLesson.get_children():
            item = self.treeLesson.item(i)["values"]
            if item[0] == "☐":
                item[0] = "☑"
            self.treeLesson.item(i, values=item)

    def proceedTaskAfter(self, skipper: skipper) -> None:
        # 利用标志位检查完成情况
        if skipper.getState():
            # 执行完成
            self.progressBar["value"] = 100
            self.progressText.config(text="执行完成。")
            # 恢复按钮到可点击状态
            self.buttonSelectAll["state"] = NORMAL
            self.buttonProceed["state"] = NORMAL
            # 清空列表
            for i in self.treeLesson.get_children():
                self.treeLesson.delete(i)
            self.displayLessonsById()
            Messagebox.show_info(
                f"跳过完成。\n成功跳过{skipper.success}个任务，失败{skipper.fail}个。", "提示"
            )

            def clearStatus(self):
                self.progressText.config(text="")
                self.progressBar["value"] = 0

            self.after(10000, clearStatus, self)
        else:
            # 任务未完成
            self.progressBar["value"] = 100 * (
                skipper.current / len(skipper.sectionList)
            )
            self.progressText.config(
                text=f"正在处理第{skipper.current}个，共{len(skipper.sectionList)}个。"
            )
            # 每100ms检查一次
            self.after(1000, self.proceedTaskAfter, skipper)

    def proceedTask(self, e) -> None:
        sectionList = list()
        skipThread = None
        # 获取勾选的任务sectionID
        for i in self.treeLesson.get_children():
            item = self.treeLesson.item(i)["values"]
            if item[0] == "☑":
                sectionList.append(str(item[3]))
        skipThread = skipper(core=self.core, sectionList=sectionList)
        skipThread.start()
        # 关闭按钮，防止任务执行过程中再次点击
        self.buttonSelectAll["state"] = DISABLED
        self.buttonProceed["state"] = DISABLED
        # 开始进度条之前需要先清空
        self.progressBar["value"] = 0
        # 开启回调，检查任务执行情况
        self.after(100, self.proceedTaskAfter, skipThread)
