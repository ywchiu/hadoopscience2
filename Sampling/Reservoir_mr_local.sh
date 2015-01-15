$k=3; for i in {1..100}; do echo $i; done | ./rand_subset_m.py $k | sort -k1,1n | ./rand_subset_r.py $k
