from flask import Flask, jsonify

app = Flask(__name__)

class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return self.name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
    
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        return self.Coffee()

@app.route('/intern1/<name>', methods=['GET'])
def get_intern(name):
    intern = Intern(name if name != "default" else "My name? I’m nobody, an intern, I have no name.")
    return jsonify({"name": str(intern)})

@app.route('/intern1/<name>/coffee', methods=['GET'])
def get_coffee(name):
    intern = Intern(name if name != "default" else "My name? I’m nobody, an intern, I have no name.")
    return jsonify({"coffee": str(intern.make_coffee())})

@app.route('/intern1/<name>/work', methods=['GET'])
def get_work(name):
    intern = Intern(name if name != "default" else "My name? I’m nobody, an intern, I have no name.")
    try:
        intern.work()
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

