# CSC3014 Computer Vision Project
# Marcus Wong Ke Lun
# 18126672
# BSc (Hons) in Computer Science

import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

def detect_sky_region(dataset_number, file_name):
    
    img = cv2.imread(f"dataset/{dataset_number}/{file_name}", 1)
    # plt.figure()
    # plt.title("Original Image")
    # plt.imshow(img)
    # plt.show()
    
    blue_plane = img[:, :, 0]
    # plt.figure()
    # plt.title("Blue Colour Plane")
    # plt.imshow(blue_plane, cmap="gray")
    # plt.show()
    
    edges = cv2.Canny(blue_plane, 16, 186)
    # plt.figure()
    # plt.title("Edges")
    # plt.imshow(edges, cmap="gray")
    # plt.show()
    
    structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, structuring_element)
    # plt.figure()
    # plt.title("Closed Edges")
    # plt.imshow(closed_edges, cmap="gray")
    # plt.show()
    
    def fillhole(input_image):
        im_flood_fill = input_image.copy()
        h, w = input_image.shape[:2]
        mask = np.zeros((h + 2, w + 2), np.uint8)
        im_flood_fill = im_flood_fill.astype("uint8")
        cv2.floodFill(im_flood_fill, mask, (0, 0), 255)
        im_flood_fill_inv = cv2.bitwise_not(im_flood_fill)
        img_out = input_image | im_flood_fill_inv
        return img_out 
    
    filled_holes = fillhole(closed_edges)
    # plt.figure()
    # plt.title("Filled Holes")
    # plt.imshow(filled_holes, cmap="gray")
    # plt.show()
    
    inverted_img = cv2.bitwise_not(filled_holes)
    # plt.figure()
    # plt.title("Inverted Image")
    # plt.imshow(inverted_img, cmap="gray")
    # plt.show()
    
    current_directory = os.getcwd()
    new_directory = os.path.join(current_directory, f'output/{dataset_number}')
    if not os.path.exists(new_directory):
       os.makedirs(new_directory)
       
    cv2.imwrite(f"output/{dataset_number}/{file_name}_mask.jpg", inverted_img)

if __name__ == '__main__':
    current_directory = os.getcwd()
    dataset_number = ["1093", "4795", "8438", "10870", "4232", "9483", "10917"]
    for number in dataset_number:
        dataset_directory = os.path.join(current_directory, f'dataset/{number}')
        for file_name in os.listdir(dataset_directory):
            detect_sky_region(number, file_name)