# coding=utf-8
import sys
import os
from PIL import Image

def convertPixel(r, g, b, a=1.):
    color = "#%02X%02X%02X" % (r, g, b)
    opacity = a
    return (color, opacity)


if __name__ == "__main__":
    for file_path in sys.argv[1:]:
        file_name, file_ext = os.path.splitext(file_path)
        if not os.path.exists(file_path):
            raise '%s file not exist' % file_path

        img = Image.open(file_path)
        mode = img.mode
        pixels = img.load()
        w, h = img.size

        print("image mode: ", mode)
        if "RGB" not in mode:
            raise "image mode not supported, need to be 24pixel depth"

        output = "<svg width='%d' height='%d' viewBox='0 0 %d %d' xmlns='http://www.w3.org/2000/svg'>" % (w, h, w, h) 
        for r in range(h): 
            for c in range(w): 
                color, opacity = convertPixel(*pixels[c, r]) 
                output += "<rect x='%d' y='%d' width='1' height='1' fill='%s' fill-opacity='%s'/>" % (c, r, color, opacity) 
        output += "</svg>"
        with open(file_name + ".svg", "w") as f: 
            f.write(output)