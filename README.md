# Django Online Shop

This project is an online shop built using Django, featuring product listing, shopping cart functionality, order management, payment processing via Stripe, and coupon discounts.

## Features

### Shop
- **Product Listing**: Browse through the list of available products by category.
- **Product Detail View**: View detailed information about a product, including recommendations for similar products.
- **Product Recommendations**: See recommended products based on the current product being viewed.

### Cart
- **Add to Cart**: Add products to the shopping cart with the option to specify quantity.
- **Remove from Cart**: Remove products from the cart.
- **Cart Overview**: View the cart details, update product quantities, and see recommended products based on cart contents.
- **Apply Coupon**: Apply discount coupons to the cart.

### Orders
- **Order Creation**: Create an order based on the contents of the cart, apply discounts, and save order details.
- **Order Confirmation**: After creating an order, proceed to payment.
- **Admin Order Management**: Admin users can view order details and generate order invoices in PDF format.

### Payments
- **Stripe Payment Processing**: Securely process payments through Stripe.
- **Payment Success**: View a confirmation page after successful payment.
- **Payment Cancellation**: View a cancellation page if the payment process is aborted.

### Coupons
- **Apply Coupons**: Users can apply coupon codes to receive discounts on their orders.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/TAnd-dev/django_ata_shop.git
    cd django_ata_shop
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (admin user):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Set up environment variables**

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8. **Access the application:**
    Open a web browser and go to `http://127.0.0.1:8000/`.

## Usage

### Shopping
1. **Browse Products**: Visit `/` to view the list of products.
2. **View Product Details**: Click on a product to see more details and recommendations.
3. **Add Products to Cart**: On the product detail page, select the quantity and add the product to your cart.
4. **View Cart**: Visit `/cart/` to see the items in your cart. You can update quantities or remove items.
5. **Apply Coupons**: Enter a coupon code in the cart view to apply a discount.
6. **Checkout**: Proceed to the checkout to create an order and process the payment.

### Admin
1. **Order Management**: Admins can log in to the admin panel at `/admin/` to manage orders and generate PDF invoices.
2. **Product Management**: Admins can add, edit, and delete products and categories.

## Payment Processing

The payment process is handled via Stripe. After creating an order, the user is redirected to a Stripe Checkout page to complete the payment. On success or cancellation, the user is redirected to the appropriate page.
