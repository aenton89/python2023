import tkinter as tk
# pip install Pillow
from PIL import Image, ImageTk
import random

def roll_dice():
    # losowanie
    dice_number = random.randint(1, 6)
    
    # label z obrazkiem wylosowanej kostki
    image_path = f"dice{dice_number}.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize((200, 200), Image.AFFINE)
    photo = ImageTk.PhotoImage(resized_image)
    label.config(image=photo)
    label.image = photo

# okno
window = tk.Tk()
window.title("Dice Roll Simulator")
window.geometry("300x400")

# label obrazka
label = tk.Label(window)
label.pack(side=tk.TOP, pady=(50, 0))

# przycisk
button = tk.Button(window, text="roll dice", font=("Times New Roman", 16), command=roll_dice)
button.pack(side=tk.BOTTOM, pady=(50, 50))

# uruchomienie okna
window.mainloop()