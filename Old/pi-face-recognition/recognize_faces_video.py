# USAGE

# import the necessary packages
from imutils.video import VideoStream
import face_recognition

import imutils
import pickle,mail,gsm
import time
import cv2

def start(name='nothing'):
	# load the known faces and embeddings
	print("[INFO] loading encodings...")
	data = pickle.loads(open("encodings.pickle", "rb").read())
	return(data)

def recognize(data):
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	writer = None
	#time.sleep(2.0)
	name=''
	# loop over frames from the video file stream
	i=1
	while i:
		# grab the frame from the threaded video stream
		frame = vs.read()
		start_time=time.time()
		cv2.imwrite("img.jpg",frame)
		# convert the input frame from BGR to RGB then resize it to have
		# a width of 750px (to speedup processing)
		rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		rgb = imutils.resize(frame, width=200)
		r = frame.shape[1] / float(rgb.shape[1])

		# detect the (x, y)-coordinates of the bounding boxes
		# corresponding to each face in the input frame, then compute
		# the facial embeddings for each face
		boxes = face_recognition.face_locations(rgb,
			model="hog")
		encodings = face_recognition.face_encodings(rgb, boxes)
		names = []

		# loop over the facial embeddings
		for encoding in encodings:
			# attempt to match each face in the input image to our known
			# encodings
			matches = face_recognition.compare_faces(data["encodings"],encoding,tolerance=0.45)
			name = "Unknown"
			
			# check to see if we have found a match
			if True in matches:
				# find the indexes of all matched faces then initialize a
				# dictionary to count the total number of times each face
				# was matched
				matchedIdxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}
				# loop over the matched indexes and maintain a count for
				# each recognized face face
				for i in matchedIdxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1

				# determine the recognized face with the largest number
				# of votes (note: in the event of an unlikely tie Python
				# will select first entry in the dictionary)
				name = max(counts, key=counts.get)
			
			#i=message.MsgApp(data=str(name))
			
			# update the list of names
			names.append(name)
			print(name)
			if name=="Unknown":
                                print name
                                mail.send_mail("robinratheya@gmail.com","googlechrome","robinrathaya@gmail.com","Unautherized person","img.jpg")
                                print "Call"
                                gsm.call("8122220022")
                        else:
                                mail.send_mail("robinratheya@gmail.com","googlechrome","robinrathaya@gmail.com","Unautherized person","img.jpg")
		# loop over the recognized faces
		for ((top, right, bottom, left), name) in zip(boxes, names):
			
			top = int(top * r)
			right = int(right * r)
			bottom = int(bottom * r)
			left = int(left * r)

			# draw the predicted face name on the image
			cv2.rectangle(frame, (left, top), (right, bottom),
				(0, 255, 0), 2)
			
			y = top - 15 if top - 15 > 15 else top + 15
			cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
				0.75, (0, 255, 0), 2)
		
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

			# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break
		end_time=time.time() 
		print(end_time-start_time)
	# do a bit of cleanup
	cv2.destroyAllWindows()
	vs.stop()

	# check to see if the video writer point needs to be released
	if writer is not None:
		writer.release()
	print("CLOSE")
if __name__=="__main__":
	data=start()
	print(recognize(data))
	
