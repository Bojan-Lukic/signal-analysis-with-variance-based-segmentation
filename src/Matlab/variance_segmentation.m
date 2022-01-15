close all;
clearvars -except normalized
normalized1 = normalized(1:940, :);
normalized2 = normalized(940:1319, :);

for i = 1:940
    sequenz{i, 1} = normalized1(i, :);
end

laenge = size(sequenz{1, 1}, 1)*size(sequenz{1, 1}, 2);

for i = 1:size(sequenz, 1)
    A{i} = reshape(sequenz{i,1}, [laenge, 1]);
end

for i = 1:size(sequenz, 1)
    B(i, :) = A{i};
end


for i = 1:940
    minimum = min(B(i, :));
    minimumlist(i) = minimum;
    B2(i, :) = B(i, :) - minimum;
end    

globmax = max(B2, [], 'all');
j = 1;

for i = 1:940
    if max(B2(i, :)) > 0.6*globmax
        B3(j, :) = B2(i, :) + minimumlist(i);
        j = j + 1;
    end
end


B3 = B3(24, :);
len = length(B3(1, :));
preseg = [floor(1/4*len), floor(1/2*len), floor(3/4*len)];
    
var_segments = var_segmentation(B3, preseg);

figure;
hold on
for i = 1:length(B3(:, 1))
    plot(B3(i, :));
end    
grid on;
title('Filtered processes with segmentation lines');
xlabel('Reading point p');
ylabel('Signal range r');
for i = 1:length(var_segments)
    xline(var_segments(i), '--r')
end
hold off


function var_segments = var_segmentation(matrix, preseg)
    
    if (isempty(preseg))
        leng = length(matrix(1, :));
        preseg = [floor(leng/4), floor(leng/2), floor(3*leng/4)];
    elseif length(preseg) < 2
        print("Need a minimum of 3 segments")
        var_segments = preseg;
        return
    end
    
    var_segments = preseg;
    thresh = 0;
    
    while thresh < 3
        for i = 1:length(var_segments)
            if i == 1
                tempvar = sum(var(matrix(:, 1:var_segments(i)))) + sum(var(matrix(:, var_segments(i):var_segments(i + 1))));
                index = var_segments(i);
                for j = 2:var_segments(i + 1) - 2
                    tempvar2 = sum(var(matrix(:, 1:j))) + sum(var(matrix(:, j:var_segments(i + 1))));
                    if tempvar2 < tempvar
                        tempvar = tempvar2;
                        index = j;
                        thresh = 0;
                    end
                end
            elseif i == length(var_segments)
                tempvar = sum(var(matrix(:, var_segments(i - 1):var_segments(i)))) + sum(var(matrix(:, var_segments(i):length(matrix(1, :)))));
                index = var_segments(i);
                for j = var_segments(i - 1) + 2:length(matrix(1, :)) - 2
                    tempvar2 = sum(var(matrix(:, var_segments(i - 1):j))) + sum(var(matrix(:, j:length(matrix(1, :)))));
                    if tempvar2 < tempvar
                        tempvar = tempvar2;
                        index = j;
                        thresh = 0;
                    end
                end
            else
                tempvar = sum(var(matrix(:, var_segments(i - 1):var_segments(i)))) + sum(var(matrix(:, var_segments(i):var_segments(i + 1))));
                index = var_segments(i);
                for j = var_segments(i - 1) + 2:var_segments(i + 1) - 2
                    tempvar2 = sum(var(matrix(:, var_segments(i - 1):j))) + sum(var(matrix(:, j:var_segments(i + 1))));
                    if tempvar2 < tempvar
                        tempvar = tempvar2;
                        index = j;
                        thresh = 0;
                    end
                end
            end
            
            var_segments(i) = index;
        end
        
        thresh = thresh + 1;
    end    
end