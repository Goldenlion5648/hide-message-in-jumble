from PIL import Image
import os
import numpy as np
import sys
# qr = Image.open("smallerQR.png")
# qr = Image.open(
#     input("what is the name of the file you want to open? (with extension): "))
def get_data(filename):
    image_name = f"{filename}.png"
    qr = Image.open(image_name)
    data_image = np.zeros((qr.size[1], qr.size[0]), dtype=int)
    black_character = "1"
    white_character = "0"
    qr_pixels = qr.load()
    i = 0
    all_filled = set()
    for i in range(qr.size[0]):
        for j in range(qr.size[1]):
            # print(xPos, yPos)
            # print(qr_pixels[i, j])
            if sum(qr_pixels[i, j]) >500:
                data_image[j][i]=black_character
                all_filled.add((i, j))
            else:
                data_image[j][i]=white_character
    temp = data_image.copy()
    to_check = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    new_data_image = data_image.copy()
    # print(qr.size)
    # print(data_image)
    for x in range(qr.size[0]):
        for y in range(qr.size[1]):
            if data_image[y][x] == int(white_character):
                count = 0
                # print(y, x)
                for dy, dx in to_check:
                    if not (0 <= y+dy < qr.size[1] and 0 <= x+dx < qr.size[0]):
                        continue
                    if data_image[y+dy][x+dx] == int(white_character):
                        count += 1
                # print("count", count)
                if count == 1:
                    new_data_image[y][x] = black_character

    data_image = new_data_image.copy()

    with open(image_name[:image_name.index(".")] + "_as_data.txt", 'w') as f:
        for i in data_image:
            print(*i, sep="", file=f)

if __name__ == '__main__':
    # try:
        print(sys.argv)
        get_data(sys.argv[1])
    # except:
        # print("use the file name (no ext) after the name of this file")
