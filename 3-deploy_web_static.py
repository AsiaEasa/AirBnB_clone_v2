#!/usr/bin/python3
"""Fabric script"""

from fabric.api import local, env, run, put
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
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

def deploy():
    """Deploys the web_static"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
