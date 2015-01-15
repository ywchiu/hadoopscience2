from avro import schema, datafile, io
import pprint
import xmltodict, json

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

o = xmltodict.parse(file('sample.xml'))
df_writer.append(o['data'])
df_writer.close()
