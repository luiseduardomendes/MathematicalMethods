function [X] = gaussian_elimination(A)
    i = size(A, 1);
    disp(A(:,1:i));
    disp(det(A(:,1:i)));
    if (det(A(:,1:i)) == 0) then
        X = [%nan; %nan; %nan];
    else
        A = matrix_triangulation(A);
        A = pivot_unit(A);
        A = isolate_pivots(A);
        
        X = A(:, i+1);
    end

endfunction

function [X] = partial_pivot(A, cur_line)
    maior = A(cur_line, :)
    index = cur_line;
    for line = cur_line+1:i
        if abs(A(line, cur_line)) > abs(maior(cur_line)) then
            maior = A(line, :)
            index = line;
        end
    end
    A = swap_line(A, cur_line, index);
    X = A
endfunction

function [X] = reorder_matrix(A)
    i = size(A, 1);
    for cur_line = 1:i-1
        A = partial_pivot(A, cur_line);
    end
    X = A
endfunction

function [X] = matrix_triangulation(A)
    for cur_line = 1:i-1
        A = partial_pivot(A, cur_line);
        for line = cur_line+1:i
            A(line, :) = A(line, :) - (A(line, cur_line) / A(cur_line, cur_line)) * A(cur_line, :);
        end
    end
    X = A
endfunction

function [X] = pivot_unit(A)
    for line = 1:i
        A(line, :) = A(line, :) / A(line, line);
    end
    X = A
endfunction

function [X] = isolate_pivots(A)
    cur_line = i - 1;
    while cur_line > 0
        for col = i : -1 : cur_line+1
            cte =  A(cur_line, col) / A(col, col);
            A(cur_line, :) = A(cur_line, :) - cte * A(col, :);
        end 
        cur_line = cur_line - 1;
    end
    X = A
endfunction

function [X] = swap_line(A, i1, i2)
    temp = A(i2,:);
    A(i2,:) = A(i1,:);
    A(i1,:) = temp;
    X = A;
endfunction

