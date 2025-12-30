import datetime
import getpass
import json
import os
import sys

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
    log_base = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_base = base_path

config_path = os.path.join(base_path, "config", "config.json")
with open(config_path, 'r') as f:
    config = json.load(f)
log_path_from_config = config["config"]["log_path"]
if os.path.isabs(log_path_from_config):
    path = log_path_from_config
else:
    path = os.path.join(log_base, log_path_from_config)
filename_format = config["config"]["log_filename_format"]
date_str = datetime.datetime.now().strftime("%m-%d-%y")
filename = filename_format.format(
    user=getpass.getuser(),
    date=date_str
)

def log(text):
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, filename)
    with open(full_path, 'a') as f:
        f.write(f"{text}\n")