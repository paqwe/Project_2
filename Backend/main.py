import random
from flask import Flask, request,jsonify
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
import pprint
load_dotenv(find_dotenv())


password = os.environ.get("MONGODB_PWD")
print(password)


connection_string = "mongodb+srv://abc:{password}@cluster1.hayb1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

# mongodb+srv://<db_username>:<db_password>@cluster1.hayb1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1

client = MongoClient(connection_string)


dbs = client.list_database_names()
print(dbs)

# print(client)





app=Flask(__name__)

# @app.route("/get-user/<cake_id>")
# def get_cake(cake_id):
#     user_data = {
#         "cake_id": cake_id,
#         "name":"chocolate cake",
#         "price": 299,
#     }

#     # extra = request.args.get("extra")
#     # if extra:
#     #     cake_data["extra"] = extra

#     # return jsonify(cake_data), 200


# @app.route("/create-cake",methods=["POST"])
# def create_cake():
#     data = request.get_json()

#     return jsonify(data),201



cakes = [
    {
        "id":1,
        "name":"chocochips",
        "price": 99,
    },

    {
        "id":2,
        "name":"Red velvet",
        "price": 89,
    },

    {
        "id":3,
        "name":"chocolava",
        "price": 99,
    }
]


@app.route("/cakes", methods=['GET'])
def get_cakes():
    return cakes


@app.route("/cakes/<int:cake_id>", methods=['GET'])
def get_cake(cake_id):
    for cake in cakes:
        if cake.get("id")=="cake_id":
            return cake,200
    return {'error':'cake not found'},404

@app.route("/cakes",methods=['POST'])
def create_cake():
    new_cake={"id":''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyz', k=4)),"name":request.json['name'],"price":request.json['price']}
    cakes.append(new_cake)
    return new_cake,201

@app.route("/cakes/<int:cake_id>",methods=['PUT'])
def update_cake(cake_id):
    for cake in cakes:
        if cake['id']==cake_id:
            cake['name']==request.json['name']
            cake['price']==request.json['price']
            return cake,201
    return {'error':'cake not found'},404

@app.route("/cakes/<int:cake_id>",methods=['DELETE'])
def delete_cake(cake_id):
    for cake in cakes:
        if cake['id']==cake_id:
            cakes.remove(cake)
            return {"data":"cake deleted successfully"},200
    return {'error':'cake not found'},404
        

@app.route("/cakes/<int:cake_id>",methods=['PATCH'])
def updateValue_cake(cake_id):
    for cake in cakes:
        if cake['id']==cake_id:
            cake['name']==request.json['name']
            cake['price']==request.json['price']
            return cake
    return {'error':'cake not found'},404

        









if __name__ == "__main__":
    app.run(debug=True)