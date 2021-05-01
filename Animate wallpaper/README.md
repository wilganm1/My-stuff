## Wallpaper animator
### !!!  This was done on Windows 10 with Python 3.8. I do not know if it will work on earlier versions of Windows or Python !!!

This code will allow your desktop wallpaper(s) to be an animation of images, whether they be separate images or frames from a gif. This is a very rudimentary project, but it is a start. I will walk you through what I did in this document, so you know the exact process.

As always, start a new project in Python. If you are going to use split images from a gif I highly recommend creating a subfolder for each gif.

   Example: Project folder 
              -pics
               -gif 1
              
First, you must choose which images you want to cycle through, or in my case, choose a gif found on the internet that you can split into images to use. If you want a gif, right click it and select "copy image link" Here is the website I used to split gifs into separate imgages: https://ezgif.com/split. I recommend you use gifs that perfectly cycle through with no jarring cuts in them. You can edit each frame in different ways like changing the size, brightness, etc. Make sure you know what the dimensions of your wallpaper is.

**Save as png file in the dropdown window, then hit the "Split to frames!" button. On the next page, download as zip, then extract them to the folder you created.** 

Second, you will have to rename the first 10 images to make the code work. When you download the images, they should look like this:
  frame_00_delay-0.03s.png
  frame_01_delay-0.03s.png
  frame_02_delay-0.03s.png
        .......
  frame_09_delay-0.03s.png
  
 You will have to delete the first 0 in the name. Just rename the file without it.
     frame_0_delay-0.03s.png
     frame_1_delay-0.03s.png,  etc.
     
 Alright, you have everything you need, now just input the code. You will need the get the path for the folder.
 
 ### Making it an exe file
 Watch this YouTube video for a tutorial to convert a Python script into an exe file: https://www.youtube.com/watch?v=UZX5kH72Yx4. 
