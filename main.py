from flask import Flask
import etcd
import os


etcd_client = etcd.Client(
	host=os.getenv("ETCD_HOST"), 
	port=int(os.getenv("ETCD_PORT")))

app = Flask(__name__)

@app.route('/')
def hello():
	key = "foo"
	foo = None
	try:
		foo = etcd_client.get(key).value
	except etcd.EtcdKeyNotFound:
		print(f"key {foo} not found")
	if foo is None:
		etcd_client.set("foo",1)
		foo=1
	else:
		new_foo = int(foo)+1
		etcd_client.set("foo",new_foo)
	return f'foo is {foo}'

if __name__ == '__main__':
		app.run(port=8000)