import pyrebase

config = {
    "apiKey": "AIzaSyAwY0KnyKEry3Yar05IByR2k1u2Rc5Hsyo",
    "authDomain": "curso-e968f.firebaseapp.com",
    "databaseURL": "https://curso-e968f.firebaseio.com",
    "projectId": "curso-e968f",
    "storageBucket": "",
    "messagingSenderId": "734618974291",
    "appId": "1:734618974291:web:8c20f1aac659b862"
}

firebase = pyrebase.initialize_app(config)
db1 = firebase.database()
