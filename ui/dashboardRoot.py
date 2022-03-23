import sys
sys.path.append('..')
from src.core import Core

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from tkinter.ttk import Style

class dashboardRoot(ttk.Window):
    def __init__(self) -> None:
        super().__init__()

        # 设置基础视图
        self.title("fuck_cqooc")
        self.geometry("800x500")

        # 定义控件
        self.root = ttk.Frame(self,padding=10)
        self.__setupLoginFrame()
        # 根
        self.root.pack(fill=X,expand=YES)

    def start(self):
        '''启动登录界面'''
        self.mainloop()

    def __setupLoginFrame(self):
        '''设置登陆界面框架，需要首先保证根里面没有组件'''
        self.loginFrame = ttk.Frame(self.root)
        self.labelWelcome = ttk.Label(self.loginFrame, text="fuck_cqooc")

        self.usernameFrame = ttk.Frame(self.loginFrame)
        self.labelUsername = ttk.Label(self.usernameFrame, text="用户名:",width=6)
        self.varUsername = ttk.StringVar(self.usernameFrame)
        self.entryUsername = ttk.Entry(self.usernameFrame, width=200, textvariable=self.varUsername)

        self.passwordFrame = ttk.Frame(self.loginFrame)
        self.labelPassword = ttk.Label(self.passwordFrame, text="密码:",width=6)
        self.varPassword = ttk.StringVar(self.passwordFrame)
        self.entryPassword = ttk.Entry(self.passwordFrame, width=200, textvariable=self.varPassword, show="*")

        self.buttonLogin = ttk.Button(self.loginFrame, text="登录", command=self.login, width=30)
        
        # 提示语部分
        self.labelWelcome.pack(pady=10)
        self.labelWelcome.config(font=('Helvatical bold',15))

        # 用户名模块
        self.labelUsername.pack(side=LEFT, anchor=NE, pady=(10,0), fill=X)
        self.entryUsername.pack(side=LEFT, padx=(10, 0), pady=(10,0), expand=YES, fill=BOTH)
        self.usernameFrame.pack()

        # 密码模块
        self.labelPassword.pack(side=LEFT, anchor=NE, pady=(10,0), fill=X)
        self.entryPassword.pack(side=LEFT, padx=(10, 0), pady=(10,0), expand=YES, fill=BOTH)
        self.passwordFrame.pack()

        # 登录按钮
        self.buttonLogin.pack(pady=(10,0))
        # 整个登录模块
        self.loginFrame.pack()

    def __disposeLoginFrame(self):
        '''清除登录框架'''
        self.loginFrame.destroy()

    def __setupDashboardFrame(self):
        self.welcomeFrame = ttk.Frame(self.root)
        self.contentWrapperFrame = ttk.Frame(self.root)
        self.courseFrame = ttk.Frame(self.contentWrapperFrame)
        self.lessonFrame = ttk.Frame(self.contentWrapperFrame)
        self.actionFrame = ttk.Frame(self.root)

    def login(self):
        '''登录'''
        username = self.varUsername.get()
        password = self.varPassword.get()
        if username == "" or password == "":
            Messagebox.show_error("用户名或密码不能为空。", "错误")
            return

        core = Core(username, password)
        loginResult = core.login()
        
        self.buttonLogin["text"] = "登录"
        if loginResult["status"] == 'ok':
            self.__disposeLoginFrame()
        else:
            Messagebox.show_error("登录失败。\n你需要前往网站手动登录并退出登录，然后再试一次。", "提示")