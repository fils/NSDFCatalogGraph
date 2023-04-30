import pandas as pd
import pyarrow as pa
import os
import pyarrow.parquet as pq

new_schema = pa.schema([
    ('repository', pa.string()),
    ('collection', pa.string()),
    ('name', pa.string()),
    ('size', pa.int64()),
    ('lastmodified', pa.string()),
    ('etag', pa.string())
])

csv_column_list = ['repository', 'collection', 'name', 'size', 'lastmodified', 'etag']

# set the directory path you want to process
fps = []
dp = "/mnt/wdb/Data/NSDF/csv"

# recursively search the directory and its subdirectories for files
for root, directories, files in os.walk(dp):
    for filename in files:
        fps.append(os.path.join(root, filename))

# process the files
for fp in fps:
    wp = fp.replace("csv", "parquet").replace(".gz", "") # cheesy way to do this...  has to be something better
    wpp = os.path.dirname(wp)
    if not os.path.exists(wpp):
        os.makedirs(wpp)
    # print("{} to {}".format(fp, wp))
    try:
        with pq.ParquetWriter(wp, schema=new_schema) as writer:
            with pd.read_csv(fp, header=None, names=csv_column_list, chunksize=100000) as reader:
                for df in reader:
                    # transformation: transform df by adding a new static column with column name 'newcol' and value 9999999
                    # df['newcol'] = 9999999
                    # convert pandas df to record batch
                    transformed_batch = pa.RecordBatch.from_pandas(df, schema=new_schema)
                    writer.write_batch(transformed_batch)
    except Exception as e:
        print("{} to {}".format(fp, wp))
        print("An error occurred: ", e)