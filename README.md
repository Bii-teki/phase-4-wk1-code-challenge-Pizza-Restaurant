# Week 1 Code Challenge - Flask Pizza Restaurant API

## Author 
Geoffrey Kipngeno Bii

## Table of Contents
- [Overview](#overview)
- [Deliverables](#deliverables)
  - [Models and Migrations](#models-and-migrations)
  - [Validations](#validations)
  - [Routes](#routes)
  - [Testing](#testing)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


Welcome to the Week 1 Code Challenge where you will be building a Flask API for managing pizza restaurants and their pizzas. Below are the instructions and deliverables for this challenge.
# Overview

Your task is to build a Flask API that handles pizza restaurant data. The API will involve managing restaurants, pizzas, and their relationships. Make sure to follow the guidelines and requirements mentioned below.
Deliverables

# Models and Migrations:
## Create models and migrations for the following database tables based on the provided domain description:
- Restaurant
- Pizza
- RestaurantPizza (to manage the many-to-many relationship)

# Validations

**RestaurantPizza Model:**

- Must have a price between 1 and 30.

**Restaurant Model:**

- Must have a name less than 50 words in length.
- Must have a unique name.


# Routes:
Implement the following routes as specified in the domain description:

- GET /restaurants
- GET /restaurants/:id
- DELETE /restaurants/:id
- GET /pizzas
- POST /restaurant_pizzas


# Testing:
        Test the implemented endpoints using Postman and ensure they function as specified.

## Getting Started

### Prerequisites:
- Python
- Flask
- SQLAlchemy

### Installation:
- Clone this repository.
- Install the necessary dependencies using pip or your package manager of choice.
- Run the Flask server.

## Usage

Follow the guidelines in the domain description to use the API effectively. Use Postman or a similar tool to test the implemented endpoints. Also  you can visit https://restaurants-pizzas-prky.onrender.com/
Contributing

If you'd like to contribute to this project, please follow the standard GitHub flow: fork, make your changes, and create a pull request.
License

## This project is licensed under the MIT License.


### Copyright (c) 2023 Geoffrey BII

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.