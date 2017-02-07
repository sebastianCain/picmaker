from math import sqrt

file = open("image.ppm", "w")

imgstr = "P3 500 500 255\n"

for i in range(0, 500):
    for j in range(0, 500):
        dist = sqrt((250-j) ** 2 + (250-i) ** 2)
        scaled = int((dist / 250) * 255)
        
        red = str(scaled) + " "
        green = str(255 - scaled) + " "
        blue = str((127 + scaled) % 256) + " "
        if i == j or i == 500 - j or j == 250 or i == 250:
            imgstr += "0 0 0 "
        else:
            imgstr += red + green + blue
    imgstr += "\n"

file.write(imgstr)
