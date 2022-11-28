import mss
import mss.tools
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
        png.save("screenshot.png")

        # Save png to file
        with open('screenshot.png', 'rb') as f:
            encoded_string = base64.b64encode(f.read())
            return encoded_string
