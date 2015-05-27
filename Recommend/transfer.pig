recommend_result = LOAD 'small_recommend/part-*' USING PigStorage() AS (userid:int, recommend:chararray);
STORE A INTO 'recommender' USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('mycf:recommend_list');
