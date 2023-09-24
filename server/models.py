from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin




db= SQLAlchemy()


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = "restaurants"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    address =db.Column(db.String)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at= db.Column(db.DateTime, onupdate=db.func.now())
    
    restaurant_pizzas = db.relationship("RestaurantPizza", backref="restaurants")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            # 'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None,
            # 'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None
        }
        
        
    @validates('name')
    def name_validate(self, key, name):
        if name is None or name.strip()=="":   
            raise ValueError("name is required") 
        
        if len(name) > 50:
            raise ValueError("Name is is too long")
        
        if name and Restaurant.query.filter_by(name=name).first():
            raise ValueError("Name already exists")
        return name
            
    
    
    def __repr__(self):
        return f'{self.name}, {self.address}'  


class Pizza(db.Model, SerializerMixin):
    __tablename__ = "pizzas"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    ingredients= db.Column(db.String)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at= db.Column(db.DateTime, onupdate=db.func.now())
    
    restaurant_pizzas = db.relationship("RestaurantPizza", backref="pizzas")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients,
            # 'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None,
            # 'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None
        }
    
    def __repr__(self):
        return f'<Pizza {self.name}, created at {self.created_at}.>'
    

class RestaurantPizza(db.Model, SerializerMixin):  
    id = db.Column(db.Integer, primary_key = True)
    price= db.Column(db.Integer, nullable=False)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at= db.Column(db.DateTime, onupdate=db.func.now())
    
    pizza_id= db.Column(db.Integer, db.ForeignKey("pizzas.id"))
    
    restaurants_id= db.Column(db.Integer, db.ForeignKey("restaurants.id"))
    
    def to_dict(self):
        return {
            'id': self.id,
            'pizza_id': self.pizza_id,
            'restaurants_id': self.restaurants_id,
        }
        
    @validates('price')
    def validate_category(self, key, price):   
        price = int(price)   
        if price >= 1 and price <= 30: 
            return price
        else:        
            raise ValueError("Price should be between 1 and 30.")
        
    
    
    def __repr__(self):
        return f'{self.price}, {self.created_at}'
    
    
    
    



 
