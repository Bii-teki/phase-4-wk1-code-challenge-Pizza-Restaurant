import pytest
from sqlalchemy.exc import IntegrityError

from unittest import TestCase
import json

from models import db, Restaurant, RestaurantPizza, Pizza

from app import app

class TestPizza(TestCase):
    
    def test_index(self):
        '''Test if Application is running'''
        tester = app.test_client(self)
        response = tester.get("/")
        assert(response.status_code == 200)
        self.assertTrue(True)
        
    def test_pizza_by_id(self):
        '''Test fetching Pizza by ID'''
        tester = app.test_client(self)
        response =tester.get('/pizzas/5')
        assert(response.status_code == 200)
        self.assertTrue(True)
        
        
    def test_all_restaurants(self):
        '''Test fetching all Restaurant by '''
        tester = app.test_client(self) 
        response = tester.get("/restaurants")  
        assert response.status_code == 200
        self.assertTrue(True)
    
    def test_delete_pizza_by_id(self):
        with app.app_context():
            
            client= app.test_client()
            pizza = Pizza(
                name="Test Pizza",
                ingredients="Test ingredients",
            )
            db.session.add(pizza)
            db.session.commit()
            response = client.delete(f'/pizzas/{pizza.id}')
            self.assertEqual(response.status_code, 200)
            expected_message = {"message": "record successfully deleted"}
            actual_message = response.get_json()
            self.assertEqual(actual_message, expected_message)
            deleted_pizza = Pizza.query.get(pizza.id)
            self.assertIsNone(deleted_pizza)
                
            
    def test_requires_name(self):
        '''Requires each record to have a name.'''
        with app.app_context():
            with pytest.raises(ValueError):
                restaurant = Restaurant(name='', address="Ingredients 1")
                db.session.add(restaurant)
                db.session.commit()
   
    def test_unique_name(self):
        '''Requires each name to be unique'''
        with app.app_context():
            with pytest.raises(ValueError):
                name_a= Restaurant(name='ingredients', address="Ingredients 1")
                name_b= Restaurant(name='ingredients', address="Ingredients 1")
                db.session.add(name_a)
                db.session.add(name_b)
                db.session.commit()
                db.session.query(Restaurant).delete()
                db.session.commit()
                assert False, "Name already exists"
    
   