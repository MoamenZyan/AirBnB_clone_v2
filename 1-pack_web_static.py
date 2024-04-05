#!/usr/bin/python3
"""Script to make tgz archive"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """making archive file on web_static"""

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
