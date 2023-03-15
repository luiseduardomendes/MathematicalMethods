function [x, y] = eigenvalue_calculation(A, x1, TOL, MAX_IT)
    x = x1
    
    y_prev = x' * A * x;
    x = A * x / norm(A * x, 2);
    y = x' * A * x;
    
    cont = 1;
    while(abs(y_prev - y) > TOL && cont < MAX_IT) do
        y_prev = y;
        x = A * x / norm(A * x, 2);
        y = x' * A * x;
    end
endfunction
