#!/usr/bin/python3
"""
creates and distributes an archive to your web servers,
using the function deploy
"""

from fabric.api import *
from datetime import datetime
from os.path import *
env.hosts = ['54.157.135.5', '52.3.220.168']


@runs_once
def do_pack():
    """generates an archive .tgz"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


@task
def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        fileName = archive_path.split("/")[-1]
        no_ext_file = fileName.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext_file))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fileName, path, no_ext_file))
        run('rm /tmp/{}'.format(fileName))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext_file))
        run('rm -rf {}{}/web_static'.format(path, no_ext_file))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext_file))
        print("New version deployed!")
        return True
    except Exception:
        return False


@task
def deploy():
    """creates & distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
