# scan for open ports and return the result
import platform,socket,re,uuid, psutil, base64

def run(**args):
    info = platform.system()
    info += platform.release()
    info += platform.version()
    info += platform.machine()
    info += platform.processor()
    return info
   