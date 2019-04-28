from numpy import zeros
import matplotlib.pyplot as plt

def Julia():
    
    rows = 600
    columns = 800
    scale = 0.5
    xcontract = 1.5
    ycontract = 1.0
    steps = 255
    shape_1 = 0.7 # these are like some kind of threshold
    shape_2 = 0.27015 

    myarray = zeros([rows, columns])

    for col in range(columns):
        for row in range(rows):
            zx = xcontract*(col-columns/2)/(scale*columns)
            zy = ycontract*(row-rows/2)/(scale*rows)
            i = steps
            t = True
            while t == True:
                if zx*zx+zy*zy >= 4:
                    t = False
                if i <= 1:
                    t = False
                a = zx * zx - zy * zy - shape_1
                zy = 2.0 * zx * zy + shape_2
                zx = a
                i = i - 1
            myarray[row][col] = i

    plt.imshow(myarray)
    plt.show()