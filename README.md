# primedConversionUI

Modulate_functions outline:
This branch is to allow testing and integration of the GUI to individual components.
The programmers can individually test: 
- Taking a before and after photo of the samples (pre and post)
- Executing green or red excitation
- Executing primed or photo conversion
- Displaying image analysis (note that this will only work when the corresponding pre and post photos have been taken)

KEYWORDS/TERMINOLOGY

Each image filename is saved as "type_method_colour_ID.png"
- **type**: An image is either pre/post/norm (normalised)
- **method**: Refers to pc (photo conversion) or pr (primed conversion)
- **colour**: refers to green (pre-conversion) or red (post-conversion) channel 
- **ID**: refers to the sample/test number 

Examples 
* "norm_pc_red_5.png" is the _normalised_ image of _5th photo conversion_ sample test, 
after undergoing photo conversion and exciting with _540nm LED_ 
* "pre_pr_green_1.png" is the raw image of the _1st primed conversion_ sample test,
before undergoing excitation with _494nm LED_ or primed conversion
