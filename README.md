# primedConversionUI

Our user interface has multiple aims. First, facilitate the operation of the platform. It needs to allow the user to turn on the LEDs simply, select the right filter for the operation, and take a picture of the sample while the excitation has been performed. Once a picture has been taken, the user interface is also used to analyse the image obtained. Hence, the user can easily know if the proteins tested are fluorescent, photoconvertible or primed-convertible.

For the interface, we used the Tkinter package (Tk intarface). It is built into the Python standard library which makes it even easier for the user. It can works on Windows, MacOS and Linux. It is powerful, user-friendly and cross-platform, which is why we decided to use this framework.

To make the user interface functional, multiple libaries must be installed:
-Tkinter, to create the user interface.
-Matplotlib, to create visualisations in Python.
-PIL, or Python Imaging Library, to visualise images.
-gpiozero, to allow the program to interact with the RaspberryPi.
-scikit-image, for image processing in Python.
-Servo Motor Library- WHAT IS IIIIIIIIIIIIIIIIIIIIIIT
-cv2, a Python library used to solve computer vision problems.



Using image_normalisation.py to normalise/subtract the 'before' image to the 'after' and saving a 'normalised' image to the project area
Detect the brightness (and thus fluorescence of the normalised image):

-Converts the image to greyscale and obtains its grey value (between 0 and 1), which is indicative of the brightness of the pixel

-A histogram of number of pixels in the image that are of a certain brightness is created(there's 256 histogram bins so it essentially looks like a line graph)

-If we can obtain an image of dendra2 with a known fluorescence, we can convert it to the corresponding grey value (using a calibration curve - currently need data to create that) - this will be the standard

We then set threshold grey values for efficient fluorescence - these values are then used to mask the image
In terms of masking, it will recolour all parts of the image that are over a certain brightness (e.g. all pixels that are brighter than 0.5 can be colour in yellow) We can then use arbitrary colours to represent the threshold values which we can use to determine the grey value and thus fluorescence of the image (using a calibration curve)

Eventually on tkinter it will display 3 graphs:
-The original image

-The masked image, recoloured with the corresponding brightness levels

-The calibration curve

-The grey value histogram curve

Limiting factor is having experimental values for fluorescence but I will check online for images and use that as a rough estimate



