hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.5.0-cdh5.2.0.jar \
 -D mapred.reduce.task=1 \
 -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator  \
 -D mapred.text.key.comparator.options=-n \
-file ./rand_subset_m.py -mapper "rand_subset_m.py 10" \
-file ./rand_subset_r.py -mapper "rand_subset_r.py 10" \
-input test.txt -output test5
