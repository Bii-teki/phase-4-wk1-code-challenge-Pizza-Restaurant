from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Restaurant, Pizza, RestaurantPizza
from flask import jsonify
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_rest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Index(Resource):
    def get(self):
        response_dict = {
            "index": "Welcome to the Pizza Restaurant RESTful API",
        }
        return jsonify(response_dict)

api.add_resource(Index, '/')

class RestaurantResource(Resource):
  
    def get(self):
        restaurants = [restaurant.to_dict() for restaurant in Restaurant.query.all()]
        return jsonify({'restaurants': restaurants})
    
    def post(self):
        try:
            data = request.get_json()
            new_restaurant = Restaurant(
                name=data['name'],
                address=data['address']
            )

            db.session.add(new_restaurant)
            db.session.commit()

            return jsonify(new_restaurant.to_dict()), 201

        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
        

api.add_resource(RestaurantResource, '/restaurants')


class RestaurantByID(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first().to_dict()
        if restaurant is None:
            response_body = {"error": "Restaurant not found"}
            return make_response(jsonify(response_body), 404)
        return make_response(jsonify(restaurant), 201)
    def delete(self, id):
        record = Restaurant.query.filter_by(id=id).first()
        if record is None:
            response_body = {"error": "Restaurant not found"}
            return make_response(jsonify(response_body), 404)
        
        db.session.delete(record)
        db.session.commit()
                
        response_dict = {"message": "Restaurant successfully deleted"}

        response = make_response(jsonify(response_dict), 200)

        return response
    
    
api.add_resource(RestaurantByID, '/restaurants/<int:id>')    
    




class PizzaResource(Resource):
    def get(self):
        pizzas = [pizza.to_dict() for pizza in Restaurant.query.all()]
        return jsonify({'pizzas': pizzas})

    def post(self):
        data = request.get_json()

        new_pizza = Pizza(
            name=data['name'],
            ingredients=data['ingredients'],
        )

        db.session.add(new_pizza)
        db.session.commit()

        return make_response(new_pizza.to_dict(), 201)


api.add_resource(PizzaResource, '/pizzas')

class PizzaByID(Resource):

    def get(self, id):
        record = Pizza.query.filter_by(id=id).first().to_dict()
        return make_response(jsonify(record), 200)



    def patch(self, id):
        record = Pizza.query.filter(Pizza.id == id).first()
        for attr in request.get_json():
            setattr(record, attr, request.get_json()[attr])

        db.session.add(record)
        db.session.commit()

        response_dict = record.to_dict()

        response = make_response(response_dict, 200)
        return response


        
        

    def delete(self, id):

        record = Pizza.query.filter_by(id=id).first()

        db.session.delete(record)
        db.session.commit()

        response_dict = {"message": "record successfully deleted"}

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response
    
api.add_resource(PizzaByID, '/pizzas/<int:id>')    
    
class  RestaurantPizzaResource(Resource):
    def get(self):          
        restpizza = [pizza.to_dict() for pizza in RestaurantPizza.query.all()]
        return jsonify({'pizzas': restpizza})
    
    
    def post(self):
        data=request.get_json()
        
       
        restaurant_ids = [restaurant.id for restaurant in Restaurant.query.all()]
        pizza_ids = [pizza.id for pizza in Pizza.query.all()]
        
        if not restaurant_ids or not pizza_ids:
            return {"error": "No restaurants or pizzas available"}, 400
        
        
        restaurant_id = random.choice(restaurant_ids)
        pizza_id = random.choice(pizza_ids)
        
        
        new_record = RestaurantPizza(
            price=data['price'],
            restaurants_id = restaurant_id,
            pizza_id = pizza_id,
            
        )

        db.session.add(new_record)
        db.session.commit()

        response_dict = new_record.to_dict()

        response = make_response(
            response_dict,
            201,
        )

        return response
    
    
    
api.add_resource(RestaurantPizzaResource, '/restaurantpizzas')    
           


if __name__ == "__main__":
    app.run(port=5550, debug=True)
