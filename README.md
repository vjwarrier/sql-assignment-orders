# Assignment: Optimize Fetching Orders of a Customer

Flipkart has millions of orders and stores details about those in a table called `Orders`. The schema of Orders looks as follows:

```sql
 CREATE TABLE IF NOT EXISTS Orders (
    OrderID INT AUTO_INCREMENT,
    CustomerID INT,
    OrderDate DATE,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID)
);
```

Flipkart often has to write a query to fetch orders for a particular customer placed after a particular date. Query looks as follows:

```sql
SELECT * FROM Orders WHERE CustomerID = {abc} AND OrderDate > '{abc}';
```

Currently Flipkart has done no optimization on this table for this query and thus query is becoming increasingly slow. Go to `schema.sql` and modify it (only add new rows at the end) to optimize the above query. The modification you should do should create an index on the relevant columns in the orders table that will make above query fast.

Post updating the schema, create a pull request with your changes. Your changes will be automatically evaluated and you will get a green tick if your answer is correct. Else, you get a red cross. Best wishes!

You can see a Loom Video here of walkthrough:

Part 1: https://www.loom.com/share/c5ec2a923ad945ab828bd7435c3f42f5?sid=c32af92e-3105-47f1-be3f-14c4b5bcfb9d  
Part 2: https://www.loom.com/share/c02f5b2aa5a84e818a9c16d2e0fda33e?sid=bc7d7621-6961-4a65-8881-a92f6d74569c