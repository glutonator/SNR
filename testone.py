import cv2
import os
from matplotlib import pyplot as plt
from skimage import feature
import numpy as np


def localBinaryPatterns(image, numPoints, radius, eps=1e-7):
    # compute the Local Binary Pattern representation
    # of the image, and then use the LBP representation
    # to build the histogram of patterns
    lbp = feature.local_binary_pattern(image, numPoints,
                                       radius, method="uniform")
    # print(lbp)


    # cv2.imshow("image", image)
    # cv2.imwrite('color_img.jpg', lbp)
    # cv2.waitKey();

    # (hist, _) = np.histogram(lbp.ravel(),
    #                          bins=np.arange(0, numPoints + 3),
    #                          range=(0, numPoints + 2))
    #
    # # normalize the histogram
    # hist = hist.astype("float")
    # hist /= (hist.sum() + eps)

    # print histogram
    # plt.hist(lbp.ravel(),
    #          bins=np.arange(0, self.numPoints + 3),
    #          range=(0, self.numPoints + 2))
    # plt.show()

    # return the histogram of Local Binary Patterns
    # return hist
    return lbp

def createLBPimage(imagePath, image):
    pointsNumber = 8
    radius = 1

    image = cv2.imread(imagePath + '/' + image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    lbp = localBinaryPatterns(gray, pointsNumber, radius)

    # print(lbp)

    return lbp


def createTraingSet():
    # List with histograms
    x = []
    # List with labels
    y = []

    # paths
    path = './fruits/fruits-360/Test'
    dirpath = os.getcwd()
    subfolders = os.listdir(path)
    print(subfolders)

    # get data
    for folder in subfolders:
        print(folder)
        tmp_path = path + "/" + folder
        images = os.listdir(tmp_path)
        for image in images:
            # print(image)
            # create histogram
            tmp_hist = createLBPimage(tmp_path, image)

            # save histogram
            x.append(tmp_hist)

            # save label
            y.append(folder)

            # break
        # break
    return x, y


# def main():
print("Hello World!")
# dataX, dataY = createTraingSet()
# np.save("dataX.npy", dataX)
# np.save("dataY.npy", dataY)
dataXXX = np.load("dataX.npy")
dataYYY = np.load("dataY.npy")

# if __name__ == "__main__":
#     main()
