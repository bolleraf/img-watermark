import sys
from tkinter import *
from tkinter import filedialog as fd

from utils.image_processing import watermark


def quit_application():
    """
    Quit application
    :return: nothing
    """
    sys.exit()


class MainWindow(Frame):
    """
    Main window that allows to setup the parameters of watermarking process

    """
    def __init__(self, master=None):
        """
        Constructor. Define all widgets and setup the layout of the form

        :param master:
        """

        Frame.__init__(self, master)
        self.master = master
        self.grid(padx=10, pady=10)

        self.align_v = IntVar()
        self.align_h = IntVar()
        self.fontsize = StringVar(value=36)

        # Setup widgets
        self.lbl_source = Label(self, text="Source file :", justify=LEFT)
        self.lbl_source.grid(sticky=W, row=1, column=0, padx=5)
        self.edit_source = Entry(self, width=50)
        self.edit_source.grid(row=1, column=1, padx=5, sticky=W)
        self.btn_select_source = Button(self, text="Select file ...", command=self.select_source)
        self.btn_select_source.grid(row=1, column=2, padx=5, sticky=W)
        self.lbl_destination_folder = Label(self, text="Destination folder :", justify=LEFT)
        self.lbl_destination_folder.grid(sticky=W, row=2, column=0, padx=5)
        self.edit_destination = Entry(self, width=50)
        self.edit_destination.grid(row=2, column=1, padx=5, sticky=W)
        self.btn_select_destination = Button(self, text="Select folder...",
                                             command=self.select_destination)
        self.btn_select_destination.grid(row=2, column=2, padx=5, sticky=W)
        self.lbl_watermark = Label(self, text="Watermark options", font=("Arial", 14))
        self.lbl_watermark.grid(row=3, column=0, padx=5, pady=10)

        self.lbl_wmk_text = Label(self, text="Text :", justify=LEFT)
        self.lbl_wmk_text.grid(row=4, column=0, padx=5, sticky=W)
        self.edit_wmk_text = Entry(self, width=50)
        self.edit_wmk_text.grid(row=4, column=1, padx=5, sticky=E)

        self.align_v.set(3)
        self.align_h.set(3)
        frame_vert_align = LabelFrame(self, text="Vertical alignment")
        frame_vert_align.grid(row=5, column=0, padx=5)
        Radiobutton(frame_vert_align, text="Top", variable=self.align_v, value=1,command=self.get_vertical_align
                    ).pack(anchor=W)
        Radiobutton(frame_vert_align, text="Center", variable=self.align_v, value=2, command=self.get_vertical_align
                    ).pack(
            anchor=W)
        Radiobutton(frame_vert_align, text="Bottom", variable=self.align_v, value=3, command=self.get_vertical_align
                    ).pack(anchor=W)

        frame_horiz_align = LabelFrame(self, text="Horizontal alignment")
        frame_horiz_align.grid(row=5, column=1, padx=5)
        Radiobutton(frame_horiz_align, text="Left", variable=self.align_h, value=1, command=self.get_vertical_align
                    ).pack(anchor=W)
        Radiobutton(frame_horiz_align, text="Center", variable=self.align_h, value=2,
                    command=self.get_vertical_align).pack(anchor=W)
        Radiobutton(frame_horiz_align, text="Right", variable=self.align_h, value=3,
                    command=self.get_vertical_align).pack(anchor=W)
        lbl_fontsize = Label(self, text="Font size :", justify=LEFT)
        lbl_fontsize.grid(row=6, column=0, padx=5, sticky=E)
        self.spin_fontsize = Spinbox(self, from_=0, to=200, textvariable=self.fontsize)
        self.spin_fontsize.grid(row=6, column=1, padx=5, sticky=W)

        self.btn_Process = Button(self, text="Process", command=self.process_watermark)
        self.btn_Process.grid(row=10, column=0, pady=10)
        self.btn_exit = Button(self, text="Quit", command=quit_application)
        self.btn_exit.grid(row=10, column=1, pady=10)

    def process_watermark(self):
        """
        process_watermark is a wrapper method that collects the required parameters end call the watermark
        function from the utils library.

        :return: nothing
        """
        source = self.edit_source.get()
        destination = self.edit_destination.get()
        text = self.edit_wmk_text.get()
        watermark(source=source, destination=destination, text=text,
                  h_align=self.get_horizontal_align(), v_align=self.get_vertical_align(),
                  fontsize=int(self.fontsize.get()))

    def select_source(self):
        """
        Display a FileDialog to select the source image file

        :return: nothing
        """
        selected_file = fd.askopenfilename(title="Select the image file to watermark",
                                           initialdir="/",
                                           filetypes=(("JPEG files", "*.jpg"),
                                                      ("All files", "*.*")))

        if len(selected_file) > 0:
            # A file has been selected

            # Delete content from the source file field
            self.edit_source.delete(0, END)

            # Update the source file field with the new selected file
            self.edit_source.insert(0, selected_file)

    def select_destination(self):
        """
        Display a FileDialog box to select the destination folder
        :return: nothing
        """
        destination_path = fd.askdirectory(title="Select destination folder")

        if len(destination_path) > 0:
            # A directory has been selected

            # Delete content from the destination path field
            self.edit_destination.delete(0, END)

            # Update the destination path field with the selected path
            self.edit_destination.insert(0, destination_path)

    def get_vertical_align(self):
        """
        Get the selected vertical alignment value from the radio buttons and returns the alignment value
        :return: alignment value (top, center, bottom)
        """
        choice = self.align_v.get()
        if choice == 1:
            return "top"
        elif choice == 2:
            return "center"
        elif choice == 3:
            return "bottom"

    def get_horizontal_align(self):
        """
         Get the selected horizontal alignment value from the radio buttons and returns the alignment value
        :return: alignment value (left, center, right)
        """
        choice = self.align_h.get()
        if choice == 1:
            return "left"
        elif choice == 2:
            return "center"
        elif choice == 3:
            return "right"
