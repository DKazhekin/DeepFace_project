import os

import face_recognition
from PIL import Image, ImageDraw


def filter_my1(path):
    copy = 'cp ' + path + ' ./test_input/'
    os.system(copy)
    name_photo = os.path.basename(path)
    command = '/home/oopbot/venv/bin/python evaluate.py --device cpu --input ' + name_photo + ' --model_name sketch_multi --seed 3000'
    name_file = os.path.splitext(path)[0]
    name_file2 = os.path.basename(name_file)
    output_file = './results/result_sketch_multi_' + name_file2 + '.png'
    os.system(command)
    return output_file


def filter_my2(path):
    copy = 'cp ' + path + ' ./test_input/'
    os.system(copy)
    name_photo = os.path.basename(path)
    command = '/home/oopbot/venv/bin/python evaluate.py --device cpu --input ' + name_photo + ' --model_name art --seed 3000'
    name_file = os.path.splitext(path)[0]
    name_file2 = os.path.basename(name_file)
    output_file = './results/result_art_' + name_file2 + '.png'
    os.system(command)
    return output_file


def filter_my3(path):
    copy = 'cp ' + path + ' ./test_input/'
    os.system(copy)
    name_photo = os.path.basename(path)
    command = './venv/bin/python evaluate.py --device cpu --input ' + name_photo + ' --model_name arcane_multi --seed 3000'
    name_file = os.path.splitext(path)[0]
    name_file2 = os.path.basename(name_file)
    output_file = './results/result_arcane_multi_' + name_file2 + '.png'
    os.system(command)
    return output_file


def face_rec(path):
    face_rec = face_recognition.load_image_file(path)

    face_location = face_recognition.face_locations(face_rec)
    print(len(face_location))
    pil_img1 = Image.fromarray(face_rec)
    draw1 = ImageDraw.Draw(pil_img1)
    for (top, right, bottom, left) in face_location:
        draw1.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

    del draw1

    pil_img1.save("images/new.jpg")

    return len(face_location)


def compare(img1_path, img2_path):
    img1 = face_recognition.load_image_file(img1_path)
    if len(face_recognition.face_encodings(img1)) == 0:
        print("На фото разные люди")
        return 2
    img1_encodings = face_recognition.face_encodings(img1)[0]

    img2 = face_recognition.load_image_file(img2_path)
    if len(face_recognition.face_encodings(img2)) == 0:
        print("На фото разные люди")
        return 2
    img2_encodings = face_recognition.face_encodings(img2)[0]

    result = face_recognition.compare_faces([img1_encodings], img2_encodings)

    if result[0]:
        print("На фото один и тот же человек")
        return 1
    else:
        print("На фото разные люди")
        return 2


def main():
    pass


if __name__ == '__main__':
    main()
