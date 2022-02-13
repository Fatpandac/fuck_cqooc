# -*- coding: utf-8 -*-
from src.core.config import Config


class Core:
    def __init__(self, xsid=None):
        self.__config = Config(xsid)

    def get_headers(self) -> str:
        return self.__config.get_headers()
