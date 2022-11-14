import wiotp.sdk.device
import time
import os
import datetime
import random
myConfig = {
"identity": {
"orgId": "u9qhfi",
"typeId": "Devicetypel",
"deviceId": "DeviceID1"
},
"auth": {
"token": ")hSb7_ZD+evl2fRhXi"
} }
client = wiotp.sdk.device.DeviceClient (config=myConfig,logHandlers=None)
client.connect ()
def myCommandCallback (cmd) :
    print ("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if (m=="motoron"):
        print ("Motor is switched on")
    elif (m=="motoroff"):
        print ("Motor is switched OFF")
    print (" ")
while True:
    soil=random.randint (0,100)
    temp=random.randint (-20, 125)
    hum=random.randint (0, 100)
    myData={'soil moisture': soil, 'temperature':temp, 'humidity':hum}
    client.publishEvent (eventId="status", msgFormat="json", data=myData, qos=0 , onPublish=None)
    print ("Published data Successfully: %s", myData)
    time.sleep (2)
client.commandCallback = myCommandCallback
client.disconnect ()
