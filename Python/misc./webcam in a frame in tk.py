import tkinter as tk
import cv2
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Side by Side Frames (Pack)")

   # Create the frame and set its parent to 'root'
vid_frame = tk.Frame(root, bg='lightblue', width=200)
   # Pack the frame to the left side
vid_frame.pack(side = tk.LEFT)

   # Capture video frames
cap = cv2.VideoCapture(0)

def show_frame():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    display1.imgtk = imgtk #Shows frame for display 1
    display1.configure(image=imgtk)
    root.after(10, show_frame) #while loop 

display1 = tk.Label(vid_frame)
display1.pack()  #Display 1

show_frame() #Display

root.mainloop()
