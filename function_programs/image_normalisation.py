# We will use this python script to perform image normalisation and return the image to other functions
def normalise_image(pre, post):
    pre = pre.convert("RGB")
    norm = post.convert("RGB")
    width, height = norm.size

    for x in range(width):
        for y in range(height):
            old_R, old_G, old_B = norm.getpixel((x, y))
            R, G, B = pre.getpixel((x, y))
            norm.putpixel((x, y), (old_R-R, old_B-B, old_G-G))

    return norm
