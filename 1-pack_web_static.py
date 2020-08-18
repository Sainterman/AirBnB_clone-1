#!/usr/bin/python3
"""Ey que pasa amigos de youtube"""
from datetime import datetime
from fabric.operations import local


def do_pack():
    """Make it bro"""
    local('mkdir -p versions')
    catched = local('tar -czvf versions/web_static{}.tar.gz web_static'
                    .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                    capture=True)
    if catched.failed:
        return None
    return catched
