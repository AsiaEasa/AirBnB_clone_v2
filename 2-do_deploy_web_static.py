#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
"""
from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ["54.197.107.140", "54.166.14.2"]

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
    except:
        return False
