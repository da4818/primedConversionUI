The general outline of what i'm doing is as follows:

- using image_normalisation.py to normalise/subtract the 'before' image to the 'after' 
and saving a 'normalised' image to the project area
- using  measuring_brightness.py to detect the brightness (and thus fluorescence of the normalised image)

Basically the idea is that converting the image to greyscale and obtaining its grey value (between 0 and 1) is 
indicative of the brightness of the pixel
- It creates a histogram showing the number of pixels in the image that are of a certain brightness 
(there's 256 histogram bins so it essentially looks like a line graph)

If we can obtain an image of dendra2 with a known fluorescence, we can convert it to the
corresponding grey value (using a calibration curve - I need data to create that) - this will be the standard

We then create threshold grey values for efficient fluorescence - these values are then used to mask the image

In terms of masking, it will recolour all parts of the image that are over a certain brightness
(e.g. all pixels that are brighter than 0.5 can be colour in yellow)
We can then use arbitrary colours to represent the threshold values which we can use to determine the 
grey value and thus fluorescence of the image (using a calibration curve)

Eventually on tkinter it will display 3 graphs:
1. The calibration curve
2. The grey value histogram curve
3. The masked image, recoloured with the corresponding brightness levels

I think the limiting factor is having experimental values for fluorescence but I 
will check online for images and use that as a rough estimate

This can still implement the image reading and graphing aspect of skimage_image_analysis branch
but I'm not sure if I've oversimplified the analysis process