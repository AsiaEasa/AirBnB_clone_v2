#!/usr/bin/python3
"""Fabric script"""

from fabric.api import *
import os
from datetime import datetime
env.hosts = ["54.197.107.140", "54.166.14.2"]


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


def do_deploy(archive_path):
    """Distributes an archive"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        AF = os.path.basename(archive_path)
        AN = os.path.splitext(AF)[0]
        AP = f"/data/web_static/releases/{AN}"
        run(f"mkdir -p {AP}")
        run(f"tar -xzf /tmp/{AF} -C {AP}")
        run(f"rm /tmp/{AF}")
        run(f"mv {AP}/web_static/* {AP}")
        run(f"rm -rf {AP}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {AP} /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception as e:
        return False


def deploy():
    """Deploys the web_static"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
