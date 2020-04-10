#!/usr/bin/python3
"""
Fabric script that generates a .tgz
"""

from datetime import datetime
from fabric.operations import local, put, run
from fabric.api import env
from os import path

env.hosts = ['35.231.144.101', '34.229.74.97']


def do_pack():
    """ Creats a trgz archive """
    time = datetime.now()
    time_format = time.strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}".format(time_format)
    local("mkdir -p versions")
    full_file = local("tar -cvzf versions/{}.tgz web_static".format(file_name))

    if full_file.failed:
        return None
    else:
        return full_file


def do_deploy(archive_path):
    """ Deploys the file """
    if not path.exists(archive_path):
        return False

    try:
        name = archive_path[9:]
        shortname = archive_path[9:-4]
        put(archive_path, "/tmp/{}".format(name))
        run("mkdir -p /data/web_static/releases/{}/".format(shortname))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(name, shortname))
        run("mv /data/web_static/releases/{}/web_static/*\
                            /data/web_static/releases/{}/"
            .format(shortname, shortname))
        run("rm /tmp/{}".format(name))
        run("rm -fr /data/web_static/current")
        run("rm -fr /data/web_static/releases/{}/web_static"
            .format(shortname))
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(shortname))
        print("New version deployed!")

    except Exception:
        return False


def deploy():
    """ deploy this """

    path = do_pack()

    if path is None:
        return False

    return do_deploy(path)
