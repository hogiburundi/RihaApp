import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

apps_dir_str = "apps"

APPS_DIR = os.path.join(BASE_DIR, apps_dir_str)

for app in os.listdir(APPS_DIR):
	print(app)