# import pytest

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
    
    
    
   