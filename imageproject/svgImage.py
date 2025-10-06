#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 10:53:39 2025

@author: enzo
"""

from PIL import Image
from math import pi
from math import cos
from math import sin


HEXAGON_SIZE = 20


def pixel_to_hex(x, y) :
    """
    Retrieves the hex associated to pixel x and y.

    Parameters
    ----------
    x : Integer
        The x coordinate of the pixel.
    y : Integer
        The y coordinate of the pixel.

    Returns
    -------
    (Integer, Integer)
    The hex coordinates associated to the pixel

    """
    temp_x = x / HEXAGON_SIZE
    temp_y = y / HEXAGON_SIZE
    
    hexa_x = 2./3 * temp_x
    hexa_y = -1./3 * temp_x + (3**(1/2) / 3 )* temp_y
    return (hexa_x, hexa_y)


def hex_center(hexa_x, hexa_y) :
    """
    Computes the center pixel of a hexagon

    Parameters
    ----------
    hexa_x : Integer
        x coordinates of the hexagon (on the hexagon grid)
    hexa_y: Integer
        y coordinates of the hexagon (on the hexagon grid)

    Returns
    -------
    (Integer, Integer)
    Coordinate of the center pixel of hexa

    """
    x = 3./2 * hexa_x
    y = (3**(1/2))/2 + 3**(1/2) * hexa_y
    
    x = x * HEXAGON_SIZE
    y = y * HEXAGON_SIZE
    return (x, y)


def hex_angles(center_x, center_y) :
    """
    Computes angles coordinates of a hexagon from its center.

    Parameters
    ----------
    center_x : Integer
        x coordinate of the center of the hexagon.
    center_y : Integer
        y coordinate of the center of the hexagon.

    Returns
    -------
    [(Integer, Integer), (Integer, Integer), 6 times in total]
    An array of 6 tuples each one containing coordinates of an angle.

    """
    angles = []
    for i in range(6) :
        angle_deg = 60 * i
        angle_rad = pi/180 * angle_deg
        angles.append((center_x + HEXAGON_SIZE * cos(angle_rad),
                      center_y + HEXAGON_SIZE * sin(angle_rad)))
    return angles


def hexagon_string(angles, color='black') :
    """
    Computes the string associated to hexagon drawing

    Parameters
    ----------
    angles : Array of Floats
        Contains angles of the hexagon
    color : String
        The color to fill the hexagon with

    Returns
    -------
    String
    The string which permits to draw the hexagon

    """
    res = ""
    res += f'\t<polygon fill="{color}" '
    res += f'points="{angles[0][0]} {angles[0][1]},'
    res += f'{angles[1][0]} {angles[1][1]},{angles[2][0]} {angles[2][1]},'
    res += f'{angles[3][0]} {angles[3][1]},{angles[4][0]} {angles[4][1]},'
    res += f'{angles[5][0]} {angles[5][1]}"/>\n'
    return res


# Import the image
image = Image.open("./images/screenshot.jpg")
image_width, image_height = image.size
image_pixels = image.load()


hexa_x, hexa_y = pixel_to_hex(0, 0)
center_x, center_y = hex_center(hexa_x, hexa_y)

"""
hexa_x, hexa_y = pixel_to_hex(30, 30)
center_x, center_y = hex_center(hexa_x, hexa_y)
angles = hex_angles(center_x, center_y)
"""
svg_content = f'<svg width="{image_width}" height="{image_height}">\n'

j = 0
center_y = 0
while center_y < image_height - HEXAGON_SIZE :
    i = 0
    center_x = 0
    while center_x < image_width :
        center_x, center_y = hex_center(i, j)
        angles = hex_angles(center_x, center_y)
        svg_content += hexagon_string(angles, "black")
        i += 2
    j += 1


j = 0
center_y = 0
while center_y < image_height :
    i = 0
    center_x = 0
    while center_x < (image_width - HEXAGON_SIZE*2) :
        center_x, center_y = hex_center(i+1, j-1/2)
        angles = hex_angles(center_x, center_y)
        svg_content += hexagon_string(angles, "white")
        i += 2
    j += 1



svg_content += '</svg>'

with open('output.svg', 'w') as file :
    file.write(svg_content)
