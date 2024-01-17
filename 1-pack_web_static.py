#!/usr/bin/python3
""" Generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Create a tar gzipped archive of the directory web_static. """
    local("mkdir -p versions")
    crnt_date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(crnt_date)
    rs = local("tar -cvzf {} web_static".format(file))
    if rs.succeeded:
        return file
    else:
        return None
