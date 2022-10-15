import pyrebase
import cv2
import argparse


# parser = argparse.ArgumentParser()
# parser.add_argument("-i", "--input", required=True, help="path to input image")
# args = vars(parser.parse_args())
config = {
  "apiKey": "AIzaSyCCHb56XahmBYrbSh_jR1dhogZyav6muKg",
  "authDomain": "project-cab30.firebaseapp.com",
  "databaseURL": "https://project-cab30-default-rtdb.firebaseio.com",
  "projectId": "project-cab30",
  "storageBucket": "project-cab30.appspot.com",
  "serviceAccount": "serviceAccountKey.json",
  # "messagingSenderId": "903723741684",
  # "appId": "1:903723741684:web:240274745bb432ffbe09a1",
  # "measurementId": "G-KQ928CZK2W"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def main(name , outgoingImage):
    try:
      storage.child(str("OutgoingImages/{}").format(name)).put(outgoingImage)
    except:
      print('Error')



if __name__ == "__main__":
    main()
