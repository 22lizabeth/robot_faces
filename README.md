# robotFaces
Facial Expressions and Animation Code for Sawyer Robot

Press a key to display a certain face. Continue to press the faces you wish to display and the code will continue to animate from face to face. Press the escape key when done.

**Keys:
  {'n': Neutral Face, 
  'h': Happy Face (not currently active), 
  'a': Angry Face, 
  's': Surprised Face, 
  'd': Sad Face, 
  'f': Afraid Face (not currently active), 
  'g': Disgusted Face (not currently active), 
  'c': Confused Face (not currently active)}


google text to speech
gcloud iam service-accounts create [NAME]
gcloud projects add-iam-policy-binding [PROJECT_ID] --member "serviceAccount:[NAME]@[PROJECT_ID].iam.gserviceaccount.com" --role "roles/owner"
gcloud iam service-accounts keys create [FILE_NAME].json --iam-account [NAME]@[PROJECT_ID].iam.gserviceaccount.com