# DuckDB

## About

This is just a quick not on the use of the DuckDB package for 
doing queries over a set of parquet files built from the CSVs
via the code in [csvToParquet](../csvToParquet).

As stated by the web site [https://duckdb.org/](https://duckdb.org/)
DuckDB is an in-process SQL OLAP database management system.

We can use it over parquet files via the read_parquet as in

```bash
❯ duckdb

v0.7.1 b00b93f0b1
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D SELECT * FROM read_parquet('./digitalrocksportal/*.parquet', filename=true)  order by lastmodified DESC limit 10;
```

with a result set such as

```bash
┌────────────────────┬───────────────┬──────────────────────────────┬────────────┬───────────────────────────────┬─────────────────────┬──────────────────────────────────┐
│     repository     │  collection   │             name             │    size    │         lastmodified          │        etag         │             filename             │
│      varchar       │    varchar    │           varchar            │   int64    │            varchar            │       varchar       │             varchar              │
├────────────────────┼───────────────┼──────────────────────────────┼────────────┼───────────────────────────────┼─────────────────────┼──────────────────────────────────┤
│ digitalrocksportal │ /projects/31  │ /media/projects/31/origin/…  │        162 │                               │                     │ ./digitalrocksportal/31.parquet  │
│ digitalrocksportal │ /projects/364 │ /media/projects/364/origin…  │ 1789573584 │ Wed, 30 Jun 2021 15:43:17 GMT │ "60dc9115-6aaab9d0" │ ./digitalrocksportal/364.parquet │
│ digitalrocksportal │ /projects/364 │ /media/projects/364/origin…  │ 1777342083 │ Wed, 30 Jun 2021 15:41:18 GMT │ "60dc909e-69f01683" │ ./digitalrocksportal/364.parquet │
│ digitalrocksportal │ /projects/364 │ /media/projects/364/origin…  │ 1784143351 │ Wed, 30 Jun 2021 15:39:23 GMT │ "60dc902b-6a57ddf7" │ ./digitalrocksportal/364.parquet │
│ digitalrocksportal │ /projects/364 │ /media/projects/364/origin…  │ 1779058053 │ Wed, 30 Jun 2021 15:35:42 GMT │ "60dc8f4e-6a0a4585" │ ./digitalrocksportal/364.parquet │
│ digitalrocksportal │ /projects/364 │ /media/projects/364/origin…  │ 1801956989 │ Wed, 30 Jun 2021 15:33:28 GMT │ "60dc8ec8-6b67ae7d" │ ./digitalrocksportal/364.parquet │
│ digitalrocksportal │ /projects/364 │ /media/projects/364/origin…  │ 1921300167 │ Wed, 30 Jun 2021 15:30:35 GMT │ "60dc8e1b-7284b6c7" │ ./digitalrocksportal/364.parquet │
│ digitalrocksportal │ /projects/364 │ /media/projects/364/origin…  │ 1766662792 │ Wed, 30 Jun 2021 15:28:12 GMT │ "60dc8d8c-694d2288" │ ./digitalrocksportal/364.parquet │
│ digitalrocksportal │ /projects/364 │ /media/projects/364/origin…  │ 1724268657 │ Wed, 30 Jun 2021 15:26:11 GMT │ "60dc8d13-66c64071" │ ./digitalrocksportal/364.parquet │
│ digitalrocksportal │ /projects/364 │ /media/projects/364/origin…  │ 1600573974 │ Wed, 30 Jun 2021 15:23:46 GMT │ "60dc8c82-5f66d216" │ ./digitalrocksportal/364.parquet │
├────────────────────┴───────────────┴──────────────────────────────┴────────────┴───────────────────────────────┴─────────────────────┴──────────────────────────────────┤
│ 10 rows                                                                                                                                                       7 columns │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
D
```

This is used as a simple approach to doing inspection of the files to explore
connections between the NSDF Catalog and a domain graph.





