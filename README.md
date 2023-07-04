# Assignment: Optimize Fetching Orders of a Customer

Flipkart has a table called `Orders` with millions of rows. The schema of Orders looks as follows:
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

Flipkart often has to write a query to fetch orders for a particular customer placed on a particular date. Query looks as follows:

```sql
SELECT * FROM Orders WHERE CustomerID = {abc} AND OrderDate > '{abc}';
```

Go to `schema.sql` and modify it (only add new rows at the end) to optimize the above query. The modification you do hsould create an index on the relevant columns in the orders table that will make query like above fast.

Post updating, create a pull request with your changes. Your changes will be automatically evaluated and you will get a tick if your answer is correct. Best wishes!

You can see a Loom Video here of walkthrough: {LINK}