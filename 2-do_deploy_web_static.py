#!/usr/bin/python3
""" module deployment updates"""
import os.path
from fabric.api import *
from fabric.operations import run, local, put, sudo
from datetime import datetime
import time

env.user = 'ubuntu'
env.hosts = ['35.229.55.69', '34.75.105.128']


def do_deploy(archive_path):
    """deploy and transfers files
    """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        archive_file = archive_path.split("/")[-1]
        # divide the path and get the name of the file
        put(archive_path, "/tmp/")
        # Remove the extension to the archive
        folfer_file = ("/data/web_static/releases/" +
                       archive_file.split(".")[0])
        # create the folder for the archive
        sudo("mkdir -p {:s}".format(folder_file))
        # Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
        sudo("tar -xzf /tmp/{:s} -C {:s}".format(archive_file, folder_file))
        # delete the archive from the web server in tmp
        sudo("rm /tmp/{:s}".format(archive_file))
        # move all files
        sudo("mv {:s}/web_static/* {:s}/".format(folder_file, folder_file))
        # delete
        sudo("rm -rf {:s}/web_static".format(folder_file))
        # delete simbolic link
        sudo("rm -rf /data/web_static/current")
        # create simbolic link
        sudo("ln -s {:s} /data/web_static/current".format(folder_file))
        print("New version deployed")
        return True
    except:
        return False
