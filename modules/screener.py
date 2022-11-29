import mss
import mss.tools
import os
from PIL import Image



def run(**args):
    with mss.mss() as sct:
        # The monitor or screen part to capture
        monitor = sct.monitors[1]  # or a region

        # Grab the data
        sct_img = sct.grab(monitor)
        # Generate the PNG
        png = mss.tools.to_png(sct_img.rgb, sct_img.size)
        with open('screenshot.png', 'wb') as f:
            f.write(png)
        file_in = "screenshot.png"
        img = Image.open(file_in)

        file_out = "screenshot.bmp"
        img.save(file_out)
        # # Save png to file
       
        # # Save png to file
        with open("screenshot.bmp") as image:
            encoded_string = image.read()
        # delete screenshot.PNG
        os.remove('screenshot.bmp')
        return(encoded_string)

