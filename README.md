# e-commerce_with_mongodb


## **Overview**
This project demonstrates the implementation and analysis of an e-commerce database using MongoDB. The database is designed to handle collections for customers, products, orders, and order items. Advanced MongoDB features like aggregation pipelines, schema design, transactions, and indexing are utilized to simulate a real-world e-commerce platform and derive meaningful insights.

---

## **Schema Design**

The database schema is designed with four primary collections:

### **1. Customers Collection**
- **Purpose**: Stores customer information including contact details and addresses.
- **Structure**:
  - `customer_id`: Primary key, unique for each customer.
  - `name`: Full name of the customer.
  - `email`: Email address, serves as a unique identifier.
  - `address`: Embedded document containing street, city, and state information.

### **2. Products Collection**
- **Purpose**: Stores details about the products available for purchase.
- **Structure**:
  - `product_id`: Primary key, unique for each product.
  - `product_name`: Name of the product.
  - `category`: Product category (e.g., Electronics, Accessories).
  - `price`: Price of the product.

### **3. Orders Collection**
- **Purpose**: Represents customer orders and their statuses.
- **Structure**:
  - `order_id`: Primary key, unique for each order.
  - `customer_id`: Foreign key referencing the `customer_id` in the Customers collection.
  - `order_date`: Date when the order was placed.
  - `delivery_date`: Date when the order was delivered (if applicable).
  - `status`: Current status of the order (e.g., Delivered, Pending, Canceled).

### **4. Order_Items Collection**
- **Purpose**: Stores the details of items within each order.
- **Structure**:
  - `order_item_id`: Primary key, unique for each order item.
  - `order_id`: Foreign key referencing the `order_id` in the Orders collection.
  - `product_id`: Foreign key referencing the `product_id` in the Products collection.
  - `quantity`: Number of units ordered for the product.
  - `price`: Price per unit.

---

### **Key Design Decisions**
1. **Embedded vs. Referenced Schema**:
   - **Embedded Schema**:
     - The `address` field in the `customers` collection is embedded to reduce the need for frequent lookups.
   - **Referenced Schema**:
     - `orders` and `order_items` reference their related collections (e.g., `customers`, `products`) for scalability and modularity.
2. **Indexing**:
   - Fields like `customer_id`, `product_id`, and `order_id` are indexed to improve query performance.
3. **Normalization**:
   - Ensures no duplication of product or customer data across collections, adhering to a relational database design.

---

## **Steps to Run the Scripts**

### **Pre-requisites**
1. Install MongoDB locally or configure a MongoDB Atlas cluster.
2. Install Python and the `pymongo` library:
   ```bash
   pip install pymongo
   ```
3. Clone this repository and navigate to the project directory.

### **How to Run**
1. Save the script in a file, e.g., `ecommerce_project.py`.
2. Run the script in your terminal:
   ```bash
   python ecommerce_project.py
   ```
3. The script will:
   - Insert sample data into the collections (`customers`, `products`, `orders`, `order_items`).
   - Run advanced analytical queries and display results.
   - Apply indexing and schema validation.
   - Demonstrate transactions and change streams (if running on a replica set).

---

## **Queries and Results**

### **1. Revenue by Product Category**
- **Query**:
  Uses `$lookup`, `$unwind`, `$addFields`, `$group`, and `$sort` to calculate total revenue for each product category.
- **Result**:
  ```
  Category: Electronics, Total Revenue: 8000
  Category: Accessories, Total Revenue: 500
  ```

### **2. Average Delivery Time**
- **Query**:
  Calculates the difference between `order_date` and `delivery_date` for all delivered orders using `$addFields` and `$group`.
- **Result**:
  ```
  Average Delivery Time: 2.0 days
  ```

### **3. Customers by State**
- **Query**:
  Groups customers by `state` and counts the number of customers in each state using `$group` and `$sort`.
- **Result**:
  ```
  State: NY, Customers: 3
  State: IL, Customers: 2
  ```

### **4. Top 3 Most Expensive Products by Order**
- **Query**:
  Joins `order_items` with `products`, groups by `order_id`, sorts products by price, and retrieves the top 3 most expensive products per order.
- **Result**:
  ```
  Order ID: 5001
    Product Name: Laptop, Price: 1200, Quantity: 2
    Product Name: Phone, Price: 800, Quantity: 1
  ```

---

## **Advanced Features**

### **1. Transactions**
Simulates an order creation process, updating both `orders` and `products` atomically using MongoDB transactions.

### **2. Change Streams**
Monitors real-time changes in the `orders` collection and prints detected changes.

### **3. Schema Validation**
Applies validation rules to the `products` collection, ensuring:
- `product_name` is a required string.
- `price` is a required positive number.

---

## **Insights and Conclusion**

### **Insights**
1. **High Revenue Products**: Electronics generated the highest revenue, indicating strong customer preference for this category.
2. **Delivery Time Consistency**: The average delivery time of 2 days suggests an efficient delivery pipeline.
3. **Customer Distribution**: New York has the highest number of customers, making it a prime market for targeted promotions.
4. **Order Preferences**: Analysis of the top 3 products per order shows a high demand for premium electronics like laptops and phones.

### **Conclusion**
This project demonstrates the power of MongoDB in handling and analyzing structured e-commerce data. By leveraging advanced features such as transactions, indexing, and change streams, we achieved a robust, scalable solution for data storage and analysis. The insights gained can guide business decisions like inventory management, delivery optimizations, and customer targeting strategies.

---

## **Acknowledgments**
This project was completed as part of a data engineering program in ALTSchool. It demonstrates proficiency in MongoDB concepts and best practices for schema design, aggregation pipelines, and advanced database features.

---
