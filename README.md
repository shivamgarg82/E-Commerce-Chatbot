# E-Commerce Chatbot

A simple Flask-based e-commerce chatbot that helps users with product inquiries, order status, shipping information, and returns.

![Screenshot 2025-06-11 152648](https://github.com/user-attachments/assets/6c50b38e-f8e2-4f8c-a17c-1c2c2ec4f8b8)

 
## Features

- Interactive chat interface with typing indicators
- Quick reply buttons for common queries
- Product database with search functionality
- Order status tracking
- Shipping and returns information
- Responsive design

## Technologies Used

- Python (Flask) - Backend server
- HTML/CSS - Frontend interface
- JavaScript - Chat functionality
- REST API - Communication between frontend and backend

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ecommerce-chatbot.git
   cd ecommerce-chatbot
Create a virtual environment (recommended):

bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
pip install flask
Run the application:

bash
python app.py
Open your browser and visit:

text
http://localhost:5000
Project Structure
text
ecommerce-chatbot/
├── app.py                # Flask application
├── static/
│   ├── css/
│   │   └── style.css     # Stylesheet
│   └── js/
│       └── script.js     # JavaScript for chat functionality
├── templates/
│   └── index.html        # Main HTML page
└── README.md             # This file
API Endpoints
GET / - Main chat interface

POST /chat - Process chat messages (expects JSON with message field)

Customization
To modify the chatbot responses, edit the get_bot_response() function in app.py. You can:

Add more products to the products list

Add more order examples to the orders list

Extend the response logic for different user queries

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
MIT
