#!/usr/bin/python3
"""
Fabric script that generates a .tgz
"""

from fabric.api import local
import datetime


def do_pack():
    """ Creats a trgz archive """
    time = datetime.datetime.now()
    time_format = time.strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}".format(time_format)
    local("mkdir -p versions")
    full_file = local("tar -cvzf versions/{}.tgz web_static".format(file_name))

    if full_file.failed:
        return None
    else:
        return full_file
