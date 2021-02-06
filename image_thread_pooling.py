from concurrent.futures import ThreadPoolExecutor
import time
import os
import random
from os import listdir
from os.path import isfile, join
import cv2


def fibo(n):
    a = 0
    b = 1
    total_sum = 0
    count = 1
    # print("Fibonacci Series: ", end=" ")
    while count <= n:
        # print(total_sum, end=" ")
        count += 1
        a = b
        b = total_sum
        total_sum = a + b

    return total_sum


def wait_function(base_image, images_target, id_index):
    cv2.imread(base_image)
    sift = cv2.xfeatures2d.SIFT_create()
    base_image_original = os.path.basename(base_image)
    base_image = cv2.imread(base_image)
    for idxInt, fileD in enumerate(images_target):
        file_name = str(os.path.basename(fileD))
        file_path = str(fileD)
        if os.path.exists(file_path):
            target_image_color = cv2.imread(file_path)
            target_image = cv2.imread(file_path, 0)
            kp1, des1 = sift.detectAndCompute(base_image, None)
            kp2, des2 = sift.detectAndCompute(target_image, None)
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1, des2, k=2)
            good = []
            min_goods = 700
            max_goods = 850
            print(f":::::::{base_image_original}:::::::")
            for match1, match2 in matches:
                if match1.distance < percentage * match2.distance:
                    good.append([match1])
                    print(f"{base_image_original}: {file_path} = {len(good)}")

    return True


def callback_function(future):
    print('Callback with the following result', future.result())

 # Init App #
start = time.time()
worker_count = 8
percentage = 0.50
base_path = os.getcwd()
img_subjects_path = os.path.join(base_path, "images_subject")
images_subject = [os.path.join(img_subjects_path, f) for f in listdir(img_subjects_path) if isfile(join(img_subjects_path, f))]
# Images Target
imgs_paths = []
images_target_path = os.path.join(base_path, "images_target")
images_target_path = os.path.abspath(images_target_path)
for root, sub_dirs, files in os.walk(images_target_path):
    for file in files:
        file_path = os.path.join(root, file)
        imgs_paths.append(file_path)
images_target_path = imgs_paths
with ThreadPoolExecutor(max_workers=worker_count) as executor:  # change max_workers to 2 and see the results
    for idx, image_subject in enumerate(images_subject):
        future = executor.submit(wait_function, image_subject, images_target_path, idx)
        # future.add_done_callback(callback_function)

    # while True:
        # if (future.done()):
            # print(future.result())
            # break
print(time.time() - start)
