# Project to color the Record of Ragnarok manga

There is a manga that I'm a fan of called Record of Ragnarok (Shūmatsu no Walküre (終末のワルキューレ, Shūmatsu no Warukyūre, lit. "Valkyrie of the End") that I want
to try something with. I want to write a script that will scan images of characters, recognize them, and color them in with colors from offical sources. I can use OpenCV to do most of this. Since this is a manga all the images are in black & white, so that makes it easier. What I will do is have Python extract the grayscale values of every pixel for each image, and save them for later. I will do the same for the reference colored image I'm using. I can get the all the unique colors too in a list so I know exactly what color values are in the images.  This project will be mostly about object detection though. I can either use LabelImg on my computer or use Roboflow to annotate images. If I use Roboflow I can use their Yolov5/4 Google Colab notebook with their code to train models to recognize characters. Since this is a manga and the design, shape, angle of the characters can alter slightly I will probably get hyper-specific when annotating characters. I'm talking about labeling their left and right arm, their head and roso, etc. Colorization of black-and-white images has already been tried: https://www.pyimagesearch.com/2019/02/25/black-and-white-image-colorization-with-opencv-and-deep-learning/, https://techvidvan.com/tutorials/deep-learning-project-colorize-black-white-images-with-python/, https://github.com/PySimpleGUI/PySimpleGUI-Photo-Colorizer/blob/master/PySimpleGUI_Colorizer.py.

This is just a fun project I want to try out. But if it works it will give me experience using openCV and object detection. I can use Roboflow or install my own Tensorflow object detection program and use that.
