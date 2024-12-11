% list1 = [3,4,2,1,3,3]
% list2 = [4,3,5,3,9,3]
[list1, list2] = parse_txt();
sim_score = [];

for num = list1
    sim_score = [sim_score num*size(find(list2 == num), 2)];
end

result = sum(sim_score)
