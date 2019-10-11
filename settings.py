import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = False
HIDE_FIREFOX = True
def override_settings(MEDIA_URL, MEDIA_ROOT, DEFAULT_FILE_STORAGE):
    pass

