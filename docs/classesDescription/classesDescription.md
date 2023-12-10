# Berg Works Access Control System Class Description

## Class PresenceIdentificationSystem
### Attributes:
- `cameras`: List of security cameras.
- `registeredEvents`: List of recorded security events.

### Methods:
- `detectPresence(camera_id)`: Detects presence using the specified camera.
- `logEvent(event)`: Records a security event.

## Class AlertManager
### Attributes:
- `managerCellNumber`: Manager's cell phone number for alerting.
- `alertHistory`: History of sent alerts.

### Methods:
- `sendAlert(message, event)`: Sends an alert to the manager.

## Class FacialRecognitionSystem
### Attributes:
- `facialDataBank`: Database for storing facial data.
- `recognitionLog`: Record of facial recognition activities.

### Methods:
- `recognizeFace(image)`: Conducts facial recognition.
- `updateDataBank(user_id, image)`: Updates the database with new facial images.

## Class Door
### Attributes:
- `doorID`: Unique identifier of the door controlled by the system.

### Methods:
- `authorizeAccess(server)`: Determines if the door should be unlocked based on the server's authorization.

## Class Employee
### Attributes:
- `employeeName`: Name of the employee.
- `age`: Employee's age.
- `department`: Department where the employee works.

### Methods:
- Methods to be defined based on the system's interactions with employees.
