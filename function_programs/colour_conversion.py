#Hexadecimal to RBG conversion
def hex_to_RGB(h):
    h = h.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return RGB
def hex_to_BGR(h):
    h = h.lstrip('#')
    BGR = tuple(int(h[i:i+2], 16) for i in (4, 2, 0))
    return BGR


if __name__ == "__main__":
    hex_to_RGB('ffff00')
    hex_to_BGR('ffff00')
