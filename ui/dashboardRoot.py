# -*- coding: utf-8 -*-
import sys
import tkinter

from matplotlib.pyplot import text
sys.path.append('..')
from src.core import Core

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from tkinter.ttk import Style

class dashboardRoot(ttk.Window):
    def __init__(self) -> None:
        super().__init__()

        self.core = None

        # 设置基础视图
        self.title("fuck_cqooc")
        self.geometry("800x500")
        self.resizable(False,False)

        # 定义控件
        self.root = ttk.Frame(self,padding=10)
        self.setupLoginFrame()
        # 根
        self.root.pack(fill=X,expand=YES)

    def start(self) -> None:
        '''启动登录界面'''
        self.mainloop()

    def setupLoginFrame(self) -> None:
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
        self.labelWelcome.config(font=('Helvetical bold',15))

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

    def disposeLoginFrame(self) -> None:
        '''清除登录框架'''
        self.loginFrame.destroy()

    def setupDashboardFrame(self) -> None:
        # 定义所有框架
        self.welcomeFrame = ttk.Frame(self.root)
        self.contentWrapperFrame = ttk.Frame(self.root)
        self.courseFrame = ttk.Frame(self.contentWrapperFrame)
        self.lessonFrame = ttk.Frame(self.contentWrapperFrame)
        self.actionFrame = ttk.Frame(self.root)

        # 放置所有框架
        self.welcomeFrame.pack()
        self.contentWrapperFrame.pack()
        self.courseFrame.pack(side=LEFT)
        self.lessonFrame.pack(side=LEFT)
        self.actionFrame.pack()

        # 设置顶部状态提示语
        self.labelWelcome = ttk.Label(self.welcomeFrame,text=f"当前登录用户为{self.varUsername.get()}")
        self.labelWelcome.config(font=('Helvetical bold',15))
        self.labelWelcome.pack(side=LEFT, padx=(20,0),pady=(0,20))

        # 设置课程列表
        self.treeCourse = ttk.Treeview(master=self.courseFrame,columns=[0],show=HEADINGS,height=10)
        self.courseList = self.getCourseDict()['course']
        for i in self.courseList:
            t = (i[0],)
            self.treeCourse.insert("",END,values=t)
        self.treeCourse.heading(0,text="课程名称")
        self.treeCourse.column(0,width=400)
        self.treeCourse.bind('<<TreeviewSelect>>',self.displayLessons)
        self.treeCourse.pack(side=LEFT)

        # 设置任务列表
        self.treeLesson = ttk.Treeview(master=self.lessonFrame,columns=[0,1,2,3],show=HEADINGS,height=10)
        self.treeLesson.insert("",END,values=("☐","点击左侧列表课程来选择","未完成",'1000'))
        self.treeLesson.heading(0,text="勾选")
        self.treeLesson.heading(1,text="任务名称")
        self.treeLesson.heading(2,text="完成情况")
        self.treeLesson.heading(3,text="sectionID")
        self.treeLesson.column(0,width=50)
        self.treeLesson.column(1,width=350)
        self.treeLesson.column(2,width=100)
        self.treeLesson.column(3,width=0)
        self.treeLesson["displaycolumns"] = [0,1,2]
        self.treeLesson.bind('<<TreeviewSelect>>',self.processCheckbox)
        self.treeLesson.pack(side=LEFT)

        # 设置功能按钮
        self.buttonExit = ttk.Button(master=self.actionFrame,text="退出", bootstyle=(INFO, OUTLINE),command=sys.exit,width=10)
        self.buttonSelectAll = ttk.Button(master=self.actionFrame,text="全选", bootstyle=(INFO, OUTLINE),width=10)
        self.buttonProceed = ttk.Button(master=self.actionFrame,text="fuck", bootstyle=SUCCESS,width=10)
        self.buttonSelectAll.bind('<Button-1>',self.selectAll)
        # self.buttonProceed.bind('<Button-1>',self.proceedTask)
        self.buttonExit.pack(side=LEFT,pady=(20,0))
        self.buttonSelectAll.pack(side=LEFT,padx=(400,0),pady=(20,0))
        self.buttonProceed.pack(side=LEFT,padx=(50,0),pady=(20,0))

    def login(self) -> None:
        '''登录'''
        username = self.varUsername.get()
        password = self.varPassword.get()
        if username == "" or password == "":
            Messagebox.show_error("用户名或密码不能为空。", "错误")
            return

        self.core = Core(username, password)
        loginResult = self.core.login()
        
        self.buttonLogin["text"] = "登录"
        if loginResult["status"] == 'ok':
            self.geometry("1000x500")
            self.disposeLoginFrame()
            self.setupDashboardFrame()
        else:
            Messagebox.show_error("登录失败。\n1. 你的用户名或密码可能有误\n2. 你可能需要前往网站手动登录，然后再试一次", "提示")

    def getCourseDict(self) -> dict:
        courseDict = dict()
        courseList = list()
        courseData = self.core.get_course()
        courseDict['count'] = courseData['meta']['total']
        for i in courseData['data']:
            courseList.append((i['title'], i['courseId']))
        courseDict['course'] = courseList
        return courseDict

    def displayLessons(self,e:tkinter.Event) -> None:
        selection = e.widget.item(e.widget.selection()[0])['values']
        for i in self.courseList:
            if i[0] == selection[0]:
                courseID = i[1]
        taskData = self.core.get_course_lessons(course_id=courseID)
        taskList = list()
        for i in taskData['data']:
            if i['category'] not in ['2','3']:# 判断是不是测验
                name = i['title']
                status = "已完成" if i['status'] == 1 else "未完成"
                sectionID = i['sectionId']
                taskList.append(('☐',name,status,sectionID))
        # 清空列表
        for i in self.treeLesson.get_children():
            self.treeLesson.delete(i)
        for i in taskList:
            self.treeLesson.insert("",END,values=i)

    def processCheckbox(self,e:tkinter.Event):
        selection = e.widget.item(e.widget.selection()[0])['values']
        if selection[0] == '☐':
            selection[0] = '☑'
        elif selection[0] == '☑':
            selection[0] = '☐'
        e.widget.item(e.widget.selection()[0],values=tuple(selection))

    def selectAll(self,e:tkinter.Event):
        for i in self.treeLesson.get_children():
            item = self.treeLesson.item(i)["values"]
            if item[0] == '☐':
                item[0] = '☑'
            self.treeLesson.item(i,values=item)

if __name__ == "__main__":
    dashboardRoot().mainloop()