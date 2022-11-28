import mss
import mss.tools


with mss.mss() as sct:
    # The monitor or screen part to capture
    monitor = sct.monitors[1]  # or a region

    # Grab the data
    sct_img = sct.grab(monitor)

    # Generate the PNG
    png = mss.tools.to_png(sct_img.rgb, sct_img.size)
    # open image
    with open('screenshot.png', 'wb') as f:
        f.write(png)
        

    # Save to the picture file
    print(sct_img)