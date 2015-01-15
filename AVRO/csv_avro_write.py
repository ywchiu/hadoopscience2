from avro import schema, datafile, io
import pprint
import csv
import json

OUTFILE_NAME = 'output/product.avro'
INPUT_SCHEMA_NAME = 'product2.avsc'

fo = open(INPUT_SCHEMA_NAME, "r+")
SCHEMA_STR = fo.read();
print "Read String is : ", SCHEMA_STR
fo.close()

SCHEMA = schema.parse(SCHEMA_STR)

rec_writer = io.DatumWriter(SCHEMA)

df_writer = datafile.DataFileWriter(
    open(OUTFILE_NAME, 'wb'),
    rec_writer,
    writers_schema = SCHEMA
)

csvfile = open('sample.csv', 'r')

fieldnames = ("product_id","product_name")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    dt =  row
    df_writer.append(dt)
df_writer.close()