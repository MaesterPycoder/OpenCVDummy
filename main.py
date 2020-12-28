import cv2
import face_recognition

imgElon = face_recognition.load_image_file(r'ImagesBasic\elonMusk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgElonTest = face_recognition.load_image_file(r'ImagesBasic\testElon.jpg')
imgElonTest = cv2.cvtColor(imgElonTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
faceLocTest = face_recognition.face_locations(imgElonTest)[0]
encodeElonTest = face_recognition.face_encodings(imgElonTest)[0]
cv2.rectangle(imgElonTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeElon], encodeElonTest)
facDis = face_recognition.face_distance([encodeElon], encodeElonTest)
cv2.putText(imgElonTest, f"{results[0]} {round(facDis[0], 2)}", (100, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Musk Test', imgElonTest)
cv2.waitKey(0)





# def markAttendance(name):
#     with open('Attendance.csv', 'r+') as f:
#         myDataList = f.readlines()
#     nameList = []
#     for line in myDataList:
#         entry = line.split(',')
#         nameList.append(entry[0])
#     if name not in nameList:
#         now = datetime.now()
#     dtString = now.strftime('%H:%M:%S')
#     f.writelines(f'\n{name},{dtString}')
# # FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr
