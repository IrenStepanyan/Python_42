from flask import Flask, render_template

app = Flask(__name__)

class Intern:
	def _init_(self, name):
		self.name = name

	def work(self):
		return self.name
	

@app.route('/', methods=['GET'])
def get_intern():
	return render_template("index.html", name="Erik")
#@app.route('/intern/<name>/coffee', methods=['GET'])
if __name__ == "__main__":
    app.run()
