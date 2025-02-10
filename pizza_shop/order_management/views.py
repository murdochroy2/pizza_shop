from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import random
import json

# Create your views here.
class MenuView(APIView):
    menu = [ 
        {"id": 1, "name": "Margherita", "size": "Medium", "price": 8.99, "toppings": ["tomato sauce", "mozzarella", "basil"]}, {"id": 2, "name": "Pepperoni", "size": "Medium", "price": 9.99, "toppings": ["tomato sauce", "mozzarella", "pepperoni"]}, {"id": 3, "name": "Vegetarian", "size": "Medium", "price": 10.99, "toppings": ["tomato sauce", "mozzarella", "bell peppers", "onions", "mushrooms"]}, {"id": 4, "name": "Hawaiian", "size": "Medium", "price": 11.99, "toppings": ["tomato sauce", "mozzarella", "ham", "pineapple"]}, {"id": 5, "name": "BBQ Chicken", "size": "Medium", "price": 12.99, "toppings": ["BBQ sauce", "mozzarella", "grilled chicken", "red onions"]}, {"id": 6, "name": "Cheese", "size": "Medium", "price": 9.99, "toppings": ["tomato sauce", "mozzarella"]}, {"id": 7, "name": "Mushroom", "size": "Medium", "price": 10.99, "toppings": ["tomato sauce", "mozzarella", "mushrooms"]}, {"id": 8, "name": "Spinach and Feta", "size": "Medium", "price": 11.99, "toppings": ["tomato sauce", "mozzarella", "spinach", "feta cheese"]}, {"id": 9, "name": "Meat Lover's", "size": "Medium", "price": 12.99, "toppings": ["tomato sauce", "mozzarella", "pepperoni", "sausage", "ham", "bacon"]}, {"id": 10, "name": "Buffalo Chicken", "size": "Medium", "price": 13.99, "toppings": ["Buffalo sauce", "mozzarella", "grilled chicken", "red onions", "blue cheese"]}, ]
    
    def get(self, request):
        name_of_pizza = request.query_params.get("name")
        item_details = None

        if name_of_pizza:
            for item in self.menu:
                if item.get("name") == name_of_pizza:
                    item_details = item


        return Response(data=item_details)
    
class OrderView(APIView):
    menu = [ 
        {"id": 1, "name": "Margherita", "size": "Medium", "price": 8.99, "toppings": ["tomato sauce", "mozzarella", "basil"]}, {"id": 2, "name": "Pepperoni", "size": "Medium", "price": 9.99, "toppings": ["tomato sauce", "mozzarella", "pepperoni"]}, {"id": 3, "name": "Vegetarian", "size": "Medium", "price": 10.99, "toppings": ["tomato sauce", "mozzarella", "bell peppers", "onions", "mushrooms"]}, {"id": 4, "name": "Hawaiian", "size": "Medium", "price": 11.99, "toppings": ["tomato sauce", "mozzarella", "ham", "pineapple"]}, {"id": 5, "name": "BBQ Chicken", "size": "Medium", "price": 12.99, "toppings": ["BBQ sauce", "mozzarella", "grilled chicken", "red onions"]}, {"id": 6, "name": "Cheese", "size": "Medium", "price": 9.99, "toppings": ["tomato sauce", "mozzarella"]}, {"id": 7, "name": "Mushroom", "size": "Medium", "price": 10.99, "toppings": ["tomato sauce", "mozzarella", "mushrooms"]}, {"id": 8, "name": "Spinach and Feta", "size": "Medium", "price": 11.99, "toppings": ["tomato sauce", "mozzarella", "spinach", "feta cheese"]}, {"id": 9, "name": "Meat Lover's", "size": "Medium", "price": 12.99, "toppings": ["tomato sauce", "mozzarella", "pepperoni", "sausage", "ham", "bacon"]}, {"id": 10, "name": "Buffalo Chicken", "size": "Medium", "price": 13.99, "toppings": ["Buffalo sauce", "mozzarella", "grilled chicken", "red onions", "blue cheese"]}, ]

    def post(self, request):
        order_details = self._get_request_body(request)
        print(order_details)        

        price_map = {item["id"]: item["price"] for item in self.menu}

        order_total = 0
        for item in order_details:
            item_price = price_map.get(item["id"])
            order_total += item_price
        
        order_id = random.randint(1, 12345)

        return Response(data={"price":order_total, "order_id": order_id})
            

    def _get_request_body(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        return body