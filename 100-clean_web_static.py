#!/usr/bin/python3
"""Fabric script"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["54.197.107.140", "54.166.14.2"]


def do_clean(number=0):
    """do_clean"""
