
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("seversAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-attendance-24dee-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name":"HEMANTH",
            "major":"robotics",
            "starting_year":2021,
            "total_attendance":6,
            "standing":"G",
            "year":3,
            "last_attendance_time":"2022-12-20 00:54:34"
        },
    "852741":
        {
            "name":"HARSHA",
            "major":"CYBER",
            "starting_year":2021,
            "total_attendance":8,
            "standing":"G",
            "year":3,
            "last_attendance_time":"2022-12-20 04:54:34"
        },
    "963852":
        {
            "name":"SOMESH",
            "major":"robotics",
            "starting_year":2022,
            "total_attendance":4,
            "standing":"G",
            "year":2,
            "last_attendance_time":"2022-12-20 06:54:34"
        }

}

for key,value in data.items():
    ref.child(key).set(value)
