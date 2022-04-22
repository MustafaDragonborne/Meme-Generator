# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 00:43:10 2022

@author: MARS
"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random

class MemeEngine():
    
    def __init__(self, path_tmp):
        self.path_tmp = path_tmp  # what should be the path here??
    
    
    def make_meme(self, img_path, text, author, width=500) -> str:        
        with Image.open(img_path) as im:                        
            if width>500:
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
            path_img_out = f'{self.path_tmp}/{img_name}'
            im.save(path_img_out)
            return path_img_out  # img_out is the path to the manipulated image
