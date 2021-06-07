import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME , CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events , errors , custom
import io
from platform import python_version , uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None :
    ALIVE_PIC = "https://telegra.ph/file/feadbe63818bc695c0417.jpg" # we will change this later

DEFAULTUSER = str ( ALIVE_NAME ) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
ALIVE_MESSAGE = "**🔱Venom Zinda Tha....Zinda Hai....Aur Zinda Rahega🔱 \n\n\n**"
ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
ALIVE_MESSAGE += f"`Kernel Type: Monolithic(linux) \n\n`"
ALIVE_MESSAGE += f"`Kernel: 2.2.9  \n\n`"
ALIVE_MESSAGE += f"`KDE: 1.1(Red Hat)  \n\n`"
ALIVE_MESSAGE += "`Default User Interface: KDE Plasma \n\n`"
ALIVE_MESSAGE += f"`Support Channel` : @Raganork_Official \n\n"
if ALIVE_MESSAGE is None :
    ALIVE_MESSAGE = "**🔱Venom Zinda Tha....Zinda Hai....Aur Zinda Rahega🔱 \n\n\n**"
    ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
    ALIVE_MESSAGE += f"`Kernel Type: Monolithic(linux) \n\n`"
    ALIVE_MESSAGE += f"`Kernel: 2.2.9  \n\n`"
    ALIVE_MESSAGE += f"`KDE: 1.1(Red Hat)  \n\n`"
    ALIVE_MESSAGE += "`Default User Interface: KDE Plasma \n\n`"
    ALIVE_MESSAGE += f"`Support Channel` : @Raganork_Official \n\n"
    ALIVE_MESSAGE += f"`ᎷᎽ ᏰᏫᏕᏕ`: {DEFAULTUSER} \n\n "


# @command(outgoing=True, pattern="^.awake$")
@borg.on ( admin_cmd ( pattern=r"awake" ) )
async def amireallyalive ( awake ) :
    """ For .awake command, check if the bot is running.  """
    await awake.delete ()
    await borg.send_file ( awake.chat_id , ALIVE_PIC , caption=ALIVE_MESSAGE )
