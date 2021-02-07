from concurrent.futures import ThreadPoolExecutor
import time
import os
import random
from os import listdir
from os.path import isfile, join
import cv2
import multiprocessing
import threading

# def wait_function(images_target_chunk, new_images_path, images_subject):
def wait_function(single_image_target, new_images_path, images_subject):
    try:
        percentage = 0.50
        geo_portail = []
        sift = cv2.xfeatures2d.SIFT_create()
        images_target_chunk = [single_image_target]

        for id_img, base_image in enumerate(images_subject):
            # print(f"image subject {id_img} - {images_subject[id_img]}")
            # cv2.imread(base_image)
            base_image_original = os.path.basename(base_image)
            print(f"{str(threading.current_thread().name)}::IMAGE SUBJECT:: {base_image_original}")
            print(f" ")
            base_image = cv2.imread(base_image, 0)
            print(f"__Supouse to check {single_image_target} ")
            for idxInt, fileD in enumerate([single_image_target]):
                # print(f"____Checking... Image Target {fileD} ")
                # print(f"Image to processe {single_image_target} ")
                file_path = str(fileD)
                if os.path.exists(file_path):
                    print(f"____file exist {True} ")
                    file_name = str(os.path.basename(fileD))
                    target_image_color = cv2.imread(file_path)
                    target_image = cv2.imread(file_path, 0)
                    kp1, des1 = sift.detectAndCompute(base_image, None)
                    kp2, des2 = sift.detectAndCompute(target_image, None)
                    bf = cv2.BFMatcher()
                    matches = bf.knnMatch(des1, des2, k=2)
                    good = []
                    percentage = 0.65 if base_image_original == 'logo.png' else percentage
                    percentage = 0.65 if base_image_original == 'logo_cadastre.png' else percentage

                    cont = 0
                    for match1, match2 in matches:
                        if match1.distance < percentage * match2.distance:
                            good.append([match1])
                            if cont == 0:
                                # print(f"____found match {True} " )
                                cont = 1
                            if base_image_original == "doble.png":
                                if file_path not in geo_portail and len(matches) >= 1400 and len(good) >= 70:
                                    # geo_portail.append(file_path)
                                    cv2.imwrite(os.path.join(new_images_path, file_name), target_image_color)
                                    matched = True
                                    if idx > 0 and len(images_target_chunk) > 0:
                                        print(f"Saved: {base_image_original} => {file_name} current size chunk {len(images_target_chunk)} - {id_img}")
                                        del images_target_chunk[idxInt]
                                        print(f"{base_image_original}: after delete: {len(images_target_chunk)} - {id_img}")
                                        break

                            if base_image_original == "green.png":
                                if file_path not in geo_portail and len(matches) >= 2500 and len(good) >= 120:
                                    # geo_portail.append(file_path)
                                    cv2.imwrite(os.path.join(new_images_path, file_name), target_image_color)
                                    matched = True
                                    if idx > 0 and len(images_target_chunk) > 0:
                                        print(f"Saved: {base_image_original} => {file_name} current size chunk {len(images_target_chunk)} - {id_img}")
                                        del images_target_chunk[idxInt]
                                        print(f"{base_image_original}: after delete: {len(images_target_chunk)} - {id_img}")
                                        break

                            if base_image_original == "icons.png":
                                if file_path not in geo_portail and len(matches) >= 120 and len(good) >= 45:
                                    # geo_portail.append(file_path)
                                    cv2.imwrite(os.path.join(new_images_path, file_name), target_image_color)
                                    matched = True
                                    if idx > 0 and len(images_target_chunk) > 0:
                                        print(f"Saved: {base_image_original} => {file_name} current size chunk {len(images_target_chunk)} - {id_img}")
                                        del images_target_chunk[idxInt]
                                        print(f"{base_image_original}: after delete: {len(images_target_chunk)} - {id_img}")
                                        break

                            if base_image_original == "logo_cadastre.png":
                                if file_path not in geo_portail and len(matches) >= 150 and len(good) >= 27:
                                    # geo_portail.append(file_path)
                                    cv2.imwrite(os.path.join(new_images_path, file_name), target_image_color)
                                    matched = True
                                    if idx > 0 and len(images_target_chunk) > 0:
                                        print(f"Saved: {base_image_original} => {file_name} current size chunk {len(images_target_chunk)} - {id_img}")
                                        del images_target_chunk[idxInt]
                                        print(f"{base_image_original}: after delete: {len(images_target_chunk)} - {id_img}")
                                        break

                            if base_image_original == "logo.png":
                                if file_path not in geo_portail and len(matches) > 200 and len(good) >= 75:
                                    # geo_portail.append(file_path)
                                    # print(f"Save here: {os.path.join(new_images_path, file_name)}")
                                    cv2.imwrite(os.path.join(new_images_path, file_name), target_image_color)
                                    matched = True
                                    if idx > 0 and len(images_target_chunk) > 0:
                                        print(f"Saved: {base_image_original} => {file_name} current size chunk {len(images_target_chunk)} - {id_img}")
                                        del images_target_chunk[idxInt]
                                        print(f"{base_image_original}: after delete: {len(images_target_chunk)} - {id_img}")
                                        break

                            if len(good) >= 125:
                                print('::::::::break Good:::::::')
                                break
        #     print(f"{base_image_original}: acabo chunk : {len(images_target_chunk)} - {id_img}")
        #
        # print(f"{base_image_original}: ACABO SUBJECT : {len(images_target_chunk)} - {images_subject[id_img]}")
        # print(f"GEO PORTAILS {len(geo_portail)}")
        return True

    except ValueError as e:
        print('main: saw error "{}" when accessing result'.format(e))
        return False

def callback_function(future):
    print(f"future it finshed a :: {future.result()}")
    return future.result()

def chunks(imgs_target_path, n):
    for i in range(0, len(imgs_target_path), n):
        yield imgs_target_path[i:i + n]
    return imgs_target_path

 # Init App #
start = time.time()
################################
#
################################
worker_count = multiprocessing.cpu_count()
# worker_count = 32
percentage = 0.50
base_path = os.getcwd()
img_subjects_path = os.path.join(base_path, "images_subject")
new_imgs_path = os.path.join(base_path, "new_images")
images_subject = [os.path.join(img_subjects_path, f) for f in listdir(img_subjects_path) if isfile(join(img_subjects_path, f))]
# Images Target
imgs_paths = []
images_target_path = os.path.join(base_path, "images_target")
images_target_path = os.path.abspath(images_target_path)
images_subject = [os.path.join(img_subjects_path, f) for f in listdir(img_subjects_path) if isfile(join(img_subjects_path, f))]
images_target_path = [os.path.join(images_target_path, f) for f in listdir(images_target_path) if isfile(join(images_target_path, f))]
new_images_target = []
for im in images_target_path:
    if os.path.exists(im):
        new_images_target.append(im)

target_imgs_count = len(new_images_target)
all_images_target = chunks(new_images_target, 1)
images_target_path = all_images_target
cont = 0
with ThreadPoolExecutor(max_workers=worker_count) as executor:  # change max_workers to 2 and see the results
    for idx, image_target_chunk in enumerate(images_target_path):
        for index, image_target in enumerate(image_target_chunk):
            globals()[f'future{idx}'] = executor.submit(wait_function, image_target, new_imgs_path, images_subject)
            # globals()[f'future{idx}'].add_done_callback(callback_function)
            # print(f"GLOBAL{f'future{idx}'} ----- {image_target}-({index}) --- {cont}")
            cont = cont + 1

    while True:
        for i in range(0, cont):
            var_future = globals()[f'future{i}']
            if var_future.running():
                print(f'future{i} is running')
            elif var_future.done():
                print(f'future{cont}', ':::::DONE::::')
                break
                exit()
        break

print(f"TOTAL: {time.time() - start} of {target_imgs_count} ")
