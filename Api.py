from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/user/<name>")  # Daynamic routing
def get_user(name):
    Userdata ={
        "get-id":name,
        "Name":"Charles",
        "Email":"charlesbkoffical@gmail.com"      
    }

    moon= request.args.get("moon")
    if moon:
        Userdata["moon"] = moon

    return jsonify(Userdata), 200


# GET =  Request data from a specified resource
# POST = Create a resource
# PUT = Update a resource
# DELETE = Delete a resource

@app.route("/create-user",methods=["POST"])
def create():
    data = request.get_json()   

    return jsonify(data),201


if __name__ == '__main__':
    app.run(debug=True)
