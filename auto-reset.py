# import statements
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime


# Initializing firebase realtime database
def initialize_db():
    # initializing the app
    cred = credentials.Certificate("./myman180-firebase-adminsdk-z56wz-51b050fa2a.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://myman180.firebaseio.com/'
    })

# Reset the timeslots
def reset_slots():
    # reading the data
    ref = db.reference('/haircut/shops/')
    data = ref.get()

    # data to update
    data_to_update =  [
                        {
                            "time": "8:00 AM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "8:30 AM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "9:00 AM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "9:30 AM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "10:00 AM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "10:30 AM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "11:00 AM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "11:30 AM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "12:00 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "12:30 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "1:00 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "1:30 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "2:00 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "2:30 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "3:00 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "3:30 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "4:00 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "4:30 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "5:00 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "5:30 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "6:00 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "6:30 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "7:00 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "7:30 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        },
                        {
                            "time": "8:00 PM",
                            "first": 0,
                            "second": 0,
                            "status": 0
                        }
                    ]

    # Resetting the timeSlots
    for i in data.keys():
        shop_ref = ref.child(i)
        temp = shop_ref.get()
        temp['timeSlots'] = data_to_update
        shop_ref.set(temp)
    



if (if __name__ == "__main__"):
    
    # Initialize the db
    initialize_db()

    while True:

        # check if the time is 00:00:00
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if(current_time == "00: 00: 00"):

            # reset the time slots
            reset_slots()