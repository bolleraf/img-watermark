from tkinter import *
from ui.main_window import MainWindow

"""
Image Watermarker Tool

Easy Watermarking tool to add watermark to your JPEG files

Author: Raphael Bolle
Copyright: (2021) Raphael Bolle
"""

root = Tk()
app = MainWindow(root)
root.wm_title("Image Watermarker")
root.mainloop()
