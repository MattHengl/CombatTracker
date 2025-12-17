import datetime
import getpass
import json


config = json.load(open("config/config.json"))
path = config["config"]["log_path"]
filename_format = config["config"]["log_filename_format"]

date_str = datetime.datetime.now().strftime("%m-%d-%y")
filename = filename_format.format(
    user=getpass.getuser(),
    date=date_str
)

def log(text):
    with open(f'{path}{filename}', 'a') as f:
        f.write(f"{text}\n")