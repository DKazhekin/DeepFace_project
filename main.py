import face_recognition
from PIL import Image, ImageDraw


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