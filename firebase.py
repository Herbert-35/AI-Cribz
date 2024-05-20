import pyrebase
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
