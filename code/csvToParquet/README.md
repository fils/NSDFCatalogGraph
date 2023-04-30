# CSV to Parquet

## About

This is just a simple bit code to convert the .csv.gz files I got from
the catalog into a set of parquet files.  These can then be fronted
with Arrow or DuckDB etc.  

## CSV Schemas

This is the eventual schema these data seem destined for 
based on the paper * [NSDF-Catalog: Lightweight Indexing Service for Democratizing Data Delivery](https://www.sci.utah.edu/publications/Lue2022a/catalog.pdf).

```
1 CREATE TABLE nsdf.catalog
2 (
3 ‘repository‘ String,
4 ‘collection‘ String,
5 ‘name‘ String,
6 ‘size‘ Int64,
7 ‘last_modified‘ Nullable(String),
8 ‘etag‘ Nullable(String)
9 )
10 ENGINE = MergeTree
11 ORDER BY (repository, collection)
12 SETTINGS index_granularity = 8192
```

So a parquet schema would look like 

```python
new_schema = pa.schema([
    ('repository', pa.string()),
    ('collection', pa.string()),
    ('name', pa.string()),
    ('size', pa.int64()),
    ('lastmodified', pa.string()),
    ('etag', pa.string())
])
```
