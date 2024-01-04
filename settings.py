import os

# data folder in appdata or same dir as this file
if os.environ.get("APPDATA"):
    data_folder = os.path.join(os.environ.get("APPDATA"), "JARVIS")
else:
    data_folder = os.path.join(os.path.dirname(__file__), "data")

database_file = os.path.join(data_folder, "database.db")
temp_folder = os.path.join(data_folder, "temp")
full_path_to_vosk_model = "vosk_model/vosk-model-en-us-daanzu-20200905-lgraph"


os.makedirs(data_folder, exist_ok=True)
os.makedirs(temp_folder, exist_ok=True)
