from tkinter import *
import numpy as np
from PIL import Image, ImageOps, ImageGrab
import tensorflow as tf

root = Tk()
root.title("Paint App")
root.geometry("800x500")  # Adjusted size for better visibility

# -------------- variables --------------------
stroke_size = IntVar()
stroke_size.set(1)

stroke_color = StringVar()
stroke_color.set("white")

# variables for pencil 
prevPoint = [0,0]
currentPoint = [0,0] 

# Load the model once
model = tf.keras.models.load_model("./model.keras")

# --------------------- functions -------------------------

def usePencil():
    stroke_color.set("white")
    canvas["cursor"] = "arrow"

def useEraser():
    stroke_color.set("white")
    canvas["cursor"] = DOTBOX

def paint(event):
    global prevPoint
    global currentPoint
    x = event.x
    y = event.y
    currentPoint = [x,y]

    if prevPoint != [0,0]: 
        canvas.create_line(prevPoint[0], prevPoint[1], currentPoint[0], currentPoint[1], fill=stroke_color.get(), width=10)

    prevPoint = currentPoint

    if event.type == "5":
        prevPoint = [0,0]

    update_predictions()

def clear():
    canvas.delete('all')
    predictions_label.config(text="Predictions: ")

def update_predictions():
    # Capture the canvas as an image
    x = root.winfo_rootx() + canvas.winfo_x() + 400
    y = root.winfo_rooty() + canvas.winfo_y() + 210
    x1 = x + canvas.winfo_width() + 100
    y1 = y + canvas.winfo_height()

    img = ImageGrab.grab(bbox=(x, y, x1, y1))
    img = img.crop((0, 0, 200, 200))

    # Convert to grayscale and resize
    img = ImageOps.grayscale(img)
    img = img.resize((28, 28))

    # Convert to numpy array
    img_array = np.array(img).reshape(1, 784) / 255
    predictions = model.predict(img_array)
    
    # Get top 5 predictions
    top_5_indices = np.argsort(predictions[0])[-5:][::-1]
    top_5_values = predictions[0][top_5_indices]

    # Prepare prediction text
    pred_text = "Predictions:\n"
    for i in range(5):
        label = names.get(top_5_indices[i], "Unknown")
        percentage = top_5_values[i] * 100
        pred_text += f"{label}: {percentage:.2f}%\n"

    # Update label
    predictions_label.config(text=pred_text)


# ------------------- User Interface -------------------

# Frame - 1 : Tools 
frame1 = Frame(root, height=100, width=800, bg="#2F6690")
frame1.pack(padx=10, pady=10, fill=X)

# toolsFrame 
toolsFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3, bg="#1A3C40")
toolsFrame.pack(side=LEFT, padx=10)

pencilButton = Button(toolsFrame, text="Pencil", width=10, command=usePencil, bg="#4B9CD3", fg="black")
pencilButton.pack(pady=5)
eraserButton = Button(toolsFrame, text="Eraser", width=10, command=useEraser, bg="#4B9CD3", fg="black")
eraserButton.pack(pady=5)
clearImageButton = Button(toolsFrame, text="Clear", bg="#FF4C4C", width=10, command=clear, fg="black")
clearImageButton.pack(pady=5)


# Frame - 2 - Canvas and Predictions
frame2 = Frame(root, height=400, width=800)
frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Prediction label
predictions_label = Label(frame2, width=20,heigh=400,text="Predictions: ", font=("Helvetica", 14), justify=LEFT, bg="#F5F5F5", fg="#1A3C40", padx=10, pady=10, relief=RAISED)
predictions_label.pack(side=LEFT, padx=10)

# Canvas
canvas_frame = Frame(frame2, bg="#F5F5F5")
canvas_frame.pack(side=RIGHT, expand=True)

canvas = Canvas(canvas_frame,width=200, height=200, bg="black")
canvas.pack(pady=10, expand=True)
canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)
canvas.bind("<B3-Motion>", paint)

# Define category names
names = {0: 'ladder', 1: 'butterfly', 2: 'book', 3: 'dog', 4: 'headphones', 5: 'lightning', 6: 'key', 7: 'arm', 8: 'train', 9: 'triangle', 10: 'house', 11: 'bird', 12: 'cow', 13: 'face', 14: 'elephant', 15: 'ice cream', 16: 'cat', 17: 'clock', 18: 'cloud', 19: 'tooth', 20: 'dolphin', 21: 'nail', 22: 'eye', 23: 'car', 24: 'axe', 25: 'banana', 26: 'tree', 27: 'telephone', 28: 'mouse', 29: 'apple', 30: 'vase', 31: 'bus', 32: 'flower', 33: 't-shirt', 34: 'airplane', 35: 'donut', 36: 'fish', 37: 'knife', 38: 'zigzag'}

root.resizable(False, False)
root.mainloop()
