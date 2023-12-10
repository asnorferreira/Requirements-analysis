from implementationClasses import *

presenceSystem = PresenceIdentificationSystem()
alertManager = AlertManager("1234-5678")
faceRecognition = FacialRecognitionSystem()

presenceSystem.detectPresence(1)
if presenceSystem.loggedEvents[-1]: 
    alertManager.sendAlert("Unusual activity detected", presenceSystem.loggedEvents[-1])

face = "image_data"
result = faceRecognition.recognizeFace(face)
if result:
    print("Face recognized.")
else:
    print("Unknown individual.")
