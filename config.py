#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6307683228:AAE3fEkS6ElaPFNvJiC0ryj0ujkqFR-3ysY")
    API_ID = int(os.environ.get("API_ID", "27924563"))
    API_HASH = os.environ.get("API_HASH", "9419471d1537a1b2355bca677055cec5")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6511470075")
