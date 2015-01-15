from avro import schema, datafile, io
import pprint

OUTFILE_NAME = 'output/product.avro'
INPUT_SCHEMA_NAME = 'product.avsc'

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

df_writer.append( {"product_id":1000,"product_name":"Hugo Boss XY","product_description":"Hugo Xy Men 100 ml","product_status":"AVAILABLE","product_category":["fragrance","perfume"],"price":10.35,"product_hash":"XY123"})

df_writer.append( {"product_id":1001,"product_name":"Hugo Men Red","product_description":"Hugo Men Red 150 ml","product_status":"ONLY_FEW_LEFT","product_category":["fragrance","perfume"],"price":12.99,"product_hash":"XY456"})

df_writer.append( {"product_id":2000,"product_name":"Cherokee Polo T Shirt","product_description":"Cherokee Medium Blue Polo T Shirt","product_status":"AVAILABLE","product_category":["T-shirts","V-Neck","Cotton","Medium"],"price":50.0,"product_hash":"XY789"})

df_writer.append( {"product_id":2001,"product_name":"Ruggers Smart","product_description":"Ruggers Smart White Small Polo T Shirt","product_status":"ONLY_FEW_LEFT","product_category":["T-shirts","Round-Neck","Woolen","Small"],"price":9.99,"product_hash":"XY987"})

df_writer.close()