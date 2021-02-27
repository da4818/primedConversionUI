def choose_y(val):
    is_valid = True
    if (val == 1):
        y=[2,4,1]
    elif (val == 2):
        y=[5,1,3]
    elif (val == 3):
        y=[0,2,5]
    else:
        y=[0,0,0]
        is_valid = False
    return y, is_valid