import pickle
from pathlib import path

import streamlit_authenticator as stauth

names = ["amir", "dr azim"]
usernames= ["amir", "drazim"]
passwords = ["abc123", "def456"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
