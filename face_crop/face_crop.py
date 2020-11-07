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

    # def distance(p1,p2):
    #     dx = p2[0] - p1[0]
    #     dy = p2[1] - p1[1]
    #
    #     return math.sqrt(dx*dx+dy*dy)
    #
    # def scale_rotate_translate(self, image, angle, center = None, new_center = None, scale = None, resample=Image.BICUBIC):
    #     if (scale is None) and (center is None):
    #         return image.rotate(angle=angle, resample=resample)
    #     nx,ny = x,y = center
    #     sx=sy=1.0
    #     if new_center:
    #         (nx,ny) = new_center
    #     if scale:
    #         (sx,sy) = (scale, scale)
    #     cosine = math.cos(angle)
    #     sine = math.sin(angle)
    #     a = cosine/sx
    #     b = sine/sx
    #     c = x-nx*a-ny*b
    #     d = -sine/sy
    #     e = cosine/sy
    #     f = y-nx*d-ny*e
    #
    #     return image.transform(image.size, Image.AFFINE, (a,b,c,d,e,f), resample=resample)
    #
    # def crop_face(self, image, eye_left=(0, 0), eye_right=(0, 0), offset_pct=(0.3, 0.3), dest_sz=(600, 600)):
    #     print(eye_left, eye_right, offset_pct, dest_sz)
    #     offset_h = math.floor(float(offset_pct[0]) * dest_sz[0])
    #     offset_v = math.floor(float(offset_pct[1]) * dest_sz[1])
    #     print(offset_h, offset_v)
    #     eye_direction = (eye_right[0] - eye_left[0], eye_right[1] - eye_left[1])
    #     print(eye_direction)
    #     rotation = -math.atan2(float(eye_direction[1]), float(eye_direction[0]))
    #     print(rotation)
    #     dist = self.distance(eye_left, eye_right)
    #     reference = dest_sz[0] - 2.0 * offset_h
    #
    #     scale = float(dist) / float(reference)
    #
    #     image = self.scale_rotate_translate(image, center=eye_left, angle=rotation)
    #
    #     display(image)
    #     crop_xy = (eye_left[0] - scale * offset_h, eye_left[1] - scale * offset_v)
    #     print(crop_xy)
    #     crop_size = (dest_sz[0] * scale, dest_sz[1] * scale)
    #     image = image.crop(
    #         (int(crop_xy[0]), int(crop_xy[1] - 30), int(crop_xy[0] + crop_size[0]), int(crop_xy[1] + crop_size[1])))
    #
    #     # image = image.resize(dest_sz, Image.ANTIALIAS)
    #     return image
    #
    # def face_identify(file_path):
    #     test = face_recognition.load_image_file(file_path)
    #     no_of_faces = 0
    #     land_marks_of_faces = {}
    #     face_landmarks_list = face_recognition.face_landmarks(test)
    #     for face_landmarks in face_landmarks_list:
    #         pts = []
    #         land_marks_of_face = {}
    #         no_of_faces = no_of_faces + 1
    #         facial_features = ['chin', 'left_eyebrow', 'right_eyebrow', 'nose_bridge',
    #                      'nose_tip', 'left_eye', 'right_eye', 'top_lip',
    #                      'bottom_lip']
    #         for facial_feature in facial_features:
    #             land_marks_of_face[facial_feature] = face_landmarks[facial_feature]
    #             for point in face_landmarks[facial_feature]:
    #                 for pix in point:
    #                     pts.append(pix)
    #
    #         land_marks_of_faces[no_of_faces] = land_marks_of_face
    #
    #     face_crop.no_of_faces = no_of_faces
    #     face_crop.land_marks = land_marks_of_faces
    #     # return {'no_of_faces': no_of_faces, 'land_marks': land_marks_of_faces}
    #     # for face_landmarks in face_landmarks_list:
    #     #     pts = []
    #     #     no_of_faces = no_of_faces + 1
    #     #     facial_features = ['chin', 'left_eyebrow', 'right_eyebrow', 'nose_bridge',
    #     #              'nose_tip', 'left_eye', 'right_eye', 'top_lip',
    #     #              'bottom_lip']
    #     # for facial_feature in facial_features:
    #     #     print(facial_feature,face_landmarks[facial_feature])
    #     #     for  point in  face_landmarks[facial_feature]:
    #     #         for pix in point:
    #     #             pts.append(pix)
    #     #
    #     #
    #     # print(pts)
    #     #
    #     # eyes = []
    #     # lex = pts[72]
    #     # ley = pts[73]
    #     # rex = pts[90]
    #     # rey = pts[91]
    #     # eyes.append(pts[72:74])
    #     # eyes.append(pts[90:92])
    #     # image = Image.open(file_path)
    #     # display(image)
    #     # land_marks_of_faces[no_of_faces] = {"pts": pts , "eyes": eyes, "lex": lex, "ley": ley, "rex": rex, "rey": rey}
    #     #
    #     # return land_marks_of_faces
    #         # crop_image = self.crop_face(image, eye_left=(lex, ley), eye_right=(rex, rey), offset_pct=(0.34,0.34), dest_sz=(300,300))
    #
    #         # display(crop_image)