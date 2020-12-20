import serial
import matplotlib.pyplot as plt
import pyrebase


########## python file to Firebase############


config = {
  "apiKey": "apiKey",
  "authDomain": "https://accounts.google.com/o/oauth2/auth",
  "databaseURL": "https://udistance-test-default-rtdb.firebaseio.com/",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "C:\\Users\\Heta Shah\\PycharmProjects\\pythonProject\\UDistanceFirebase.json"

}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Get a reference to the database service
db = firebase.database()


# data = {"name": "Mortimer 'Morty' Smith"}
# db.child("users").child("Morty").set(data)
# db.child("users").child("Morty").update({"name": "Mortiest Morty"})

############ Arduino to Python ###################


plt.style.use('seaborn')

arduinoData = serial.Serial('COM3', 9600)  # Creating our serial object named arduinoData
arduinoData.flushInput()
print("Established serial connection to Arduino")

cnt = 0
b=0
r=0
try:
    while True:
        while (arduinoData.inWaiting() == 0):  # Wait here until there is data
            pass  # do nothing
        arduinobytes = arduinoData.readline()# read the line of text from the serial port
        arduinoStringraw = arduinobytes.decode("utf-8")
        arduinoString = arduinoStringraw.strip() # remove any spaces

        if arduinoString == "": # if it is an empty string then disregard
            continue
        else:
            rawdata = arduinoString.split(",") # split the data where there is the comma

            blue=int(rawdata[0][0]) # converts str into int for the first index
            red=int(rawdata[1][0]) # converts str into str for the second index

            if blue==5 and red==0:
                b = 1
                r = 0
            elif blue==0 and red==5:
                r = 1
                b = 0
            elif blue==5 and red ==5:
                if b == 1:
                    cnt = cnt+1
                    b = 0
                    r = 0

                elif r == 1:
                    cnt=cnt-1
                    r = 0
                    b = 0
            else:
                cnt=cnt
            if cnt < 0:
                cnt = 0
            print(cnt)

            db.child("ILC").update({"Population": cnt}) ##updates the database


finally:
    arduinoData.close()



