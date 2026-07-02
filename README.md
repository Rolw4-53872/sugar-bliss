![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.2-black)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.44-red)
![License](https://img.shields.io/badge/License-MIT-green)

# Sugar Bliss

Sugar Bliss is a full-stack Flask web application for an online desserts and sweets shop.
Customers can browse the product catalog, place custom orders (product, quantity, sweetness
level, extras, and pickup/delivery details), and the shop owner can review every order through
a built-in admin dashboard.

The interface is fully in Arabic (RTL) and built with Bootstrap 5.

* * *

## Project Overview

- **Type:** Full-stack web application (server-rendered)
- **Domain:** E-commerce / online ordering for a desserts business
- **Backend:** Flask + Flask-SQLAlchemy + Flask-Admin
- **Frontend:** Jinja2 templates, Bootstrap 5, custom CSS/JS
- **Database:** SQLite (`instance/cake.db`, created automatically on first run)

## Features

- Public storefront with home, "About Us", and product catalog pages
- Order form with:
  - Product selection with live pricing
  - Quantity, sweetness level (1–5), and add-ons (cream, chocolate sauce, extra nuts)
  - Delivery or in-store pickup, with date/time selection for pickup
- Server-side order total calculation (product price + extras + delivery fee)
- Order confirmation page summarizing the submitted order
- Public order history page (`/orders`) listing all submitted orders
- Admin dashboard (`/admin`) powered by Flask-Admin for managing orders (view/edit/delete)

## Tech Stack

| Layer          | Technology                          |
|----------------|--------------------------------------|
| Language       | Python 3                             |
| Web framework  | Flask 3.1                            |
| ORM            | Flask-SQLAlchemy / SQLAlchemy 2.0    |
| Admin panel    | Flask-Admin                          |
| Database       | SQLite                               |
| Frontend       | Bootstrap 5, HTML/CSS/JS, Font Awesome |
| Templating     | Jinja2                               |

## Project Structure

```
sugar-bliss/
├── application.py        # Flask app, routes, pricing logic, order calculation
├── database.py            # SQLAlchemy models (Order)
├── requirements.txt        # Python dependencies
├── static/
│   ├── all.css / stye.css  # Custom styles
│   ├── all.js               # Custom scripts
│   ├── bootstrap*.js        # Bootstrap bundle
│   └── images/               # Product and site images
├── templates/
│   ├── index.html            # Home page
│   ├── hht.html               # About us
│   ├── mine.html               # Products
│   ├── order.html               # Order form
│   ├── confirmation.html         # Order confirmation
│   └── orders.html                # Order history
└── instance/
    └── cake.db                    # SQLite database (auto-generated, git-ignored)
```

## How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/Rolw4-53872/sugar-bliss.git
   cd sugar-bliss
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python application.py
   ```

5. Open your browser at **http://127.0.0.1:5000**

   The SQLite database is created automatically on first run. The admin dashboard is
   available at **http://127.0.0.1:5000/admin**.

## Data Model

The application stores every order in a single `orders` table (`database.py`):

| Field            | Type    | Description                              |
|-------------------|---------|-------------------------------------------|
| id                 | Integer | Primary key                               |
| name               | String  | Customer name                             |
| phone / email      | String  | Contact details                           |
| address            | String  | Delivery address (if applicable)          |
| product            | String  | Selected product name                     |
| quantity           | Integer | Number of items                           |
| sweetness          | Integer | Sweetness level (1–5)                     |
| extras             | String  | Comma-separated list of add-ons           |
| delivery_method    | String  | `delivery` or `pickup`                    |
| total              | Float   | Final calculated total                    |

## License

This project is licensed under the [MIT License](LICENSE).

## Author

**Rolw4-53872** — [github.com/Rolw4-53872](https://github.com/Rolw4-53872)
