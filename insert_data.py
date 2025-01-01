from pymongo import MongoClient
from datetime import datetime, timedelta
from pymongo.errors import PyMongoError
import time
from pymongo.errors import PyMongoError
from pymongo import MongoClient, errors

# Connect to MongoDB Atlas
client = MongoClient("mongodb://localhost:27017/")

# Access the 'ecommerce' database
db = client["ecommerce"]

# print("Connected to MongoDB!")

# customers = db["customers"]

# customer_data = [
#     {"customer_id": 1, "name": "Alice", "email": "alice@example.com", "address": {"street": "123 Maple St", "city": "Springfield", "state": "IL"}},
#     {"customer_id": 2, "name": "Bob", "email": "bob@example.com", "address": {"street": "456 Oak St", "city": "Metropolis", "state": "NY"}},
#     {"customer_id": 3, "name": "Charlie", "email": "charlie@example.com", "address": {"street": "789 Pine St", "city": "Smallville", "state": "CA"}},
#     {"customer_id": 4, "name": "Daisy", "email": "daisy@example.com", "address": {"street": "101 Elm St", "city": "Riverdale", "state": "TX"}},
#     {"customer_id": 5, "name": "Eve", "email": "eve@example.com", "address": {"street": "202 Birch St", "city": "Hill Valley", "state": "FL"}},
#     {"customer_id": 6, "name": "Frank", "email": "frank@example.com", "address": {"street": "303 Cedar St", "city": "Gotham", "state": "NJ"}},
#     {"customer_id": 7, "name": "Grace", "email": "grace@example.com", "address": {"street": "404 Willow St", "city": "Star City", "state": "WA"}},
#     {"customer_id": 8, "name": "Hank", "email": "hank@example.com", "address": {"street": "505 Ash St", "city": "Central City", "state": "CO"}},
#     {"customer_id": 9, "name": "Ivy", "email": "ivy@example.com", "address": {"street": "606 Oak St", "city": "Mystic Falls", "state": "GA"}},
#     {"customer_id": 10, "name": "Jack", "email": "jack@example.com", "address": {"street": "707 Fir St", "city": "Metropolis", "state": "NY"}},
#     {"customer_id": 11, "name": "Kara", "email": "kara@example.com", "address": {"street": "808 Redwood St", "city": "Smallville", "state": "CA"}},
#     {"customer_id": 12, "name": "Leo", "email": "leo@example.com", "address": {"street": "909 Sequoia St", "city": "Gotham", "state": "NJ"}},
#     {"customer_id": 13, "name": "Maya", "email": "maya@example.com", "address": {"street": "100 Birch St", "city": "Riverdale", "state": "TX"}},
#     {"customer_id": 14, "name": "Nina", "email": "nina@example.com", "address": {"street": "111 Maple St", "city": "Hill Valley", "state": "FL"}},
#     {"customer_id": 15, "name": "Oscar", "email": "oscar@example.com", "address": {"street": "222 Elm St", "city": "Central City", "state": "CO"}},
#     {"customer_id": 16, "name": "Pam", "email": "pam@example.com", "address": {"street": "333 Cedar St", "city": "Mystic Falls", "state": "GA"}},
#     {"customer_id": 17, "name": "Quinn", "email": "quinn@example.com", "address": {"street": "444 Willow St", "city": "Star City", "state": "WA"}},
#     {"customer_id": 18, "name": "Ray", "email": "ray@example.com", "address": {"street": "555 Ash St", "city": "Springfield", "state": "IL"}},
#     {"customer_id": 19, "name": "Sophie", "email": "sophie@example.com", "address": {"street": "666 Oak St", "city": "Metropolis", "state": "NY"}},
#     {"customer_id": 20, "name": "Tom", "email": "tom@example.com", "address": {"street": "777 Fir St", "city": "Riverdale", "state": "TX"}}
# ]


# # Insert documents into the 'customers' collection
# customers.insert_many(customer_data)
# print("Inserted customers!")


# # Fetch all documents from the 'customers' collection
# customers = db["customers"].find()
# print("Customers:")
# for customer in customers:
#     print(customer)


# # Insert data into 'products' collection
# products = db["products"]
# product_data = [
#     {"product_id": 101, "product_name": "Laptop", "category": "Electronics", "price": 1200},
#     {"product_id": 102, "product_name": "Phone", "category": "Electronics", "price": 800},
#     {"product_id": 103, "product_name": "Tablet", "category": "Electronics", "price": 600},
#     {"product_id": 104, "product_name": "Monitor", "category": "Electronics", "price": 300},
#     {"product_id": 105, "product_name": "Headphones", "category": "Accessories", "price": 150},
#     {"product_id": 106, "product_name": "Keyboard", "category": "Accessories", "price": 50},
#     {"product_id": 107, "product_name": "Mouse", "category": "Accessories", "price": 25},
#     {"product_id": 108, "product_name": "Printer", "category": "Electronics", "price": 200},
#     {"product_id": 109, "product_name": "Speaker", "category": "Accessories", "price": 100},
#     {"product_id": 110, "product_name": "Camera", "category": "Electronics", "price": 400},
#     {"product_id": 111, "product_name": "Webcam", "category": "Accessories", "price": 80},
#     {"product_id": 112, "product_name": "Router", "category": "Networking", "price": 120},
#     {"product_id": 113, "product_name": "Switch", "category": "Networking", "price": 250},
#     {"product_id": 114, "product_name": "Smartwatch", "category": "Electronics", "price": 300},
#     {"product_id": 115, "product_name": "Fitness Tracker", "category": "Electronics", "price": 150},
#     {"product_id": 116, "product_name": "Projector", "category": "Electronics", "price": 500},
#     {"product_id": 117, "product_name": "Hard Drive", "category": "Storage", "price": 100},
#     {"product_id": 118, "product_name": "SSD", "category": "Storage", "price": 200},
#     {"product_id": 119, "product_name": "Memory Card", "category": "Storage", "price": 50},
#     {"product_id": 120, "product_name": "USB Drive", "category": "Storage", "price": 20}
# ]

# products.insert_many(product_data)
# print("Inserted products!")


# # Insert data into 'orders' collection
# orders = db["orders"]
# order_data = [
#     {"order_id": 5001, "customer_id": 1, "order_date": "2024-01-15T10:00:00Z", "status": "Delivered"},
#     {"order_id": 5002, "customer_id": 2, "order_date": "2024-01-16T12:00:00Z", "status": "Pending"},
#     {"order_id": 5003, "customer_id": 3, "order_date": "2024-01-17T14:30:00Z", "status": "Shipped"},
#     {"order_id": 5004, "customer_id": 4, "order_date": "2024-01-18T09:45:00Z", "status": "Delivered"},
#     {"order_id": 5005, "customer_id": 5, "order_date": "2024-01-19T16:20:00Z", "status": "Canceled"},
#     {"order_id": 5006, "customer_id": 6, "order_date": "2024-01-20T11:10:00Z", "status": "Pending"},
#     {"order_id": 5007, "customer_id": 7, "order_date": "2024-01-21T08:25:00Z", "status": "Shipped"},
#     {"order_id": 5008, "customer_id": 8, "order_date": "2024-01-22T13:15:00Z", "status": "Delivered"},
#     {"order_id": 5009, "customer_id": 9, "order_date": "2024-01-23T10:05:00Z", "status": "Pending"},
#     {"order_id": 5010, "customer_id": 10, "order_date": "2024-01-24T15:50:00Z", "status": "Delivered"},
#     {"order_id": 5011, "customer_id": 11, "order_date": "2024-01-25T18:30:00Z", "status": "Shipped"},
#     {"order_id": 5012, "customer_id": 12, "order_date": "2024-01-26T09:00:00Z", "status": "Delivered"},
#     {"order_id": 5013, "customer_id": 13, "order_date": "2024-01-27T11:45:00Z", "status": "Pending"},
#     {"order_id": 5014, "customer_id": 14, "order_date": "2024-01-28T17:25:00Z", "status": "Delivered"},
#     {"order_id": 5015, "customer_id": 15, "order_date": "2024-01-29T13:55:00Z", "status": "Shipped"},
#     {"order_id": 5016, "customer_id": 16, "order_date": "2024-01-30T08:40:00Z", "status": "Pending"},
#     {"order_id": 5017, "customer_id": 17, "order_date": "2024-01-31T19:15:00Z", "status": "Delivered"},
#     {"order_id": 5018, "customer_id": 18, "order_date": "2024-02-01T10:50:00Z", "status": "Canceled"},
#     {"order_id": 5019, "customer_id": 19, "order_date": "2024-02-02T14:10:00Z", "status": "Pending"},
#     {"order_id": 5020, "customer_id": 20, "order_date": "2024-02-03T16:35:00Z", "status": "Delivered"}
# ]

# orders.insert_many(order_data)

# # Insert data into 'order_items' collection
# order_items = db["order_items"]
# order_item_data = [
#     {"order_item_id": 9001, "order_id": 5001, "product_id": 101, "quantity": 2, "price": 1200},
#     {"order_item_id": 9002, "order_id": 5001, "product_id": 105, "quantity": 1, "price": 150},
#     {"order_item_id": 9003, "order_id": 5002, "product_id": 102, "quantity": 1, "price": 800},
#     {"order_item_id": 9004, "order_id": 5002, "product_id": 107, "quantity": 2, "price": 25},
#     {"order_item_id": 9005, "order_id": 5003, "product_id": 103, "quantity": 3, "price": 600},
#     {"order_item_id": 9006, "order_id": 5003, "product_id": 109, "quantity": 1, "price": 100},
#     {"order_item_id": 9007, "order_id": 5004, "product_id": 104, "quantity": 1, "price": 300},
#     {"order_item_id": 9008, "order_id": 5004, "product_id": 110, "quantity": 1, "price": 400},
#     {"order_item_id": 9009, "order_id": 5005, "product_id": 101, "quantity": 1, "price": 1200},
#     {"order_item_id": 9010, "order_id": 5006, "product_id": 106, "quantity": 4, "price": 50},
#     {"order_item_id": 9011, "order_id": 5007, "product_id": 108, "quantity": 1, "price": 200},
#     {"order_item_id": 9012, "order_id": 5007, "product_id": 114, "quantity": 2, "price": 300},
#     {"order_item_id": 9013, "order_id": 5008, "product_id": 115, "quantity": 1, "price": 150},
#     {"order_item_id": 9014, "order_id": 5008, "product_id": 119, "quantity": 5, "price": 50},
#     {"order_item_id": 9015, "order_id": 5009, "product_id": 120, "quantity": 4, "price": 20},
#     {"order_item_id": 9016, "order_id": 5010, "product_id": 112, "quantity": 1, "price": 120},
#     {"order_item_id": 9017, "order_id": 5011, "product_id": 113, "quantity": 1, "price": 250},
#     {"order_item_id": 9018, "order_id": 5012, "product_id": 118, "quantity": 2, "price": 200},
#     {"order_item_id": 9019, "order_id": 5013, "product_id": 117, "quantity": 3, "price": 100},
#     {"order_item_id": 9020, "order_id": 5014, "product_id": 115, "quantity": 1, "price": 150}
# ]

# order_items.insert_many(order_item_data)

# print("All data inserted successfully!")

# Task 2: Analytical Queries
# 1. Calculate the total revenue generated by each product category.

# pipeline = [
#     # Join order_items with products to get product details
#     {
#         "$lookup": {
#             "from": "products",  # Target collection
#             "localField": "product_id",  # Field in order_items
#             "foreignField": "product_id",  # Field in products
#             "as": "product_details"  # Output array field
#         }
#     },
#     # Unwind the product_details array to make it a single document
#     {
#         "$unwind": "$product_details"
#     },
#     # Add a calculated field for revenue (quantity * price)
#     {
#         "$addFields": {
#             "revenue": {"$multiply": ["$quantity", "$price"]}
#         }
#     },
#     # Group by product category and calculate total revenue
#     {
#         "$group": {
#             "_id": "$product_details.category",  # Group by category
#             "total_revenue": {"$sum": "$revenue"},
#             "details": {
#                 "$push": {
#                     "product_id": "$product_id",
#                     "quantity": "$quantity",
#                     "price": "$price",
#                     "revenue": "$revenue"
#                 }
#             }
#         }
#     },
#     # Sort categories by total revenue in descending order
#     {
#         "$sort": {"total_revenue": -1}
#     }
# ]

# # Run the aggregation pipeline
# result = list(db.order_items.aggregate(pipeline))

# # Print detailed output
# for category in result:
#     print(f"Category: {category['_id']}, Total Revenue: {category['total_revenue']}")
#     print("Details:")
#     for detail in category["details"]:
#         print(f"  Product ID: {detail['product_id']}, Quantity: {detail['quantity']}, Price: {detail['price']}, Revenue: {detail['revenue']}")
#     print()


# # What is the average delivery time for orders?

# orders = db.orders.find()
# for order in orders:
#     print(f"Processing order: {order['_id']}")
#     order_date = order["order_date"]
#     # Convert order_date to ISODate if it's a string
#     if isinstance(order_date, str):
#         try:
#             order_date = datetime.strptime(order_date.replace("Z", ""), "%Y-%m-%dT%H:%M:%S")
#             db.orders.update_one(
#                 {"_id": order["_id"]},
#                 {
#                     "$set": {
#                         "order_date": order_date
#                     }
#                 }
#             )
#             print(f"Updated order_date for order: {order['_id']}")
#         except Exception as e:
#             print(f"Error updating order_date for order {order['_id']}: {e}")

#     # Add a dummy delivery_date if it doesn't exist
#     if "delivery_date" not in order:
#         try:
#             delivery_date = order_date + timedelta(days=2)
#             db.orders.update_one(
#                 {"_id": order["_id"]},
#                 {
#                     "$set": {
#                         "delivery_date": delivery_date
#                     }
#                 }
#             )
#             print(f"Added delivery_date for order: {order['_id']}")
#         except Exception as e:
#             print(f"Error adding delivery_date for order {order['_id']}: {e}")

# # Step 2: Define the aggregation pipeline to calculate average delivery time
# pipeline = [
#     # Match documents with valid order_date and delivery_date
#     {
#         "$match": {
#             "order_date": {"$exists": True, "$ne": None},
#             "delivery_date": {"$exists": True, "$ne": None},
#         }
#     },
#     # Add a field to calculate delivery time in days
#     {
#         "$addFields": {
#             "delivery_time_in_days": {
#                 "$divide": [
#                     {"$subtract": ["$delivery_date", "$order_date"]},  # Difference in milliseconds
#                     1000 * 60 * 60 * 24,  # Convert milliseconds to days
#                 ]
#             }
#         }
#     },
#     # Group by all orders and calculate the average delivery time
#     {
#         "$group": {
#             "_id": None,  # No grouping key, aggregate all orders
#             "average_delivery_time": {"$avg": "$delivery_time_in_days"},
#         }
#     },
# ]

# # Step 3: Run the aggregation pipeline
# try:
#     result = list(db.orders.aggregate(pipeline))
#     # Step 4: Print the result
#     if result and result[0].get("average_delivery_time") is not None:
#         avg_delivery_time = result[0]["average_delivery_time"]
#         print(f"Average Delivery Time: {avg_delivery_time:.2f} days")
#     else:
#         print("No valid data to calculate average delivery time.")
# except Exception as e:
#     print(f"Error running aggregation pipeline: {e}")


# Which states have the highest number of customers?
# Define the aggregation pipeline
# pipeline = [
#     # Group by state and count the number of customers
#     {
#         "$group": {
#             "_id": "$address.state",  # Access the state field inside the address object
#             "customer_count": {"$sum": 1}  # Count the number of customers in each state
#         }
#     },
#     # Sort the results by customer_count in descending order
#     {
#         "$sort": {"customer_count": -1}
#     }
# ]

# # Run the aggregation pipeline
# result = list(db.customers.aggregate(pipeline))

# # Print the results
# print("Number of Customers by State (Descending):")
# for state in result:
#     print(f"State: {state['_id']}, Customers: {state['customer_count']}")


# What are the top 3 most expensive products sold in each order?

# Define the aggregation pipeline
# pipeline = [
#     # Join order_items with products to get product details
#     {
#         "$lookup": {
#             "from": "products",  # Target collection
#             "localField": "product_id",  # Field in order_items
#             "foreignField": "product_id",  # Field in products
#             "as": "product_details"  # Output array field
#         }
#     },
#     # Unwind product_details to make it a single document
#     {
#         "$unwind": "$product_details"
#     },
#     # Group by order_id to collect product details
#     {
#         "$group": {
#             "_id": "$order_id",  # Group by order ID
#             "products": {
#                 "$push": {
#                     "product_name": "$product_details.product_name",
#                     "price": "$product_details.price",
#                     "quantity": "$quantity"
#                 }
#             }
#         }
#     },
#     # Sort the products within each group by price in descending order
#     {
#         "$project": {
#             "products": {
#                 "$slice": [
#                     {
#                         "$sortArray": {
#                             "input": "$products",
#                             "sortBy": {"price": -1}
#                         }
#                     },
#                     3
#                 ]
#             }
#         }
#     }
# ]

# # Run the aggregation pipeline
# result = list(db.order_items.aggregate(pipeline))

# # Print the results
# print("Top 3 Most Expensive Products for Each Order:")
# for order in result:
#     print(f"Order ID: {order['_id']}")
#     for product in order["products"]:
#         print(f"  Product Name: {product['product_name']}, Price: {product['price']}, Quantity: {product['quantity']}")
#     print()


#Task 3: Schema Design and Optimization
#Choose between embedded and referenced schema designs for each collection and explain why.
#Create indexes on frequently queried fields like customer_id and product_id.

# Create indexes
# db.customers.create_index("customer_id")  # Index on customer_id
# db.products.create_index("product_id")    # Index on product_id
# db.orders.create_index("order_id")        # Index on order_id
# db.order_items.create_index("order_id")   # Index on order_id in order_items
# db.order_items.create_index("product_id") # Index on product_id in order_items

# print("Indexes created successfully!")

# # List indexes for the customers collection
# indexes = db.customers.index_information()
# print("Indexes on 'customers':", indexes)


# Task 4: Advanced Features


# Check if the MongoDB instance is part of a replica set
is_replica_set = client.is_mongos or client.admin.command("ismaster").get("setName")

if is_replica_set:
    # Part 1: Transaction - Simulate order creation process
    session = client.start_session()
    session.start_transaction()

    try:
        # Step 1: Insert a new order
        new_order = {
            "order_id": 5015,
            "customer_id": 1,
            "order_date": "2024-01-22T12:00:00Z",
            "delivery_date": "2024-01-25T12:00:00Z",
            "status": "Pending"
        }
        db.orders.insert_one(new_order, session=session)

        # Step 2: Insert related order items
        new_order_items = [
            {"order_item_id": 9005, "order_id": 5015, "product_id": 101, "quantity": 1, "price": 1200},
            {"order_item_id": 9006, "order_id": 5015, "product_id": 102, "quantity": 2, "price": 800}
        ]
        db.order_items.insert_many(new_order_items, session=session)

        # Step 3: Update product inventory
        for item in new_order_items:
            db.products.update_one(
                {"product_id": item["product_id"]},
                {"$inc": {"stock_quantity": -item["quantity"]}},
                session=session
            )

        # Commit the transaction
        session.commit_transaction()
        print("Transaction completed successfully.")

    except errors.PyMongoError as e:
        # Abort the transaction in case of an error
        session.abort_transaction()
        print(f"Transaction aborted due to an error: {e}")

    finally:
        # End the session
        session.end_session()

    # Part 2: Monitor changes in the `orders` collection using Change Streams
    try:
        with db.orders.watch() as stream:
            print("Watching changes in the 'orders' collection...")
            for change in stream:
                print("Change detected:")
                print(change)
    except KeyboardInterrupt:
        print("Stopped watching changes.")
else:
    print("Transactions and change streams are only supported on replica sets or sharded clusters.")

# Part 3: Schema validation for the `products` collection
db.command({
    "collMod": "products",  # Target collection
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["product_name", "price"],
            "properties": {
                "product_name": {
                    "bsonType": "string",
                    "description": "Must be a string and is required"
                },
                "price": {
                    "bsonType": "number",
                    "minimum": 0,
                    "description": "Must be a positive number and is required"
                }
            }
        }
    },
    "validationLevel": "strict"
})
print("Schema validation applied to the `products` collection.")

# Test schema validation with an invalid document
try:
    db.products.insert_one({
        "product_name": "Invalid Product",
        "price": -10  # Invalid price
    })
except errors.PyMongoError as e:
    print(f"Schema validation prevented invalid document: {e}")