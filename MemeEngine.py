"""Responsible for manipulating and drawing text onto images."""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random


class MemeEngine():
    """Create MemeEngine object to manipulate and draw text onto images.

    This class is constructed using the static folder path where the
    manipulated images are saved. It implements the make_meme method with the
    following input arguments:
        - the original image path,
        - text and author which needs to be drawn on it and
        - width to which the image needs to be manipulated

    Returns the path of the manipulated image in the static folder.

    Invoked by meme.py and app.py
    """

    def __init__(self, path_static):
        self.path_static = path_static

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Manipulate and draw text onto images."""
        with Image.open(img_path) as im:
            if width > 500:
                raise ValueError('Width of the manipulated image should not '
                                 'exceed 500px.')
            original_width, original_height = im.size
            aspect_ratio = original_width // original_height
            height = width * aspect_ratio
            im = im.resize((width, height))

            draw = ImageDraw.Draw(im)
            img_fraction = 0.06
            font_size = int(np.ceil(im.width * img_fraction))
            font = ImageFont.truetype('./font/LilitaOne-Regular.ttf',
                                      size=font_size)
            message = f'{text} \n - {author}'
            text_position = random.choice(range(30, height - 100))
            draw.text((30, text_position), message, font=font, fill='white')

            img_name = img_path.split('/')[-1]
            # img_name = img_name.split('.')
            # img_name = img_name[0] + '_' + \
            #     str(random.choice(range(0,100000))) + '.' + img_name[-1]
            path_img_out = f'{self.path_static}/{img_name}'
            im.save(path_img_out)

            return path_img_out  # img_out is the path to the manipulated image
