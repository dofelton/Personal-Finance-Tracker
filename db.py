# Handle all Firestore interactions
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# credentials are automatically created
cred = credentials.Certificate("sdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

