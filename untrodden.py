import  cv2
import face_recognition

input_video = cv2.VideoCapture("final_hera_pheri.mp4")                   #input video
length = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))


fourcc = cv2.VideoWriter_fourcc('M','P','E','G')     # Create an output movie file 

output_video = cv2.VideoWriter('OUTPUT_FINAL.avi', fourcc, 25, (640,360))

# Load some sample pictures and learn how to recognize them.
amitabh_image = face_recognition.load_image_file("amitabh.jpg")
amitabh_face_encoding = face_recognition.face_encodings(amitabh_image)[0]

ashrani_image = face_recognition.load_image_file("ashrani.png")
ashrani_face_encoding = face_recognition.face_encodings(ashrani_image)[0]

sulakshana_image = face_recognition.load_image_file("sulakshana.jpeg")
sulakshana_face_encoding = face_recognition.face_encodings(sulakshana_image)[0]

vinod_image = face_recognition.load_image_file("vinod.png")
vinod_face_encoding = face_recognition.face_encodings(vinod_image)[0]

mac_image = face_recognition.load_image_file("mac_mohan.jpg")
mac_face_encoding = face_recognition.face_encodings(mac_image)[0]

sherry_image = face_recognition.load_image_file("Mohan_Sherry.jpg")
sherry_face_encoding = face_recognition.face_encodings(sherry_image)[0]

goga_image = face_recognition.load_image_file("goga.jpg")
goga_face_encoding = face_recognition.face_encodings(goga_image)[0]

saira_image = face_recognition.load_image_file("saira_2.jpeg")
saira_face_encoding = face_recognition.face_encodings(saira_image)[0]

shreeram_image = face_recognition.load_image_file("shreeram.png")
shreeram_face_encoding = face_recognition.face_encodings(shreeram_image)[0]

urmila_image = face_recognition.load_image_file("urmila.png")
urmila_face_encoding = face_recognition.face_encodings(urmila_image)[0]

yunus_image = face_recognition.load_image_file("yunus.png")
yunus_face_encoding = face_recognition.face_encodings(yunus_image)[0]


known_faces = [
    amitabh_face_encoding,
    ashrani_face_encoding,
    sulakshana_face_encoding,
    vinod_face_encoding,
    mac_face_encoding,
    sherry_face_encoding,
    goga_face_encoding,
    saira_face_encoding,
    shreeram_face_encoding,
   urmila_face_encoding,
   yunus_face_encoding
]

# Initialize variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

vinod_frame = 0
amitabh_frame = 0
sulakshana_frame = 0
ashrani_frame = 0
mac_frame = 0
sherry_frame = 0
goga_frame = 0
saira_frame = 0
shreeram_frame = 0
urmila_frame = 0
yunus_frame = 0

while True:
    # Grab a single frame of video
	ret, frame = input_video.read()
	frame_number += 1

    # Quit when the input video file ends
	if not ret:
		break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
	rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
	face_locations = face_recognition.face_locations(rgb_frame)
	face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

	face_names = []
	for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
		match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

		name = None
		if match[0]:
			name = "amitabh"
			amitabh_frame +=1
		if match[1]:
			name = "ashrani"
			ashrani_frame +=1
		if match[2]:
			name = "sulakshana"
			sulakshana_frame +=1
		if match[3]:
			name = "vinod"
			vinod_frame = vinod_frame + 1
		if match[4]:
			name = "mac_mohan"
			mac_frame = mac_frame + 1
		if match[5]:
			name = "Sherry"
			sherry_frame = sherry_frame + 1
		if match[6]:
			name = "Goga"
			goga_frame = goga_frame + 1
		if match[7]:
			name = "Saira"
			saira_frame = saira_frame + 1
		if match[8]:
			name = "shreeram"
			shreeram_frame = shreeram_frame + 1
		if match[9]:
			name = "urmila"
			urmila_frame = urmila_frame + 1
		if match[10]:
			name = "yunus"
			yunus_frame = yunus_frame + 1
    #Append the detected names
		face_names.append(name)

    # Label the results

	for (top, right, bottom, left), name in zip(face_locations, face_names):
		if not name:
			continue

        # Draw a box around the face
		cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
		cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Write the resulting image to the output video file
	print("Writing frame {} / {}".format(frame_number, length))
	output_video.write(frame)


def ontime(frames):
	return(frames/25)
#Print the on screen time of each characters
print ("Estimates On-Screen  time of Vinod: %.2f seconds" % ontime(vinod_frame))
print ("Estimates On-Screen  time of Ashrani: %.2f seconds" % ontime(ashrani_frame))
print ("Estimates On-Screen  time of Sulakshana: %.2f seconds" % ontime(sulakshana_frame))
print ("Estimates On-Screen  time of Amitabh:  %.2f seconds" % ontime(amitabh_frame))
print ("Estimates On-Screen  time of Mac Mohan: %.2f seconds" % ontime(mac_frame))
print ("Estimates On-Screen  time of Mohan Sherry: %.2f seconds" % ontime(sherry_frame))
print ("Estimates On-Screen  time of Goga Kapoor: %.2f seconds" % ontime(goga_frame))
print ("Estimates On-Screen  time of Saira Banu:  %.2f seconds" % ontime(saira_frame))
print ("Estimates On-Screen  time of Shreeram: %.2f seconds" % ontime(shreeram_frame))
print ("Estimates On-Screen  time of Urmila: %.2f seconds" % ontime(urmila_frame))
print ("Estimates On-Screen  time of Yunus:  %.2f seconds" % ontime(yunus_frame))

input_video.release()
cv2.destroyAllWindows()
