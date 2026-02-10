import tkinter as tk
import time
from PIL import Image, ImageTk

# Main window
root= tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

#List of image paths
image_paths= [  # this all is my projects images of HTML And CSS
    r"C:\Users\vinay\Desktop\Projects\Python Project\Image Slideshow App\img\porjects screenshort.png",
    r"C:\Users\vinay\Desktop\Projects\Python Project\Image Slideshow App\img\Resume.png",
    r"C:\Users\vinay\Desktop\Projects\Python Project\Image Slideshow App\img\Swiggy Menu.png",
    r"C:\Users\vinay\Desktop\Projects\Python Project\Image Slideshow App\img\cafe website 1.png",
    r"C:\Users\vinay\Desktop\Projects\Python Project\Image Slideshow App\img\cafe website 2.png",
    r"C:\Users\vinay\Desktop\Projects\Python Project\Image Slideshow App\img\Card project .png"
]

image_size= (800, 800)
images= []


for path in image_paths:
    print("Opening:", path)
    img = Image.open(path)
    images.append(img)  # Adding each image to the list

# Convert PIL images into Tkinter Compatible Image
final_images= []
for img in images:
    photo= ImageTk.PhotoImage(img)
    final_images.append(photo)

# Label visit to keep photoss
image_label= tk.Label(root)
image_label.pack(pady=30)

# Slideshow function
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image= photo
        root.update()
        time.sleep(1.5)

# Button
play_button= tk.Button(
    root,
    text= "Play the slideshow",
    font=("Arial",18),
    command= start_slideshow
)

play_button.pack(pady=40)

root.mainloop()