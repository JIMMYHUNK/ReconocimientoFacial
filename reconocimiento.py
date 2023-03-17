import datetime
import cv2
import face_recognition

class Reconocimiento:
    # Detecta la fecha y hora actual del reconocimiento facial
    ahora = datetime.datetime.now()

    # Imagen guardada
    image = cv2.imread("imagenes/Jimmy.jpg")

    face_loc = face_recognition.face_locations(image)[0]
    face_image_ecodings = face_recognition.face_encodings(
        image, known_face_locations=[face_loc])[0]

    # Foto
    cap = cv2.VideoCapture(0)
    it = 0
    while it < 1:
        ret, frame = cap.read()
        if ret == False:
            break
        it = it + 1

        """ frame = cv2.flip(frame,1) """

        face_locations = face_recognition.face_locations(frame)
        if face_locations != []:
            for face_location in face_locations:
                face_frame_encodings = face_recognition.face_encodings(
                    frame, known_face_locations=[face_location])[0]
                result = face_recognition.compare_faces(
                    [face_frame_encodings], face_image_ecodings)
                print(result, ahora)

                if result[0] == True:
                    text = "Jimmy"
                    color = (125, 220, 0)
                else:
                    text = "Desconocido"
                    color = (50, 50, 255)

                cv2.rectangle(frame, (face_location[3], face_location[2]), (
                    face_location[1], face_location[2]+30), color, -1)
                cv2.rectangle(frame, (face_location[3], face_location[0]), (
                    face_location[1], face_location[2]), color, 2)
                cv2.putText(
                    frame, text, (face_location[3], face_location[2]+20), 2, 0.7, (255, 255, 255), 1)
        cv2.imwrite("imagenes/foto.png", frame)

        k = cv2.waitKey(1)
        if k == 27 & 0xFF:
            break

    cap.release()
    cv2.destroyAllWindows()
