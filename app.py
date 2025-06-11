from flask import Flask, render_template, request, jsonify
import random
import json
from datetime import datetime

app = Flask(__name__)

# Sample product database
products = [
    {"id": 1, "name": "Wireless Headphones", "price": 99.99, "category": "Electronics", "stock": 50},
    {"id": 2, "name": "Smart Watch", "price": 199.99, "category": "Electronics", "stock": 30},
    {"id": 3, "name": "Running Shoes", "price": 79.99, "category": "Sports", "stock": 100},
    {"id": 4, "name": "Coffee Maker", "price": 49.99, "category": "Home", "stock": 25},
    {"id": 5, "name": "Backpack", "price": 39.99, "category": "Fashion", "stock": 75}
]

# Sample order database
orders = [
    {"id": 1001, "customer": "John Doe", "products": [1, 3], "total": 179.98, "status": "Shipped", "date": "2023-05-15"},
    {"id": 1002, "customer": "Jane Smith", "products": [2, 4], "total": 249.98, "status": "Processing", "date": "2023-05-18"}
]

# Chatbot responses
greetings = ["Hello!", "Hi there!", "Greetings!", "Welcome!"]
goodbyes = ["Goodbye!", "See you later!", "Have a great day!", "Bye bye!"]

def get_bot_response(user_message):
    user_message = user_message.lower()
    
    # Greetings
    if any(word in user_message for word in ["hello", "hi", "hey"]):
        return random.choice(greetings) + " How can I assist you today?"
    
    # Goodbyes
    elif any(word in user_message for word in ["bye", "goodbye", "see you"]):
        return random.choice(goodbyes)
    
    # Products
    elif "product" in user_message or "item" in user_message or "buy" in user_message:
        return "Here are our featured products:\n" + "\n".join([f"{p['name']} - ${p['price']}" for p in products])
    
    # Specific product search
    elif "what is" in user_message or "tell me about" in user_message:
        for product in products:
            if product['name'].lower() in user_message:
                return f"{product['name']} is priced at ${product['price']}. We have {product['stock']} in stock."
        return "I couldn't find that product. Could you be more specific?"
    
    # Orders
    elif "order" in user_message or "purchase" in user_message:
        if "status" in user_message:
            return "Order statuses:\n" + "\n".join([f"Order #{o['id']}: {o['status']}" for o in orders])
        return "You can check your order status or browse products. What would you like to do?"
    
    # Shipping
    elif "shipping" in user_message or "delivery" in user_message:
        return "Standard shipping takes 3-5 business days. Express shipping is available for an additional fee."
    
    # Returns
    elif "return" in user_message or "refund" in user_message:
        return "We accept returns within 30 days of purchase. Please contact support with your order number."
    
    # Help
    elif "help" in user_message:
        return "I can help with:\n- Product information\n- Order status\n- Shipping details\n- Returns\nWhat do you need?"
    
    # Default response
    else:
        return "I'm not sure I understand. Could you rephrase that or ask about products, orders, shipping, or returns?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    
    # Simulate processing delay
    response = get_bot_response(user_message)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)