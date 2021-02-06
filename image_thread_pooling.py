from concurrent.futures import ThreadPoolExecutor
import time
import os
import random
from os import listdir
from os.path import isfile, join
import cv2


def wait_function(base_image, images_target, new_images_path):
    try:
        percentage = 0.50
        cv2.imread(base_image)
        sift = cv2.xfeatures2d.SIFT_create()
        base_image_original = os.path.basename(base_image)
        base_image = cv2.imread(base_image)
        geo_portail = []
        for idxInt, fileD in enumerate(images_target):
            file_name = str(os.path.basename(fileD))
            file_path = str(fileD)
            if os.path.exists(file_path):
                # target_image_color = cv2.imread(file_path)
                target_image = cv2.imread(file_path, 0)
                kp1, des1 = sift.detectAndCompute(base_image, None)
                kp2, des2 = sift.detectAndCompute(target_image, None)
                bf = cv2.BFMatcher()
                matches = bf.knnMatch(des1, des2, k=2)
                good = []
                min_goods = 700
                max_goods = 850

                for match1, match2 in matches:
                    percentage = 0.65 if base_image_original == 'logo.png' else percentage
                    percentage = 0.65 if base_image_original == 'logo_cadastre.png' else percentage

                    if match1.distance < percentage * match2.distance:
                        good.append([match1])

                        if base_image_original == "doble.png":
                            if file_path not in geo_portail and len(matches) >= 1400 and len(good) >= 70:
                                geo_portail.append(file_path)
                                cv2.imwrite(os.path.join(new_images_path, file_name), target_image)
                                matched = True
                                if idx > 0 and len(images_target) > 0:
                                    print(f"Saved: doble.png => {file_name}")
                                    del images_target[idx]
                                    break

                        if base_image_original == "green.png":
                            if file_path not in geo_portail and len(matches) >= 2500 and len(good) >= 120:
                                geo_portail.append(file_path)
                                cv2.imwrite(os.path.join(new_images_path, file_name), target_image)
                                matched = True
                                if idx > 0 and len(images_target) > 0:
                                    del images_target[idx]
                                    print(f"Saved: green.png => {file_name}")
                                    break

                        if base_image_original == "icons.png":
                            if file_path not in geo_portail and len(matches) >= 120 and len(good) >= 45:
                                geo_portail.append(file_path)
                                cv2.imwrite(os.path.join(new_images_path, file_name), target_image)
                                matched = True
                                if idx > 0 and len(images_target) > 0:
                                    del images_target[idx]
                                    print(f"Saved: icons.png => {file_name}")
                                    break

                        if base_image_original == "logo_cadastre.png":
                            if file_path not in geo_portail and len(matches) >= 150 and len(good) >= 27:
                                geo_portail.append(file_path)
                                cv2.imwrite(os.path.join(new_images_path, file_name), target_image)
                                matched = True
                                if idx > 0 and len(images_target) > 0:
                                    del images_target[idx]
                                    print(f"Saved: logo_cadastre.png => {file_name}")
                                    break

                        if base_image_original == "logo.png":
                            if file_path not in geo_portail and len(matches) > 200 and len(good) >= 75:
                                geo_portail.append(file_path)
                                cv2.imwrite(os.path.join(new_images_path, file_name), target_image)
                                matched = True
                                if idx > 0 and len(images_target) > 0:
                                    del images_target[idx]
                                    print(f"Saved: logo.png => {file_name}")
                                    break
        return geo_portail

    except cv2.error as e:
        print(e)
        return False



def callback_function(future):
    print('Callback with the following result', future.result())

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





 # Init App #
start = time.time()
worker_count = 8
percentage = 0.50
base_path = os.getcwd()
img_subjects_path = os.path.join(base_path, "images_subject")
new_imgs_path = os.path.join(base_path, "new_images")
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
        future = executor.submit(wait_function, image_subject, images_target_path, new_imgs_path)
        future.add_done_callback(callback_function)

    # while True:
        # if (future.done()):
            # print(future.result())
            # break
print(time.time() - start)
