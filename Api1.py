from flask import Flask, jsonify, request
from insultgenerator import phrases

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def home():
    if(request.method == "GET"):
        data = 'hello world'
        return jsonify({'data':data})

@app.route("/home/<string:Name>",methods = ["GET"])
def disp(Name):
     hi = phrases.get_so_insult_with_action_and_target(Name,Name + "'s mom")
     return jsonify({'data':hi})

if __name__ == "__main__":
    app.run(debug = True)