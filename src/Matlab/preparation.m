clear normalized2
clear A
clear B
normalized2 = normalized(940:1319, :);
normalized3 = normalized(1:940, :);

for i = 1:940
    sequenz2{i, 1} = normalized3(i, :);
end

for i = 1:size(sequenz2, 1)
    B2(i, :) = sequenz2{i};
end

j = 1;

for i = 1:20:380
    sequenz{j, 1} = normalized2(i:i + 19, :);
    j = j + 1;
end

laenge = size(sequenz{1, 1}, 1)*size(sequenz{1, 1}, 2);

for i = 1:size(sequenz, 1)
    A{i} = reshape(sequenz{i,1}, [laenge, 1]);
end

clear B

for i = 1:size(sequenz, 1)
    B(i, :) = A{i};
end

plot(B(1, :))
plot(B2(1, :))