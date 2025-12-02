---
date:
    created: 2025-11-22
draft: true
tags:
  - Programming
---
My note regarding relational database(Mostly PostgreSQL)
<!-- more -->


# 1. CRUD Query
## 1.1 Create tables
regular table with primary key:
```postgresql
DROP DATABASE IF EXISTS Projects;
CREATE DATABASE Projects;

CREATE TABLE Projects.ContractorInfo (
    ContractorId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Address VARCHAR(255)
);
```

table with foreign key:
```postgresql
CREATE TABLE Projects.ProjectInfo (
    ProjectId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Address VARCHAR(255),
    ContractorId INT,
    FOREIGN KEY (ContractorId)
        REFERENCES Projects.ContractorInfo(ContractorId)
);

CREATE TABLE Projects.Invoices (
    InvoiceId INT AUTO_INCREMENT PRIMARY KEY,
    ProjectId INT,
    JobNumber VARCHAR(50),
    InvoiceValue DECIMAL(10, 2),
    FOREIGN KEY (ProjectId)
        REFERENCES Projects.ProjectInfo(ProjectId)
);

```


## 1.2 Select Query
use the table schema from above section
```postgresql
-- basic query structure
SELECT ProjectInfo.Name AS projectname, ContractorInfo.Name AS contractorname, sum(Invoices.InvoiceValue) AS total
FROM ProjectInfo JOIN ContractorInfo 
    ON ProjectInfo.ContractorId = ContractorInfo.ContractorId
JOIN Invoices
    ON ProjectInfo.ProjectId = Invoices.ProjectId
WHERE ...
GROUP BY ProjectInfo.Name, ContractorInfo.Name
HAVING ...
ORDER BY ... [ASC | DESC]
LIMIT ...
OFFSET ...;
```

## 1.3 INSERT/UPDATE/DELETE


# 2. Index
data structure:
- Common: B+ tree
- full-text indexes
- location queries: geo-spatial indexes


# 3. Non-relational type
other database types:
- hashtable: Reddis
- documents: MongoDB
- column: Cassandra, Hbase
- graph: Neo4j