# -*- coding: utf-8 -*-
from src.core.core import Core

import os
import pytest


ROOT_PATH = os.path.dirname(os.path.dirname(__file__))


def test_core_init():
    xsid = "abcd"
    ua = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
        + "/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    )
    xsid_file_path = f"{ROOT_PATH}/cookies.txt"

    try:
        with pytest.raises(Exception) as e:
            Core()
        exec_msg = e.value.args[0]
        assert exec_msg == "No XSID found"

        core = Core(xsid)
        assert os.path.exists(xsid_file_path)
        assert core.get_headers()["Cookie"] == f"xsid={xsid};"
        assert core.get_headers()["User-Agent"] == ua

        core_without_xsid = Core()
        assert core_without_xsid.get_headers()["Cookie"] == f"xsid={xsid};"
    finally:
        os.remove(xsid_file_path)
