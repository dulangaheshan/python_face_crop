import math
import face_recognition
from PIL import Image, ImageDraw
from IPython.display import display
# import cv2
import numpy as np
import math

class face_crop:

    def __init__(self, file_path):
        self.no_of_faces = 0
        self.land_marks = {}

        test = face_recognition.load_image_file(file_path)
        no_of_faces = 0
        land_marks_of_faces = {}
        face_landmarks_list = face_recognition.face_landmarks(test)
        for face_landmarks in face_landmarks_list:
            pts = []
            land_marks_of_face = {}
            no_of_faces = no_of_faces + 1
            facial_features = ['chin', 'left_eyebrow', 'right_eyebrow', 'nose_bridge',
                         'nose_tip', 'left_eye', 'right_eye', 'top_lip',
                         'bottom_lip']
            for facial_feature in facial_features:
                land_marks_of_face[facial_feature] = face_landmarks[facial_feature]
                for point in face_landmarks[facial_feature]:
                    for pix in point:
                        pts.append(pix)

            land_marks_of_faces[no_of_faces] = land_marks_of_face

        self.no_of_faces = no_of_faces
        self.land_marks = land_marks_of_faces


    def view_land_marks(self, face_number):
        return self.land_marks[face_number]

