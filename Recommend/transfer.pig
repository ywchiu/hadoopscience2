A = load 'small_recommend/part-*' Using PigStorage() as (userid:int, recommend:chararray);
STORE A INTO 'mydata' USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('mycf:recommend_list');
