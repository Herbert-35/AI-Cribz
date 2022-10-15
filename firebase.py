import pyrebase
config = {
  "apiKey": "AIzaSyCCHb56XahmBYrbSh_jR1dhogZyav6muKg",
  "authDomain": "project-cab30.firebaseapp.com",
  "databaseURL": "https://project-cab30-default-rtdb.firebaseio.com",
  "projectId": "project-cab30",
  "storageBucket": "project-cab30.appspot.com",
  "serviceAccount": "serviceAccountKey.json",
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


#UPLOAD
def main(outgoingImage):
    try:
      # print(args["input"])
      # print(outgoingfile)
      storage.child(outgoingImage).put(outgoingImage)
    except:
      print('Error')



if __name__ == "__main__":
    main()
