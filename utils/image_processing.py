import pathlib
from pathlib import PurePath

from PIL import Image, ImageDraw, ImageFont

"""
Image Processing module contains the processing utilities

Author: Raphael Bolle
Copyright: (2021) Raphael Bolle

"""


def watermark(source, destination, text, margin=10, h_align="right", v_align="bottom", fontsize=36):
    """
    watermark embeds a text into the source image and save it on the destination folder

    :param fontsize: font size in px
    :param v_align: vertical alignment ("top" / "center" / "bottom")
    :param h_align: horizontal alignment ("left" / "center" / "right")
    :param source: complete path to source file
    :param destination: complete path to the destination folder
    :param text: text to embed on the image as watermarked
    :param margin: margin in pixels. Default margin is 10px
    :return: nothing
    """
    source_img = source
    destination_folder = destination
    p = PurePath(source_img)
    original_filename = p.parts[-1]
    watermark_filename = "W_" + original_filename

    img = Image.open(source_img)
    width, height = img.size

    draw = ImageDraw.Draw(img)
    text = text

    font = ImageFont.truetype('arial.ttf', fontsize)
    text_width, text_height = draw.textsize(text, font)

    x = y = 0

    if h_align == "left":
        x = 0 + margin
    elif h_align == "right":
        x = width - text_width - margin
    elif h_align == "center":
        x = (width - text_width - margin) / 2

    if v_align == "top":
        y = 0 + margin
    elif v_align == "center":
        y = (height - text_height - margin) / 2
    elif v_align == "bottom":
        y = height - text_height - margin

    draw.text((x, y), text, font=font)

    img.save(pathlib.Path(destination_folder) / watermark_filename)
