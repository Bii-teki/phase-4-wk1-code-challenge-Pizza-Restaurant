from models import db, Restaurant, RestaurantPizza, Pizza

from faker import Faker

import random

from app import app



with app.app_context():
    fake = Faker()
    
    db.drop_all()
    db.create_all()


    restaurants= []
    for i in range(20):
        restaurant = Restaurant(
            name = fake.unique.company(),
            address= fake.address()
        )        
        restaurants.append(restaurant)
        
    db.session.add_all(restaurants)
    db.session.commit()
    
    pizzas= []
    for i in range(20):
        pizza = Pizza(
            name = fake.unique.company(),
            ingredients= fake.address()
        )        
        pizzas.append(pizza)
        
    db.session.add_all(pizzas)
    db.session.commit()
    
    restaurant_pizza =[]
    for i in range(20):
        restaurant_pizzas = RestaurantPizza(
            price= random.randint(300, 1000),
            pizza_id = random.choice(pizzas).id,
            restaurants_id =random.choice(restaurants).id,
        )
        restaurant_pizza.append(restaurant_pizzas)
    
    db.session.add_all(restaurant_pizza) 
    db.session.commit()  
    
    
    
    
    
    
    
    
    
    
        

    





