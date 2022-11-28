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
        jpg = mss.tools.to_jpg(sct_img.rgb, sct_img.size)
        #
        # # Save jpg to file
        with open('screenshot.jpg', 'wb') as f:
            f.write(jpg)
        # # Save jpg to file
        with open("screenshot.jpg", "rb") as image:
            encoded_string = image.read()
        # delete screenshot.PNG
        os.remove('screenshot.jpg')
        return(encoded_string)

