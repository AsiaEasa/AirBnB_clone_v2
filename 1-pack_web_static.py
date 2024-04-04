#!/usr/bin/python3
"""generates a .tgz archive"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """Function do pack"""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    N = datetime.now()
    F = (
        f"versions/web_static_{N.strftime('%Y%m%d_%H%M%S')}"
        + ".tgz"
    )
    local(f"tar -cvzf {F} web_static")

    if os.path.exists(F):
        return F
    else:
        return None
