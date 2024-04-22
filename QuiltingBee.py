import matplotlib

import time

import matplotlib.pyplot as plt
import numpy as np

def inputHandler():
    lines = []
    print("Syntax: 'scale r g b'\nUse ctrl+c or 'exit' to close input.")
    try:
        while True:
            line = input()
            if line.upper() == "EXIT":
                break
            if syntaxHandler(line):
                lines.append(line)
                print("Added!")
    except (EOFError, KeyboardInterrupt):
        pass
    return lines

def syntaxHandler(input_str):
    parts = input_str.split()
    if len(parts) != 4:
        return False
    try:
        scale.append(float(parts[0].strip()))
        rVal.append(int(parts[1].strip()))
        gVal.append(int(parts[2].strip()))
        bVal.append(int(parts[3].strip()))
        idx = len(scale) - 1
        if any(val < 0 or val > 255 for val in (rVal[idx], gVal[idx], bVal[idx])):
            return False
    except ValueError:
        return False
    return True

def drawSquares(x, y, size, depth):
    if depth >= maxDepth:
        return
    colors = np.array([rVal[depth], gVal[depth], bVal[depth]]) / 255.0
    sz = size * scale[depth]
    cx = x - sz / 2
    cy = y - sz / 2
    ax.add_patch(plt.Rectangle((cx, cy), sz, sz, fill=True, color=colors))
    sqrs = sz / 2
    drawSquares(x - sqrs, y - sqrs, size, depth + 1)
    drawSquares(x - sqrs, y + sqrs, size, depth + 1)
    drawSquares(x + sqrs, y - sqrs, size, depth + 1)
    drawSquares(x + sqrs, y + sqrs, size, depth + 1)

if __name__ == "__main__":
    start_time = time.time()
    scale, rVal, gVal, bVal = [], [], [], []
    lines = inputHandler()
    sizer = 250
    windowSz = sum(scale) * sizer
    if windowSz > 750:
        sizer = 750 / sum(scale)
        windowSz = sum(scale) * sizer
    else:
        windowSz = 750
    fig, ax = plt.subplots(figsize=(windowSz / 100, windowSz / 100), subplot_kw=dict(aspect="equal"))
    ax.set_xlim(0, windowSz)
    ax.set_ylim(0, windowSz)
    maxDepth = len(scale)
    drawSquares(0, 0, sizer, 0)
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout(pad=0)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time: {:.2f} seconds".format(execution_time))
    plt.show()
    
