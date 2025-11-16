# libs/rich_presence/__init__.py
#coding:utf-8

import os
import time
from pypresence import Presence

class discord_rpc:

    def __init__(self, client_id = "1391420811402805308"):
        
        self.rpc = Presence(client_id,pipe=0)
        self.connected = False
        self.start_time = int(time.time())

    def connect(self):

        output_discord = os.popen("wmic process get description").read()

        if output_discord.find("Discord.exe") != -1:

            try:
                self.rpc.connect()
                self.connected = True

            except Exception:
                pass

        else:
            pass

    def update_status(self, status):

        if not self.connected:
            return

        try:
            self.rpc.update(details=status, state="Credits : NoNoDu88", large_image="corehalla", start=self.start_time)
            
        except Exception:
            pass

    def disconnect(self):

        if self.connected:

            try:
                self.rpc.close()
                self.connected = False

            except Exception:
                pass