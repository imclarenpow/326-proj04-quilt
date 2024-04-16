import sys
import matplotlib.pyplot as plt
import tkinter as tk
from tkcolorpicker import askcolor
lines = []
# lists for storing values
scale = []
rVal = []
gVal = []
bVal = []
# variables for gui
scaleEntry = None
guiClosed = False

# simple method to handle input.
def inputHandler():
    global lines, guiClosed
    print("Syntax: 'scale r g b'\nUse ctrl+c or 'exit' to close input.\nOr use 'gui' to input using the gui")
    try:
        try:
            while not guiClosed:
                line = input()
                if(syntaxHandler(line)):
                    lines.append(line)
                    print("Added!")
                elif(line.upper()=="GUI"):
                    gui()
                elif(line.upper()=="EXIT"):
                    break
        except EOFError:
            print("\nEnd of File")
    except KeyboardInterrupt:
        print("\nInterrupted by user")
# method to handle errors in input as to not add them to the data
def syntaxHandler(input_str):
    global scale, rVal, gVal, bVal
    parts = input_str.split(" ")
    # check there are enough values given
    if len(parts) != 4:
        return False
    # try for parsing values
    try:
        scale.append(float(parts[0]))
        rVal.append(int(parts[1]))
        gVal.append(int(parts[2]))
        bVal.append(int(parts[3]))
        idx = len(scale)-1
        # check that rgb & scale numbers are valid.
        if scale[idx] < 0 or rVal[idx] < 0 or rVal[idx] > 255 or bVal[idx] < 0 or bVal[idx] > 255 or gVal[idx] < 0 or gVal[idx] > 255:
            return False
    except ValueError:
        return False
    return True

# method for controlling the gui input
def gui():
    global scaleEntry, guiClosed
    root = tk.Tk()
    root.title("Quilting Bee")
    # Lets the Done Button Exit the Input Stream thus bring up the quilt.
    def closeGUI():
        global guiClosed
        guiClosed = True
        root.destroy()
    # Instructions
    instructions = tk.Label(root, text="Input Scale, Then Select Colour.\nWhen Done is Pressed it is Added.")
    instructions.grid(row=0, column=0, columnspan=2)
    # Scale Input
    scaleLabel = tk.Label(root, text="Scale:")
    scaleLabel.grid(row=2, column=0)
    scaleEntry = tk.Entry(root)
    scaleEntry.grid(row=2, column=1)
    # Color picker button
    colorButton = tk.Button(root, text="Pick Color", command=addGUIData)
    colorButton.grid(row=3, column=0, columnspan=2)
    # Done button
    doneButton = tk.Button(root, text="Done", command=closeGUI)
    doneButton.grid(row=6, column=0, columnspan=2)
    root.mainloop()

# method for adding data from the gui to the variables
def addGUIData():
    global scaleEntry
    scaleVal = scaleEntry.get()
    try:
        scaleVal = float(scaleVal)
        # get the color as seperate r, g and b values
        color = askcolor(color=(255, 255, 255))
        if color[0] is not None:
            r_val, g_val, b_val = color[0]
            scale.append(scaleVal)
            rVal.append(r_val)
            gVal.append(g_val)
            bVal.append(b_val)
            lines.append(f"{scaleVal} {r_val} {g_val} {b_val}")
            print("Added!")
        else:
            print(text="No color selected")
    except ValueError:
        print(text="Invalid scale value")
    
# recursive method for adding the squares to the 
def drawSquare(x, y, size, depth):
    global scale, rVal, gVal, bVal
    if(depth>=maxDepth):
        return
    r = rVal[depth]/255.0
    g = gVal[depth]/255.0
    b = bVal[depth]/255.0
    sz = size * scale[depth]
    cx = x - sz/2
    cy = y - sz/2
    plt.gca().add_patch(plt.Rectangle((cx, cy), sz, sz, fill=True, color=(r,g,b)))
    # sizing for smaller squares
    sqrs = sz/2
    drawSquare(x-sqrs,y-sqrs,size,depth+1)  # top left corner
    drawSquare(x-sqrs,y+sqrs,size,depth+1)  # bottom left corner
    drawSquare(x+sqrs,y-sqrs,size,depth+1)  # top right corner
    drawSquare(x+sqrs,y+sqrs,size,depth+1)  # bottom right corner


inputHandler()
sizer = 250
windowSz = 0
for scl in scale:
    windowSz += scl*sizer
fig, ax = plt.subplots(figsize=(windowSz/100, windowSz/100), subplot_kw=dict(aspect="equal"))
# Set axis limits to cover the entire plot area
ax.set_xlim(0, windowSz)  
ax.set_ylim(0, windowSz)  
maxDepth = len(scale)
drawSquare(0,0,sizer,0)
plt.axis('equal')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()