from face_crop import face_crop


faces = face_crop('2.jpg')

print(faces.no_of_faces)
print(faces.view_land_marks(1))
