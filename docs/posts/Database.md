---
date:
    created: 2025-12-12
tags:
  - Programming
---
My note regarding relational database(Mostly PostgreSQL 14+)
<!-- more -->


# 1. SQL

## 1.1 Connect to DB
1. start postgresql server(windows): `net start "postgresql-x64-14"`
2. connect with client: `psql -h <hostname> -p <port> -U <user>`(user default: `postgres`) or use pgadmin

useful commands

| command                            | role                                      |
| ---------------------------------- | ----------------------------------------- |
| \l                                 | lists all databases                       |
| \conninfo                          | show current user and database            |
| `\c <target_db>`                   | switch current db to `<target_db>`        |
| \dn                                | list all schema names of current database |
| SELECT current_schema;             | show current schema name                  |
| `set search_path to <schema_name>` | switch current schema to `<schema_name>`  |
| \dt                                | list all tables under current schema      |
| `\dt <schema_name>.*`              | list all tables under `<schema_name>`     |


## 1.2 Create tables
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


## 1.3 Select Query
use the table schema from above section
```postgresql
-- basic query structure
SELECT [DISTINCT ]<table1>.<col1> AS <col1>, <table2>.<col2> AS <col2>, aggregate_function(<table3>.<col3>) AS total
FROM <tablex> JOIN <tabley> 
    ON <tablex>.<colx> = <tabley>.<coly>
JOIN ... ON ...
WHERE <cond>
GROUP BY <tablea>.<cola>, <tableb>.<colb>
HAVING <cond>
WINDOW <window_name>
[< UNION | INTERSECT | EXCEPT > [ <ALL | DISTINCT >] <select_query> ]
ORDER BY <tablexx>.<colxx> [ASC | DESC]
LIMIT <row_num>
OFFSET <pos>
FOR <UPDATE | NO KEY UPDATE | SHARE | KEY SHARE>; -- lock selected rows

-- example
SELECT ProjectInfo.Name AS projectname, ContractorInfo.Name AS contractorname, sum(Invoices.InvoiceValue) AS total
FROM ProjectInfo JOIN ContractorInfo 
    ON ProjectInfo.ContractorId = ContractorInfo.ContractorId
JOIN Invoices
    ON ProjectInfo.ProjectId = Invoices.ProjectId
GROUP BY ProjectInfo.Name, ContractorInfo.Name;
```


| Keyword | Role                                                                                                                              |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Having  | filter groups based on condition; if this group has multiple rows, the condition after having needs to employ aggregate functions |


## 1.4 Join table queries

```postgresql
-- inner join(default): output contains the intersection of two tables rows 
-- left join: output contains all left table rows, combined right table columns will be empty
-- right join: output contains all right table rows, combined left table columns will be empty
-- full join: returns rows from a table that do not have the corresponding rows in the other table
-- full outer join: contains all rows from both left and right tables
-- cross: combining every row from the first table with every row from the second, no join condition
```

## 1.5 INSERT/UPDATE/DELETE
```postgresql
-- Insert
INSERT INTO <tables_name> (<col1>, <col2>, <col3>, ...)
VALUES (<val1>, <val2>, <val3>, ...);

-- Update
UPDATE <tables_name>
SET (<col1> = <val1>, <col2> = <val2>, ...)
WHERE <cond>

-- delete
DELETE FROM <tables_name>
WHERE <cond> 
```

## 1.6 Alter table
```postgresql
-- add column
ALTER TABLE <tables_name>
ADD <col_name> <col_type>;

-- modify column
ALTER TABLE <tables_name>
ALTER COLUMN <col_name> <new_col_type>;

-- drop column
ALTER TABLE <tables_name>
DROP COLUMN <col_name>;

-- add/drop constraint
-- add primary key
ALTER TABLE <tables_name>
ADD PRIMARY KEY <col_name>;
-- drop constraint
ALTER TABLE <tables_name>
DROP CONSTRAINT <constraints_name>;

-- Rename
-- rename a table
ALTER TABLE <tables_name>
RENAME TO <new_table_name>;
-- rename column
ALTER TABLE <tables_name>
RENAME COLUMN <col_name> TO <new_col_name>;

```

## 1.7 import and export
> [!NOTE]- export
> - database:
> ```powershell
> # entire database
> pgdump -U <username> -d <db_name> > output.sql
> # export only the schema
> pgdump -U <username> -d <db_name> --schema-only > output.sql
> # export only the data
> pgdump -U <username> -d <db_name> --data-only > output.sql
> ```
> - schema:
> ```powershell
> # dump only the schema, no data through -s
> pgdump -U <username> -n <schema_name> -s <db_name> > output.sql
> ```
> - table:
> ```powershell
> # entire table
> pg_dump -U <username> -d <db_name> -n <schema_name> -t <table_name> > output.sql
> # schema only
> pg_dump -U <username> -d <db_name> -n <schema_name> -t <table> --schema-only > table_schema.sql
> # data only
> pg_dump -U <username> -d <db_name> -n <schema_name> -t <table> --data-only > table_data.sql
> ```

> [!NOTE]- import
> 1. create db in psql: `createdb -T template0 <db_name>`
> 2. import .sql: `psql -U <username> -d <db_name> -f <sql_file_name>`

## 1.8 Other syntax

```postgresql
-- WITH

-- IF

-- operator(::)

```

# 2. Index
## 2.1 Overview
Types of indices:
- B+ tree(default): for  single or range query with condition that contains`=`, `>`, `<` 
- hash: for condition that contains `=`
- GIN(Generalized Inverted Index): for arrays, JSONB data, TEXT
- GiST(Generalized Search Tree): geometric, spatial, full-text
- SP-Gist(Space-partitioned GiST): data that can be partitioned into non-overlapping regions
- BRIN(Block Range Index): data with natural physical order(e.g: timestamp column in an append-only log table)


When index scan(explain query plan) is used(or when to use index):
- when indexed column combined with indexable operators appears in `select...where...`
- indexed columns used in `JOIN...ON` conditions
- indexed columns appear in `ORDER BY` or `GROUP BY`
- when there is primary key column, unique column or distinct keyword in select query(note: primary key column/unique column creates b-tree index which is the only supported index type)

create regular index sql for different types:
```postgresql
-- btree index
CREATE INDEX IF NOT EXISTS <idx> ON <tables_name> (<col>);

-- hash index
CREATE INDEX <idx> ON <tables_name> USING HASH (<col>);

-- gist:point, box, polygon, tsrange, tsvector, tsquery type ...
CREATE INDEX <idx> ON <tables_name> USING GIST (<geometric_col>);

-- gin
CREATE INDEX <idx> ON <tables_name> USING GIN (<jsonb_col>);

-- brin
CREATE INDEX <idx> ON <tables_name> USING BRIN (<timestamp_cols>);
```

advanced usage of index:
```postgresql
-- index on expr: will store index on expression result and called when these expressions appear in SELECT WHERE, ORDER BY statements...
CREATE INDEX <idx> ON <tables_name> (<expr>);

-- partial index: only inserts rows that satisfy <cond> into the index, then in select query, if the same <cond> appears in SELECT WHERE, this index will be used
CREATE [IF NOT EXISTS] INDEX <idx>
ON <tables_name> (<col1>)
WHERE <cond>;

-- multi-column index: index sequence of multiple columns
-- - support 32 col at max by default, can be adjusted in pg_config_manual.h
-- - index type that support this: btree, GIST, GIN and BRIN
-- - used when the WHERE statement appears subsequence of index sequence joined by AND, such as "col1=v1", "col1=v1 AND col2=v2", ...; if you omit "col1=v1" and just use "col2=v2" in WHERE, index use is not guranteed
CREATE INDEX [IF NOT EXISTS] INDEX <idx>
ON <tables_name> (<col1>, <col2>, <col3>, ...);


```

create index in production environment:
```postgresql
-- avoid blocking write and reading during index build to avoid downtime;
-- if not used, db creates mutual lock during index build
CREATE INDEX CONCURRENTLY <idx> ON <tables_name> (<col>);
```

## 2.2 Full-Text Search (GIN)
Beside elastic search, we can also use `tsvector`, `tsquery` combined with GIN index to perform FTS in DB.


Relevant data type:
- `to_tsvector()`: takes a string, preprocess it into lexeme tokens, returns a sorted list of tokens and their positions and weight within the string
- `to_tsquery()`: takes some keywords joined by search operators and return a search query

GIN indexable operator:

| operator class | indexable operator     | role                                                                     |
| -------------- | ---------------------- | ------------------------------------------------------------------------ |
| tsvector_ops   | @@ (tsvector, tsquery) | evaluate similarity between tsvector and tsquey and return true if match |


Set up FTS:
1. Create database to store text and tsvector:
```postgresql
CREATE TABLE Articles (
	id SERIAL PRIMARY KEY,
	title TEXT NOT NULL,
	article TEXT,
	search_vectors TSVECTOR GENERATED ALWAYS AS 
		(to_tsvector('English', article)) STORED
);
```
2. Create GIN index on tsvector column type:
```postgresql
CREATE INDEX article_fts
ON Articles
USING GIN ( search_vectors );
```

Perform basic FTS Query on databases:
```postgresql
-- use ts_vector @@ ts_query in where to match
SELECT title, article FROM Articles
WHERE search_vectors @@ to_tsquery('<keyword1>');

-- FTS with AND: articles contain both <keyword1> and <keyword2>
SELECT title, article FROM Articles
WHERE search_vectors @@ to_tsquery('<keyword1> & <keyword2>');

-- FTS with OR: articles contain either <keyword1> or <keyword2>
SELECT title, article FROM Articles
WHERE search_vectors @@ to_tsquery('<keyword1> | <keyword2>');

-- FTS with phrases: phrase must be enclosed by double quotes
SELECT title, article FROM Articles
WHERE search_vectors @@ to_tsquery('"<keyword1> <keyword2>"');
```

Advanced FTS query: https://iniakunhuda.medium.com/postgresql-full-text-search-a-powerful-alternative-to-elasticsearch-for-small-to-medium-d9524e001fe0

FTS functions and operators: https://www.postgresql.org/docs/current/functions-textsearch.html

## 2.3 Storing JSON
We can use postgresql to store and index json documents like using MongoDB. The corresponding data type in postgresql is `jsonb`(binary json). We can check key existence and retrieve key value on json documents stored in psql.


> [!EXAMPLE]- Relevant data type: jsonpath, jsonb, array
> jsonpath are a kind of expression on jsonb value. There are 2 types:  SQL-standard JSON path expressions and json path predicate check expressions. The first one return a jsonb data type, while the second one return `true/false/unknown`:
> - SQL-standard json path: has `? ( <cond> )` as filter condition, used with `@?`, example: `'{"a":[1,2,3,4,5]}' @? '$ ?(@.a[*] > 2)'`
> - predicate check json path:  has no `?()` as filter condition, used with `@@`, example: `'{"a":[1,2,3,4,5]}' @@ '$.a[*] > 2'`
> 
> jsonpath symbols:
> - `$`: denote the root value of json value
> - `.*`: returns the values of all members at the top level of current object
> - `.**`: return all member values at all levels
> - `[<index>]`: return the single array element specified by the index
> - `[*]`: return all array elements
> - `?(<cond>)`: filter expression
> - `@`: represent the result of path evaluation, json path are of forms: `<path> ?(<cond>)`, examples of`<path>` include: `$`, `$.<field_name>`
> 
> jsonb are binary json column type. The literal values of such types are json strings with keys and values enclosed by double quotes. Its operators include:
> - `->>`: access a field of json object and return the field as text type
> - `->`: access a field of json object and return the field as jsonb type
> - `#>>`: takes an array of text as the field path and return the field as text type, example: result of `'{"a":[1,2,3],"b":[4,5,6]}'::json#>>'{a,2}'` is 3
> - `#>`: takes an array of text as the field path and return the field as jsonb type, example: result of `'{"a": {"b":{"c": "foo"}}}'::json#>'{a,b}'` is `{"c": "foo"}`

GIN indexable operators:

| operator class | indexable operators     | Role                                                                                                     |
| -------------- | ----------------------- | -------------------------------------------------------------------------------------------------------- |
| array_ops      | && (anyarray, anyarray) | check if 2 arrays share at least 1 element                                                               |
|                | @> (anyarray, anyarray) | check if left array fully contains right array                                                           |
|                | <@ (anyarray, anyarray) | check if right array full contains left array                                                            |
|                | = (anyarray, anyarray)  | check if 2 arrays are equal                                                                              |
| jsonb_ops      | @> (jsonb, jsonb)       | check if the left json document contains the key/value entries from the right json document at top level |
|                | @? (jsonb, jsonpath)    | used with SQL-standard json path, check if the json path return any item from the json document          |
|                | @@ (jsonb, jsonpath)    | used with predicate check json path, behavior N/A                                                        |
|                | ? (jsonb, text)         | key exists in jsonb document at top level                                                                |
|                | ?\| `(jsonb, text[])`   | any key from the array exists in jsonb document at top level                                             |
|                | ?& `(jsonb, text[])`    | all keys from the array exist in jsonb document at top level                                             |
| jsonb_path_ops | @> (jsonb, jsonb)       | same as jsonb_ops @>                                                                                     |
|                | @? (jsonb, jsonpath)    | same as jsonb_ops @?                                                                                     |
|                | @@ (jsonb, jsonpath)    | same as jsonb_ops @@                                                                                     |
jsonb_ops vs jsonb_path_ops:
- jsonb_ops is the default jsonb operator class in gin index and support a wide range of operators as above
- jsonb_path_ops uses an even more optimized GIN Index structure but supports a smaller set of operations as above

Set up database:
1. Create database with `JSONB` type column:
```postgresql
CREATE TABLE data_json (
	id SERIAL PRIMARY KEY,
	data JSONB NOT NULL
);

CREATE TABLE data_arr (
	id SERIAL PRIMARY KEY,
	data TEXT[]
);

INSERT INTO data_json (data) VALUES
('{"name": "Laptop", "specs": {"RAM": "16GB", "storage": "512GB SSD"}, "in_stock": true}'),
('{"name": "Phone", "specs": {"RAM": "8GB", "storage": "256GB"}, "in_stock": false}'),
( jsonb_build_object('first_name', 'papa', 'last_name', 'john', 'address', jsonb_build_object('city', 'New York', 'country', 'CA')) ),
(jsonb_build_object('first_name', 'harry', 'last_name', 'potter', 'address', jsonb_build_object('city', 'London', 'country', 'UK'), 'email', 'abc@123'));
```
2. Create index on `JSONB` column or its field:
```postgresql
-- index JSONB column with jsonb_ops class operator
CREATE INDEX index_json ON data_json
USING GIN ( data );

-- or index on specific field that we are interested of JSONB col with jsonb_path_ops class operator for even more optimization
CREATE INDEX index_json ON data_json
USING GIN (data->> 'last_name' jsonb_path_ops);

-- index on array column
CREATE INDEX index_arr ON data_arr
USING GIN ( data );
```

Perform index query:
```postgresql
-- ->> return a field as jsonb type, -> return a field as text type
SELECT data ->> 'first_name' first_name,
	data ->> 'last_name' last_name
	FROM data_json
	WHERE data @> '{"last_name": "john"}';

-- equivalent to above query
SELECT data ->> 'first_name' first_name,
	data ->> 'last_name' last_name
	FROM data_json
	WHERE data->'last_name' @> '"john"';

-- for nonexistent field, query return null value
-- return ['papa', 'john', null, 'CA']
SELECT data ->> 'first_name' first_name,
	data ->> 'last_name' last_name,
	data ->> 'email' email,
	data ->'address' ->>'country' county
	FROM data_json
	WHERE data->'address' @> '{"city": "New York"}';
```

## 2.4 b-tree index

indexable operators: =, <, <=, >, >=


# 3. Policy, Constraint & Tigger

## 3.1 Policy
For each table, we define policies to control specific rows permission to certain users

```postgresql
CREATE POLICY <policy_name> ON <tables_name>
	[AS <PERMISSIVE | RESTRICTIVE>]
	[FOR < ALL | SELECT | INSERT | UPDATE | DELETE>]
	[TO < role_name | PUBLIC | CURRENT_ROLE | CURRENT_USER >]
	[USING <using_cond>]
	[WITH CHECK <check_cond>]
```

example:
```postgresql
-- required step to create policies
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- create policy that allows user to do any operation on rows with username
-- equal to postgres, the expression after USING is similar to where condition in select
CREATE POLICY user_policy ON users
FOR ALL
USING users.user_name = 'postgres';
```

## 3.2 Trigger
triggers are functions that automatically execute in response to INSERT, UPDATE， DELETE or TRUNCATE on a table. Trigger functions are comprise of sql and the response is triggered before/after/instead of the event of insert/update/delete/truncate

```postgresql
-- define trigger function
CREATE OR REPLACE FUNCTION <trigger_function>() RETURNS TRIGGER AS $$
BEGIN
    -- trigger logic here, e.g., logging changes or modifying NEW/OLD rows
    RETURN NEW; -- or OLD, or NULL depending on trigger type and timing
END;
$$ LANGUAGE plpgsql;

-- define when trigger is triggered
CREATE TRIGGER trigger_name
<BEFORE | AFTER | INSTEAD OF> <INSERT | UPDATE | DELETE | TRUNCATE>
ON table_name
[FOR EACH <ROW | STATEMENT>]
[WHEN (condition)]
EXECUTE FUNCTION trigger_function();
```

example:
```postgresql
-- define trigger function
CREATE OR REPLACE FUNCTION audit_log() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO Audit(emp_ID, entry_date) VALUES (NEW.ID, current_timestamp)
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- trigger
CREATE TRIGGER audit_trigger
AFTER INSERT
ON Company
FOR EACH ROW
EXECUTE FUNCTION audit_log();
```

## 3.3 Constraint
types:
- check constraint
- not null constraint
- unique constraint
- primary keys
- foreign keys
- exclusive constraint

```postgresql
-- price, discountedPrice are 2 cols of table product
ALTER TABLE product
ADD CONSTRAINT valid_discount CHECK (price > discountedPrice);

-- not null constraint
ALTER TABLE product
ALTER COLUMN <col> SET NOT NULL;

-- unique constriant: create unique index using b+tree and only b+tree type index supports unique index
ALTER TABLE product
ADD CONSTRAINT unique_constraint UNIQUE (<col1>, <col2>...);

-- primary key constraint: create b+tree index which is the only index type that supports primary key constraint
ALTER TABLE product
ADD CONSTRAINT <constrain_name> PRIMARY KEY (<col1>, <col2>...);

-- foreign constraint, available action includes: NO ACTION(default), RESTRICT, CASCADE, SET NULL, SET DEFAULT
ALTER TABLE <child_table>
ADD CONSTRAINT <constrain_name>
FOREIGN KEY (<col1>, <col2>, ...)
REFERENCES <parent_table> (<parent_col1>, <parent_col2>, ...)
ON <available_action>;

-- exclude constraint specifies 2 rows cannot exist at the same time if they meet certain conditions, this constraint automatically creates index like gist/b-tree/hash
-- syntax:
CREATE EXTENSION IF NOT EXISTS btree_gist; -- required step
ALTER TABLE <tables_name>
ADD CONSTRAINT <constrain_name>
EXCLUDE USING gist (
	-- common operator includes tsrange(timestamp_col1, timestamp_col2) with &&, regular column with =
	<col1> WITH <operator1>,
	<col2> with <operator2>
)
-- we first apply WHERE condition to filter out the rows we apply exclude
[WHERE (<cond>)];

-- example: same room cannot be booked if the time interval overlaps, 
--          only applies to rooms that are not canceled
CREATE EXTENSION IF NOT EXISTS btree_gist; -- required step
ALTER TABLE reservation
ADD CONSTRAINT <constrain_name>
EXCLUDE USING GIST (room_id WITH =, TSRANGE(start_date, end_date) WITH &&)
WHERE (booking_status != 'CANCELED');
```


# 4. Transaction
transaction: a sequence of sql operations executed as a single unit.

Principles implemenetd by transactions(ACID):
- Atomicity: all sqls within the transaction block either executed entirely or either not executed at all
- Consistency: all tables data must follow the defined rules/constraints before or after transactions
- Isolation: multiple transactions should not interfere with each other at the same when access the same resources, isolation level can be adjusted in `BEGIN` command below
- Durability: once a txn is committed, changes are permanent.

Database anomaly resulted by diff levels of transaction isolation:
- Dirty read: read uncommitted data by another transaction, usually don't happen in postgresql because every query is wrapped in `READ COMMITTED` transaction.
- non-repeatable read: a transaction reads the same row multiple times but gets different values because another concurrent transactions modification, can be solved by setting the read transaction level to be `REPEATABLE READ` 
- phantom read: a transaction executes a query and then again, but get different set of rows because another concurrent transactions insert/delete the tables, can be solved by setting read transaction

transaction related command:

| COMMAND                                                                         | role                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BEGIN [ISOLATION LEVEL < READ COMMITED \| REPEATABLE READ \| SERIALIZABLE > ]` | Marks the beginning of a transaction block with following increasing isolation level:<br>- READ COMMITED: A query only sees data committed before the query began. Two consecutive queries within the same transaction can see different data if another transaction commits changes in between.<br>- REPEATABLE READ: all queries within a single transaction see a stable snapshot of the data as it was at the _start_ of the transaction<br>- SERIALIZABLE: all queries within a single can not just see the row values as it was at the start of the transaction but also the row set is fixed. |
| COMMIT                                                                          | submit the transaction to datab                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ROLLBACK                                                                        | cancel all changes of the current transaction b                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `SAVEPOINT <name>`                                                              | Create a savepoint within the transaction to rollback                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `ROLLBACK TO <savepoint_name>`                                                  | rollback to the previously defined sav                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |


# 5. SQL Optimization
## 5.1 EXPLAIN
EXPLAIN is a command that can return the query plan of a given query but does not execute the query. `EXPLAIN ANALYZE` can not just return the query plan but also return the real execution time of the query plan.

How to use `EXPLAIN`:
```postgresql
-- syntax
EXPLAIN <query>
EXPLAIN ANALYZE <query>

-- example:
EXPLAIN SELECT Token.name FROM public.Token;
```

Output:
```text
QUERY PLAN
---
Seq Scan on "Token"  (cost=0.00..394.91 rows=13591 width=11)
```
The result of query plan is executed from inner to outermost. Each step of query plan is represented by`<STEP>(cost=<initial_cost>..<total_cost> rows=<row_num> width=<col_size>)`

| Metric       | role                                                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| initial_cost | How many milli seconds does it take to fetch the first page of the table, factors that influence this metric include order by, aggregate function |
| total_cost   | Total amount of time sql_server thinks will take(EXPLAIN does not really execute the sql)                                                         |
| row_num      | an estimate of number of rows of the table                                                                                                        |
| col_size     | estimate avg sum of all the bytes of the columns                                                                                                  |
query plan steps(`<Step>`):

| Step                                         | role                                                  |
| -------------------------------------------- | ----------------------------------------------------- |
| `Bitmap Index Scan on <table>`               | where condition on indexed column                     |
| `Bitmap Heap Scan on <table>`                | non-indexed column of index scan rows                 |
| `Seq Scan on <table> [Filter:]`              | select based on non indexed where condition           |
| Hash(cost=...)                               | temporary store the scan results in hashtable         |
| `Hash Join(cost=...) Hash Cond: <join_cond>` | Join 2 tables based on the sql join condition         |
| `Sort (cost=...) Sort Key:<orderby_column>`  | order the result based on the column after `order by` |

# 7. Extensions
Extensions are just like libraries that provide additional functions.

How to check extensions:
```postgresql
-- list of all available extensions that can be enabled
SELECT * FROM pg_available_extensions;

-- list of enabled extensions in your database
SELECT * FROM pg_extension;
```

Enable an extension:
```postgresql
CREATE EXTENSION IF NOT EXISTS <extensions_name>;
```

# 6. Non-relational type
other database types:
- hashtable: Reddis
- documents: MongoDB
- column: Cassandra, Hbase
- graph: Neo4j