from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk

# initialize window
root = Tk()
root.title("Province Picker")
root.geometry("1280x720")

# create frames
image_frame = Frame(root)
image_frame.pack(side = LEFT)

tools_frame = Frame(root, bg="red")
tools_frame.pack(side = LEFT)

# open file select dialog
filename = fd.askopenfilename()

#load image
canvas = Canvas(image_frame)
canvas.pack()
image = Image.open(filename)
img = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, image=img)
root.update()

# create buttons
#button1 = Button(tools_frame, text="Hello Bruh")
#button1.pack()

root.mainloop()