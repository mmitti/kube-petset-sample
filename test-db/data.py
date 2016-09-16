import json
from socket import gethostname
import time
import os.path
class Data:
    def save(self):
        f = open(self.path, "w")
        f.write(json.dumps(self.data))
        f.close()

    def __init__(self, path):

        self.path = path
        if os.path.exists(path):
            f = open(self.path, "r")
            self.data = json.loads(f.read())
            f.close()
        else:
            self.data = {
                "info":{
                    "init_host":gethostname(),
                    "init_time":time.ctime()
                },
                "data":[]
            }
            self.save()

    def get_info(self):
        dat = self.data["info"]
        dat["current_host"] = gethostname()
        dat["time"] = time.ctime()
        return dat

    def get_data(self):
        return self.data["data"]

    def add_data(self, text, api):
        self.data["data"].append({
            "dbhost":gethostname(),
            "apihost":api,
            "data":text,
            "time":time.ctime()
        })
        self.save()
