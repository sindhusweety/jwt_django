# jwt_django
Json web token for login with username, password and  crud operations for bikes

1. cd jwt_django
2. source env/bin/activate
2. pip install -r requirements.txt
3. cd crudbike
3. python manage.py runserver 5000


**ENDPOINTS**

1. http://127.0.0.1:5000/api/register/     POST METHOD
   {"username": "testuser4", "password": "password123"}
2. http://127.0.0.1:5000/api/login/     POST METHOD
   {"username": "testuser2", "password": "password123"}
3. http://127.0.0.1:5000/api/bikes/   GET METHOD
4. http://127.0.0.1:5000/api/bikes/  POST METHOD
   {"name": "Hybrid Bike", "brand": "Specialized", "price": 900, "model":"ABC", "purchase_date":"2024-12-31"}
5. http://127.0.0.1:5000/api/bikes/1   GET METHOD
6. http://127.0.0.1:5000/api/bikes/1/ PUT METHOD
   {"id":1,"name": "Hybrid Bike", "brand": "Specialized", "price": 900, "model":"XYZ", "purchase_date":"2024-12-31"}
7. http://127.0.0.1:5000/api/bikes/6/ DETELE METHOD