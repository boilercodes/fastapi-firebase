import logging
import sys

import firebase_admin
from firebase_admin import credentials, firestore

from app.core import settings

log = logging.getLogger(__name__)

__all__ = ["db"]

if "pytest" in sys.modules:
    # This is a pytest environment.
    # We need to mock the Firestore database.
    from mockfirestore import MockFirestore
    db = MockFirestore()
else:
    cred = credentials.Certificate({
        "type": "service_account",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "project_id": settings.firebase.project_id,
        "private_key": settings.firebase.private_key,
        "client_email": settings.firebase.client_email,
    })

    firebase_admin.initialize_app(cred)
    log.info("Initialized Firebase Admin SDK")

    # Initialize Cloud Firestore DB.
    db = firestore.client()
