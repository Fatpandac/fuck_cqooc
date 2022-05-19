# -*- coding: utf-8 -*-

import traceback
import ttkbootstrap as ttk


class exceptionHandler(ttk.Toplevel):
    def __init__(self, master, e: Exception) -> None:
        super().__init__()
        self.master = master
        self.exception = e
        self.stacktrace = "".join(traceback.format_tb(e.__traceback__))
        font = ("Consolas", 10, "normal")

        self.title("啊哦，好像出错了")
        self.resizable(False, False)
        # self.geometry("500x600")

        self.label1 = ttk.Label(
            master=self, anchor=ttk.W, font=font, text="程序运行过程中出现了错误，下面是错误信息。"
        )
        self.label2 = ttk.Label(
            master=self,
            anchor=ttk.W,
            font=font,
            text="麻烦你把下列错误信息发送到 github.com/Fatpandac/fuck_cqooc/issues。"
            + "我们很快就会修复的！",
        )
        self.label1.pack(fill=ttk.BOTH, padx=10, pady=(10, 0))
        self.label2.pack(fill=ttk.BOTH, padx=10, pady=(0, 10))

        self.stacktraceText = ttk.Text(master=self, wrap=ttk.WORD)
        self.stacktraceText.insert(
            ttk.END,
            "请将本段信息发送到github.com/Fatpandac/fuck_cqooc/issues，"
            + "使用快捷键Ctrl+A和Ctrl+C复制。\n",
        )
        self.stacktraceText.insert(
            ttk.END, "===============================================\n"
        )
        self.stacktraceText.insert(ttk.END, self.stacktrace)
        self.stacktraceText.config(state=ttk.DISABLED, font=font)
        self.stacktraceText.pack()

    def start(self) -> None:
        self.mainloop()
