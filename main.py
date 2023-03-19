import tkinter.filedialog
import time
import os
from image_capture import *

# create folder directory to save images
folder = r"\images"
cwd = os.getcwd()
path = cwd + folder
if not os.path.exists(path):
    os.makedirs(path)

# create a dictionary for the filters
fil = ['color', 'gray', 'threshold', 'increaseContrast', 'decreaseContrast', 'logTransformation', 'powerLowEnhancement',
       'negativeEnhancement', 'gauss', 'sobel', 'laplace', 'min', 'max', 'median', 'average', 'unsharp', 'prewitt',
       'histogramEqualization']
filter_dic = {}


def select_filter(filter, status):
    # change required filter to true
    filter_dic = {x: False for x in fil}  # change all values to false in dictionary to make only filter to true
    if filter in filter_dic:
        assert type(status) == bool
        filter_dic[filter] = status
    return filter_dic


class App:
    isImageInstantiated = False

    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Labels
        label1 = tkinter.Label(window, text="Filters")
        label1.grid(row=3, column=13, columnspan=5)

        self.canvas = tkinter.Canvas(self.window, width=300, height=300)
        self.canvas.grid(row=0, column=1, rowspan=15, columnspan=5)

        # button of choose
        self.b_snap = tkinter.Button(window, text="Choose an image", command=self.select_image)
        self.b_snap.grid(row=3, column=3)

        # Button for applying the other filters!
        self.b1 = tkinter.Button(window, text="Increase Contrast", width=15, command=self.increaseContrast_filter)
        self.b1.grid(row=4, column=13)

        self.b2 = tkinter.Button(window, text="Decrease Contrast", width=15, command=self.decreaseContrast_filter)
        self.b2.grid(row=4, column=17)

        self.b3 = tkinter.Button(window, text="Gauss", width=15, command=self.gauss_filter)
        self.b3.grid(row=5, column=13)

        self.b4 = tkinter.Button(window, text="Laplace", width=15, command=self.laplace_filter)
        self.b4.grid(row=5, column=17)

        self.b5 = tkinter.Button(window, text="Threshold", width=15, command=self.threshold_filter)
        self.b5.grid(row=6, column=17)

        # note, add sobel filters to the same button, multiple clicks
        self.b6 = tkinter.Button(window, text="Sobel", width=15, command=self.sobel_filter)
        self.b6.grid(row=6, column=13)

        self.b7 = tkinter.Button(window, text="Gray", width=15, command=self.gray_filter)
        self.b7.grid(row=8, column=13)

        self.b8 = tkinter.Button(window, text="Median", width=15, command=self.median_filter)
        self.b8.grid(row=8, column=17)

        self.b9 = tkinter.Button(window, text="Average", width=15, command=self.average_filter)
        self.b9.grid(row=9, column=13)

        self.b10 = tkinter.Button(window, text="Color/No Filter", width=15, command=self.no_filter)
        self.b10.grid(row=9, column=17)

        self.b11 = tkinter.Button(window, text="Unsharp", width=15, command=self.unsharp_filter)
        self.b11.grid(row=13, column=13)

        self.b12 = tkinter.Button(window, text="LogTrans...", width=15, command=self.logTransformation)
        self.b12.grid(row=10, column=17)

        self.b13 = tkinter.Button(window, text="NegativeEnhanc...", width=15, command=self.negativeEnhancement)
        self.b13.grid(row=11, column=13)

        self.b14 = tkinter.Button(window, text="Min filter", width=15, command=self.min_filter)
        self.b14.grid(row=12, column=13)

        self.b15 = tkinter.Button(window, text="Max filter", width=15, command=self.max_filter)
        self.b15.grid(row=12, column=17)

        self.b16 = tkinter.Button(window, text="Prewitt", width=15, command=self.prewitt_filter)
        self.b16.grid(row=11, column=17)

        self.b17 = tkinter.Button(window, text="Histogram Equaliz...", width=15, command=self.histogram_filter)
        self.b17.grid(row=13, column=17, columnspan=2)

        self.b18 = tkinter.Button(window, text="Power Low 0.5g", width=15, command=self.powerLowEnhancement)
        self.b18.grid(row=10, column=13, columnspan=2)

        self.b19 = tkinter.Button(window, text="Save image", width=15, command=self.save_image)
        self.b19.grid(row=15, rowspan=2, column=13, columnspan=4)

        self.b20 = tkinter.Button(window, text="Close Program", command=window.destroy)
        self.b20.grid(row=15, rowspan=2, column=17, columnspan=2)

        # After	it is called once, the update method will be automatically called every loop
        self.delay = 15
        self.window.tk.call('wm', 'iconphoto', self.window._w, tkinter.PhotoImage(file='icon.png'))
        self.window.mainloop()

    def select_image(self):
        # create instance from image capture
        self.img = ImageCap()
        self.img.all_filters = select_filter('color', True)
        self.img.update()
        self.isImageInstantiated = True

    def save_image(self):
        if self.isImageInstantiated:
            cv2.imwrite(path + r"\image-" + time.strftime("%d-%m-%Y-%H-%M-%S") + '.jpg', self.img.filtered_image)
            print('Image saved!')

    # all filters
    def gray_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('gray', True)
            self.img.update()

    def gauss_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('gauss', True)
            self.img.update()
        
    def laplace_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('laplace', True)
            self.img.update()

    def threshold_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('threshold', True)
            self.img.update()

    def sobel_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('sobel', True)
            self.img.update()
    
    def no_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('color', True)
            self.img.update()

    def median_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('median', True)
            self.img.update()
        
    def average_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('average', True)
            self.img.update()

    def unsharp_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('unsharp', True)
            self.img.update()
    
    def logTransformation(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('logTransformation', True)
            self.img.update()
        
    def negativeEnhancement(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('negativeEnhancement', True)
            self.img.update()

    def powerLowEnhancement(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('powerLowEnhancement', True)
            self.img.update()

    def increaseContrast_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('increaseContrast', True)
            self.img.update()
    
    def decreaseContrast_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('decreaseContrast', True)
            self.img.update()

    def decreaseContrast_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('decreaseContrast', True)
            self.img.update()

    def min_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('min', True)
            self.img.update()

    def max_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('max', True)
            self.img.update()

    def prewitt_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('prewitt', True)
            self.img.update()

    def histogram_filter(self):
        if self.isImageInstantiated:
            self.img.all_filters = select_filter('histogramEqualization', True)
            self.img.update()


# Create a window and pass it to the Application object
App(tkinter.Tk(), 'Tkinter OpenCV')
