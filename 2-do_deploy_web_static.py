#!/usr/bin/python3
"""Ey que pasa amigos de youtube"""
import os.path
from datetime import datetime
from fabric.operations import local, put, run
from fabric.api import env

env.hosts = ['34.75.39.77', '104.196.25.93']


def do_pack():
    """Make it bro"""
    local('mkdir -p versions')
    catched = local('tar -czvf versions/web_static{}.tgz web_static'
                    .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                    capture=True)
    if catched.failed:
        return None
    return catched


def do_deploy(archive_path):
    """Distribute an archive to the web servers"""
    if os.path.exists(archive_path):
        try:
            name = archive_path.split('/')[1]
            noext = name.split('.')[0]
            folder = '/data/web_static/releases/versions/{}/'.format(noext)
            put(archive_path, '/tmp')
            sudo('mkdir -p {}'.format(folder))
            sudo('tar -xzf /tmp/{} -C {}'.format(name, folder))
            sudo('rm /tmp/{}'.format(name))
            sudo('mv {}/web_static/* {}'.format(folder, folder))
            sudo('rm -rf {}/web_static'.format(folder))
            sudo('rm -rf /data/web_static/current')
            sudo('ln -s /data/web_static/current {}'.format(folder))
            return True
        except Exception as identifier:
            return False

    else:
        return False
