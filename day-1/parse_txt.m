function [list1, list2] = parse_txt()
    fileID = fopen('input.txt','r');
    sizeA = [2 Inf];
    A = fscanf(fileID, '%d', sizeA);
    list1 = A(1,:);
    list2 = A(2,:);
    fclose(fileID);
end