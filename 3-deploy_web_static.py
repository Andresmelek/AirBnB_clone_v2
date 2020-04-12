#!/usr/bin/python3
"""
Fabric script that generates a .tgz
"""

from datetime import datetime
from fabric.operations import local, put, run
from fabric.api import env
from os import path


env.hosts = ['35.231.144.101', '34.229.74.97']
archive_path = None


def do_pack():
    """ Creats a trgz archive """
    local("mkdir -p versions")
    my_path = local("tar -zcvf versions/web_static_{}.tgz web_static".format(
                        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    my_path_name = "versions/web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))

    if my_path.failed:
        return None
    return my_path_name


def do_deploy(archive_path):
    """ Deploys the file """
    try:
        name = archive_path[9:]
        shortname = archive_path[9:-4]
        put(archive_path, "/tmp/{}".format(name))
        run("sudo mkdir -p /data/web_static/releases/{}/".format(shortname))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(name, shortname))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
                            /data/web_static/releases/{}/"
            .format(shortname, shortname))
        run("sudo rm /tmp/{}".format(name))
        run("sudo rm -fr /data/web_static/current")
        run("sudo rm -fr /data/web_static/releases/{}/web_static"
            .format(shortname))
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(shortname))
        print("New version deployed!")
        return True

    except Exception:
        return False


def deploy():
    """ deploy this """
    global archive_path
    if archive_path is None:
        archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
