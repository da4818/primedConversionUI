# primedConversionUI

Our user interface has multiple aims. First, facilitate the operation of the platform. 
It needs to allow the user to turn on the LEDs select the right filter for the operation, 
and take a picture of the sample while the excitation has been performed. 
Once a picture has been taken, the user interface is also used to analyse the image obtained. 
Hence, the user can easily know if the proteins tested are fluorescent, photoconvertible or primed-convertible.

For the interface, we used the Tkinter package (Tk intarface). 
It is built into the Python standard library which makes it easily accessible. 
It works on Windows, MacOS and Linux. It is a powerful, user-friendly and cross-platform, which is why we decided to use this framework.

To make the user interface functional, multiple libaries must be installed:
- Tkinter, to create the user interface.
- Matplotlib, to create visualisations in Python.
- PIL, or Python Imaging Library, to visualise images.
- gpiozero, to allow the program to interact with the RaspberryPi.
- scikit-image, for image processing in Python.
- Servo Motor Library 
- cv2, a Python library used to solve computer image problems.

The user has an option to undergo analysis for primed conversion or photo conversion.
Then they can take an initial photo (a control image - non converted samples).
After taking an initial photo, they can initiate primed/photo conversion, which automatically normalises the photos
and undergoes masking. After analysis is complete, the data will be displayed to the user.
The data will give quantitative values for the pixel (and thus sample well) brightness.


Outline of image analysis:

- Converts the image to greyscale and obtains its grey value (between 0 and 1), which is indicative of the brightness of the pixel

- Produces a histogram of number of pixels in the image that are of a certain brightness is created(there's 256 histogram bins so it essentially looks like a line graph)

- If we can obtain an image of dendra2 with a known fluorescence, we can convert it to the corresponding grey value (will be done using a calibration curve - currently need data to create that) - this will be the standard
- We then set greyscale value thresholds for what we consider to be 'significant' fluorescence - 
these values are then used to mask the image.
Masking consists of recolouring all pixels that are over a certain brightness 
(e.g. all pixels that are brighter than 0.5 can be recoloured as teal).
We can then use arbitrary colours to represent the threshold values 
which we can use to determine the grey value and thus fluorescence of the image (using a calibration curve)

4 outputs will be displayed to the user:
- The original image
- The masked image, recoloured with the corresponding brightness levels (resembling a heatmap)
- The calibration curve 
- The grey value histogram curve

Future amendments:
- Obtaining experimental values for fluorescence using a standard sample (Dendra2)
- Obtaining pixel locations to accurately label well positions
- Plotting/displaying the relative fluorescence of all wells against a standard sample (using the calibration curve)
- Adding user input time for primed/photo conversion duration
- Displaying messages (accurately reflecting the which LEDs and when they are turned on/off)

Other branches may focus on different aspects of the code at varying points in time;
e.g., modulating_functions is used for troubleshooting the component integration between the Raspberry Pi and GUI
by modulating each function



