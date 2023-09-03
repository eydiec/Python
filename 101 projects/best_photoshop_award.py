"""
File: best_photoshop_award.py
Name: Eydie Cheng
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.15


def main():
    """
    創作理念：be in the snow
    """
    me = SimpleImage('image_contest/IMG_665.png')
    me.show()

    background = SimpleImage('image_contest/IMG_6660.jpg')
    background.make_as_big_as(me)
    combined_img = combine(background, me)
    combined_img.show()


def combine(background, me):
    """
    : param background: SimpleImage, the background image
    : return me: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for y in range(background.height):
        for x in range(background.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red + pixel_me.blue + pixel_me.green) // 3
            total = pixel_me.red + pixel_me.blue + pixel_me.green
            if pixel_me.green > avg * THRESHOLD and total > 90:
                pixel_background = background.get_pixel(x, y)
                pixel_me.red = pixel_background.red
                pixel_me.blue = pixel_background.blue
                pixel_me.green = pixel_background.green
    return me


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
