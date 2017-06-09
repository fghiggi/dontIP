"""
My personal DDNS (づ｡◕‿‿◕｡)づ
"""

from sys import argv
from requests import get, post

def dothehand(url):
    """
    Find actual IP address and send it to dontpad
    """
    _ip = get("https://ifconfig.co/ip").content

    post(url, {'text': _ip})

if __name__ == "__main__":
    if len(argv) < 2:
        print('URL parameter required')
        exit(0)

    dothehand(argv[1])
