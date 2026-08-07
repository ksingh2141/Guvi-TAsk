# Automated Testing of E-commerce Web Application

## SauceDemo E-commerce Automation Framework

---

## 1. Project Overview

This project is an automated testing framework developed for testing the demo e-commerce web application:

**Application Under Test:**  
https://www.saucedemo.com/

The objective of this project is to automate and validate the core functionalities of the SauceDemo e-commerce application, including:

- Login functionality
- Invalid login validation
- Logout functionality
- Cart validation
- Random product selection
- Adding products to the cart
- Cart product validation
- Checkout process
- Product sorting
- Reset App State functionality

The framework is designed using the **Page Object Model (POM)** with Selenium WebDriver and Pytest.

---

# 2. Project Objective

The primary objective of this project is to simulate real-world user behavior and validate the functionality of an e-commerce web application through automated tests.

The automation framework validates:

- Different user login scenarios
- Positive and negative test cases
- Product selection and data extraction
- Shopping cart operations
- Checkout workflow
- Dynamic UI behavior
- Product sorting
- Application state reset
- Order confirmation
- Product and price validation

---

# 3. Scope

The automation framework covers the following areas:

### Functional Testing

- Login
- Logout
- Product listing
- Cart
- Checkout
- Sorting
- Reset application state

### Data Validation

- Product names
- Product prices
- Cart item count
- Cart product details
- Checkout summary

### Dynamic Behavior

- Random product selection
- Dynamic waits
- Dynamic UI elements
- Menu interactions

### Reporting

- Pytest execution reports
- HTML test reports
- Execution logs
- Screenshots where applicable

---

# 4. Test Scenarios

The project contains **10 test scenarios** as specified in the assignment.

---

## TC1 - Login with Various Predefined Users

### Scenario

Login using different predefined SauceDemo users.

### Users Covered

Examples include:

- standard_user
- performance_glitch_user
- locked_out_user
- problem_user
- visual_user

### Validation

The test verifies whether each user's login behavior matches the expected application response.

### Expected Result

Users should receive the appropriate response based on their account status.

---

# TC2 - Login with Invalid Credentials

### Scenario

Attempt to log in using invalid/non-standard credentials.

### Validation

The test verifies the error message displayed by the application.

### Expected Result

Access should be denied and an appropriate error message should be displayed.

---

# TC3 - Validate Logout Functionality

### Scenario

Login successfully and perform logout.

### Validation

The test verifies:

- Logout option is available
- Logout can be performed
- User is redirected to the login page

### Expected Result

The user should be successfully logged out and returned to the login screen.

---

# TC4 - Check Cart Icon Visibility

### Scenario

Login successfully and verify the shopping cart icon.

### Validation

The test verifies that the cart icon is visible and accessible on the products page.

### Expected Result

The cart icon should be displayed after successful login.

---

# TC5 - Random Selection of Products and Data Extraction

### Scenario

Randomly select 4 products from the available product catalog.

### Validation

The test extracts:

- Product name
- Product price

### Expected Result

Exactly 4 products should be selected and their product data should be accurately captured.

---

# TC6 - Add Selected Products to Cart and Validate

### Scenario

Add 4 selected products to the shopping cart.

### Validation

The test verifies:

- Products are added successfully
- Cart count is updated
- Cart count equals 4

### Expected Result

The cart should display a count of 4.

---

# TC7 - Validate Product Details Inside Cart

### Scenario

Navigate to the shopping cart and validate the products added during the purchase flow.

### Validation

The test compares:

- Expected product names
- Expected prices
- Actual cart product names
- Actual cart prices

### Expected Result

The products and prices displayed in the cart should match the products that were selected and added.

---

# TC8 - Complete Checkout and Validate Order

### Scenario

Complete the checkout process after adding products to the cart.

### Steps

1. Login
2. Select products
3. Add products to cart
4. Open cart
5. Proceed to checkout
6. Enter customer information
7. Validate order summary
8. Complete the order

### Validation

The test verifies:

- Checkout information
- Product summary
- Product count
- Product names
- Product prices
- Order completion

### Expected Result

The order summary should contain the correct products and the order confirmation should be displayed.

---

# TC9 - Validate Sorting Functionality

### Scenario

Validate product sorting functionality.

### Sorting Options

The framework validates sorting such as:

- Price: Low to High
- Name: Z to A

### Validation

The test compares the displayed product order with the expected sorted order.

### Expected Result

Products should be displayed in the correct order according to the selected sorting option.

---

# TC10 - Validate Reset App State Functionality

### Scenario

Add products to the cart and use the application's **Reset App State** functionality.

### Steps

1. Login
2. Add 4 products
3. Verify cart count
4. Open application menu
5. Select Reset App State
6. Verify cart count
7. Open cart
8. Verify cart is empty

### Expected Result

All cart items should be removed and the application should return to its default state.

---

# 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution framework |
| Pytest HTML | HTML test reporting |
| Page Object Model | Framework design |
| Chrome | Web browser |
| Git | Version control |
| GitHub | Source code repository |
| Google Drive | Test report sharing |

---

# 6. Framework Architecture

The framework follows the **Page Object Model (POM)** design pattern.

```text
E-commerce web application_Sauce demo/
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── menu_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_case_01_login.py
│   ├── test_case_02_invalid_login.py
│   ├── test_case_03_logout.py
│   ├── test_case_04_cart_icon.py
│   ├── test_case_05_random_products.py
│   ├── test_case_06_add_products_cart.py
│   ├── test_case_07_cart_details.py
│   ├── test_case_08_checkout.py
│   ├── test_case_09_sorting.py
│   └── test_case_10_reset_app_state.py
│
├── utilities/
│   ├── __init__.py
│   └── logger.py
│
├── reports/
│   └── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md