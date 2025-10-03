#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 10:53:39 2025

@author: enzo
"""

from PIL import Image

# Import the image
image = Image.open("./images/screenshot.jpg")
image_width, image_height = image.size
image_pixels = image.load()

svg_content = f'<svg width="{image_width}" height="{image_height}">\n'
svg_content += '\t<polygon points="50 3,100 28,100 75,50 100,3 75,3 25"/>\n'
svg_content += '</svg>'

with open('output.svg', 'w') as file :
    file.write(svg_content)