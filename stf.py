import pyrebase
import cv2
import argparse


# parser = argparse.ArgumentParser()
# parser.add_argument("-i", "--input", required=True, help="path to input image")
# args = vars(parser.parse_args())
config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "projectId": "",
  "storageBucket": "",
  "serviceAccount": "serviceAccountKey.json",
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
