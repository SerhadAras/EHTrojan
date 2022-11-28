import mss
import mss.tools

def run(**args):
    with mss.mss() as sct:
        # The monitor or screen part to capture
        monitor = sct.monitors[1]  # or a region

        # Grab the data
        sct_img = sct.grab(monitor)

        # Generate the PNG
        png = mss.tools.to_png(sct_img.rgb, sct_img.size)
    return(sct_img)
