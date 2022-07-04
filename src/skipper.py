# -*- coding: utf-8 -*-
from hackcqooc.core import Core

import threading
from time import sleep


class skipper(threading.Thread):
    """用于执行跳过课程任务的线程类"""

    def __init__(self, core: Core, sectionList: list) -> None:
        """参数说明：

        *core* 功能内核对象，来自src.core

        *sectionList* 包含课程ID的字符串列表

        """
        threading.Thread.__init__(self)
        self.core = core
        self.sectionList = sectionList
        self.success = 0
        self.fail = 0
        self.current = 1
        self.state = False

    def run(self) -> None:
        print("skip thread started")
        self.skip(self.sectionList)

    def skip(self, sectionList: list) -> None:
        print("skip task started")
        for i in sectionList:
            result = self.core.skip_section(i)
            if result["code"] == 200:
                self.success += 1
            else:
                self.fail += 1
            # 对于任务列表长度为1的情况就没有必要sleep这么久了，只有长度超过1的才要分别sleep 31秒
            if len(sectionList) != 1:
                sleep(31)
            self.current += 1
        # 跳出循环说明任务执行完成，修改状态标志位为True
        self.state = True

    def getState(self) -> bool:
        """返回True说明任务执行完成，False为未完成"""
        return self.state
