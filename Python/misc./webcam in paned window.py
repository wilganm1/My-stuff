import tkinter as tk
import cv2
from tkinter import ttk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("PanedWindow Demo")

# Create a horizontal PanedWindow
# The ttk version is recommended
pw = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=True)


# Create child frames (panes)

vid_frame = ttk.Frame(pw, width=200, height=300, relief=tk.SUNKEN)
   # Pack the frame to the left side

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


right_frame = ttk.Frame(pw, width=400, height=300, relief=tk.SUNKEN)

# Add some content to the frames (optional, but shows the panes)
tk.Label(vid_frame, text="Left Pane").pack(pady=10)
tk.Label(right_frame, text="Right Pane").pack(pady=10)

# Add the frames to the PanedWindow using the .add() method
# Note: Do not use .grid() or .pack() on the child frames *after* adding them to the PanedWindow
pw.add(vid_frame, weight=1) # The weight option gives this pane a relative resizing priority
pw.add(right_frame, weight=2)

# Start the Tkinter event loop
root.mainloop()
