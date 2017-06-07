"""
My personal DDNS (づ｡◕‿‿◕｡)づ
"""

from requests import get, post

def dothehand():
    """
    Find actual IP address and send it to dontpad
    """
    _ip = get("https://ifconfig.co/ip").content

    post("http://dontpad.com/ipghiggi", {'text': _ip})

if __name__ == "__main__":
    dothehand()
