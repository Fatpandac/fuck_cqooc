# -*- coding: utf-8 -*-
from setuptools import setup

APP = ["fuck_cqooc.pyw"]
OPTIONS = {
    "argv_emulation": True,
}

setup(app=APP, options={"py2app": OPTIONS}, setup_requires=["py2app"])
