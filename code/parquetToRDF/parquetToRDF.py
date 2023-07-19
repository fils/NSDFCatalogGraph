import pandas as pd
import pyarrow as pa
import os
import pyarrow.parquet as pq
import json
from pyld import jsonld
from pyld import documentloader


# Simple program to read a parquet file and convert it to schema.org
# following FROF patterns and profiles
def myloader(*args, **kwargs):
    requests_loader = documentloader.requests.requests_document_loader(*args, **kwargs)

    def loader(url, options={}):
        options['headers']['Accept'] = 'application/ld+json'
        return requests_loader(url, options)

    return loader


def generate_json_ld(repository, collection, name, size, lastmodified, etag):
    # Create a dictionary representing the JSON-LD object

    # context = {
    #     "@vocab": "http://schema.org/",
    #     "name": "name",
    #     "description": "description",
    #     "url": "url"
    # }

    context =  [
        "https://schema.org",
        "https://www.w3.org/ns/pub-context"
    ]


    json_ld = {
        "@context": [
        "https://schema.org",
        "https://www.w3.org/ns/pub-context"
        ],
        "@type": "DigitalDocument",
        "conformsTo": "https://example.com/cdifspec",
        "name": name,
        "producer": repository,
        "isPartOf": collection,
        "publishingPrinciples": [
            {
            "@type": "CreativeWork",
            "url": "https://example.org/id/policy",
            "name": "Digital Object Policy",
            "description": "A description of the digital object policy"
            }
        ],
        "encoding": {
            "@type": "MediaObject",
            "sha256": etag,
            "contentSize": size
        },
        "distribution": "https://example.org/datasets/1234567890",
        "dateModified": lastmodified
    }

    # jsonld.set_document_loader(myloader())

    # compacted = jsonld.compact(json_ld, context)
    json_ld_str = json.dumps(json_ld, indent=2)

    return json_ld_str


new_schema = pa.schema([
    ('repository', pa.string()),
    ('collection', pa.string()),
    ('name', pa.string()),
    ('size', pa.int64()),
    ('lastmodified', pa.string()),
    ('etag', pa.string())
])

csv_column_list = ['repository', 'collection', 'name', 'size', 'lastmodified', 'etag']
file_path = "/mnt/wdb/Data/NSDF/parquet/mdf/w_14_v1.1.parquet"

# Read the Parquet file using pyarrow
table = pq.read_table(file_path)

# Convert the table to a Pandas DataFrame
df = table.to_pandas()

# Filter the DataFrame to keep only the specified columns
df = df[csv_column_list]

# Iterate through each row and print the values
for index, row in df.iterrows():
    # print(row['repository'], row['collection'], row['name'], row['size'], row['lastmodified'], row['etag'])
    fn = "/mnt/wdb/Data/NSDF/graphs/{}{}.json".format(row['repository'], index)
    # print(fn)
    json_ld_output = generate_json_ld(row['repository'], row['collection'], row['name'], row['size'], row['lastmodified'], row['etag'])
    with open(fn, 'w') as file:
        file.write(json_ld_output)
    
    # print(json_ld_output)

# # Example usage
# repository = "The repository"
# collection = "The collection"
# name = "DO name"
# size = "DO size"
# lastmodified = "Last mod"
# etag = "etag value"
# 
# json_ld_output = generate_json_ld(repository, collection, name, size, lastmodified, etag)
# print(json_ld_output)
