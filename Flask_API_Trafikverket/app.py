from flask import Flask, request, jsonify
from models import db
from services import UserService, CarService

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trafikverket.db'
# Below, I used an absolute path to create the database in a specific folder since the above path did not work
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trafikverket.db_final_home_assignment/exercise_4/instance/trafikverket.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) 

# below I check the current working directory and the database URI because I had some issues with the database path
# print("Current working directory:", os.getcwd())
# print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])

@app.route('/users/', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return jsonify(UserService.get_all_users()), 200
    elif request.method == 'POST':
        return jsonify(UserService.create_user(request.json)), 201

@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE']) 
def user(user_id):
    if request.method == 'GET':
        user = UserService.get_user_by_id(user_id)
        if user:
            return jsonify(user), 200
        return jsonify({"error": "User not found"}), 404

    elif request.method == 'PUT':
        return jsonify(UserService.update_user(user_id, request.json)), 200

    elif request.method == 'PATCH':
        return jsonify(UserService.update_user(user_id, request.json)), 200

    elif request.method == 'DELETE':
        if UserService.delete_user(user_id):
            return '', 204
        return jsonify({"error": "User not found"}), 404

@app.route('/cars/', methods=['GET', 'POST'])
def cars():
    if request.method == 'GET':
        return jsonify(CarService.get_all_cars()), 200
    elif request.method == 'POST':
        return jsonify(CarService.create_car(request.json)), 201

@app.route('/cars/<int:car_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def car(car_id):
    if request.method == 'GET':
        car = CarService.get_car_by_id(car_id)
        if car:
            return jsonify(car), 200
        return jsonify({"error": "Car not found"}), 404

    elif request.method == 'PUT':
        return jsonify(CarService.update_car(car_id, request.json)), 200

    elif request.method == 'PATCH':
        return jsonify(CarService.update_car(car_id, {k: v for k, v in request.json.items() if v is not None})), 200 # {k: v for k, v in request.json.items() if v is not None} är en dictionary comprehension som tar bort nycklar med värde None från request.json

    elif request.method == 'DELETE':
        if CarService.delete_car(car_id):
            return '', 204
        return jsonify({"error": "Car not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
