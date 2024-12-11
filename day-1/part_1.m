% list1 = [3,4,2,1,3,3]
% list2 = [4,3,5,3,9,3]
[list1, list2] = parse_txt();

list1srtd = sort(list1)
list2srtd = sort(list2)

dist = abs(list1srtd-list2srtd);
total_dist = sum(dist)
