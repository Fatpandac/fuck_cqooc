# -*- coding: utf-8 -*-
from src.core.core import Core

import os
import pytest


ROOT_PATH = os.path.dirname(os.path.dirname(__file__))


def test_core_init():
    xsid = "abcd"
    xsid_file_path = f"{ROOT_PATH}/cookies.txt"

    with pytest.raises(Exception) as e:
        Core()
    exec_msg = e.value.args[0]
    assert exec_msg == "No XSID found"

    core = Core(xsid)
    assert os.path.exists(xsid_file_path)
    assert core.get_xsid() == xsid

    core_without_xsid = Core()
    assert core_without_xsid.get_xsid() == xsid
    os.remove(xsid_file_path)
