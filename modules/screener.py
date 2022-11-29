import mss
import mss.tools
import os
import base64


def run(**args):
    with mss.mss() as sct:
        # The monitor or screen part to capture
        monitor = sct.monitors[1]  # or a region

        # Grab the data
        sct_img = sct.grab(monitor)
        # Generate the PNG
        png = mss.tools.to_png(sct_img.rgb, sct_img.size)
        #
        # # Save png to file
        with open('screenshot.bmp', 'wb') as f:
            f.write(png)
        # # Save png to file
        with open("screenshot.bmp", "rb") as image:
            encoded_string = image.read()
        # delete screenshot.PNG
        os.remove('screenshot.bmp')
        return(encoded_string)

