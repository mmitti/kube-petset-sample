import json
import falcon
import time
from data import Data

data = Data("/db/dat.json")

class Info(object):
    def on_get(self, req, res):
        res.body = json.dumps(data.get_info())

class GetData(object):
    def on_get(self, req, res):
        res.body = json.dumps(data.get_data())

class AddData(object):
     def on_post(self, req, res):
        body = req.stream.read().decode('utf-8')
        print(body)
        dat = json.loads(body)
        data.add_data(dat["text"], dat["host"])
        res.body = "OK"

app = falcon.API()
app.add_route("/info", Info())
app.add_route("/get", GetData())
app.add_route("/add", AddData())

if __name__ == "__main__":
	from wsgiref import simple_server
	httpd = simple_server.make_server("0.0.0.0", 8000, app)
	httpd.serve_forever()
