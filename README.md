# 🛒 Basic E-Commerce Backend

This is a simple e-commerce backend built using Django & DRF with Stripe integration and JWT auth via Djoser+Simple-JWT.

## Features

- ✅ Product CRUD API
    - Admins ➝ can create, update, delete products
    - Authenticated users ➝ can view products and place orders (checkout)
    - Unauthenticated users ➝ can view products (read-only)
- ✅ JWT-based user registration, login & logout via Djoser
- ✅ Custom user model using `email` as login
- ✅ Stripe Checkout integration (returns session URL)
- ✅ Swagger UI for API documentation

## Tech Stack

- Django, Django REST Framework
- Djoser + SimpleJWT for auth API Generation
- Stripe for payment
- drf_yasg for Swagger API Documentation


# 📄 API Docs (Swagger)
You can use the built-in Swagger UI for testing all endpoints:

```bash
http://localhost:8000/api/docs  #Swagger UI

or

http://localhost:8000/api/redoc # ReDoc UI 

```
Usage:
Click "Authorize" and paste your JWT access token (Bearer <token>)

Use the endpoints directly: register, login, checkout, etc.

# 📍Naming Conventions

All Django apps are named using the format:

```
app_<feature>
```
Examples:

app_users: handles authentication and user logic.

app_products: manages product listing and checkout logic.




# 🔐API Usage

### Register
`POST /api/auth/users/`
```json
{
  "email": "test@mail.com",
  "full_name": "Test User",
  "password": "yourpass123",
  "re_password": "yourpass123"
}
```

### Login (JWT)
`POST /api/auth/jwt/create/`

```json
{
  "email": "test@mail.com",
  "password": "yourpass123"
}
```

### Create Checkout Session (JWT required)
`POST /api/create-checkout-session/`

```json
{
  "product_id": 1
}
```

### Product CRUD
`GET /api/products/`

`POST /api/products/ (admin only)`
```json
{
  "name": "Product Name",
  "description": "Product Description",
  "price": "10",
  "stock": 2
}
```
`GET /api/products/{id}`

`PUT /api/products/{id}`

`PATCH /api/products/{id}`

`DELETE /api/products/{id}`


# Required Enviroment Variables
- `STRIPE_SECRET_KEY` - stripe test key

# ⚙️Setup & Run
### ✅ Clone the repository
```git clone https://github.com/shemanto27/ecommerce.git```

```cd ecommerce```  

### ✅ Install dependencies using uv
```uv sync```

### ✅ Activate Virtual Environment
```source .venv/bin/activate```

### ✅ Apply migrations
```python manage.py migrate```

### ✅ Run the development server
```python manage.py runserver```

### ✅ create superuser to add/delete/update products
```python manage.py createsuperuser```

### ✅ Go to Swagger api url for live testing
```http://localhost:8000/api/docs/ ```

`create user` --> `login/generate token` --> `Authorize` --> `checkout session `

# ℹ️Note:
- This project uses uv (a fast, modern Python package manager). To install dependencies, run uv sync — no need for pip or requirements.txt.
- Stripe keys are in test mode.
- Project is modular and clean for easy scaling.