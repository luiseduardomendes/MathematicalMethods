function [x] = JacobiMethod(A, b, x0, TOL, MAX_IT)
    n = size(b, 1);
    cont = 0;
    while cont < MAX_IT do
        x_1 = x0;
        for i = 1:n do
            k = b(i);
            for j = 1:n do
                if j ~= i then
                    k = k - A(i, j) * x0(j);
                end
            end
            x(i) = k / A(i, i);
        end
        x0 = x;
        if norm(x_1 - x0, 'inf') < TOL then
            break;
        end
        cont = cont + 1;
    end
endfunction

function [x] = Gauss_Scidel(A, b, x0, TOL, MAX_IT)
        n = size(b, 1);
    cont = 0;
    while cont < MAX_IT do
        x_1 = x0;
        for i = 1:n do
            k = b(i);
            for j = 1:n do
                if j ~= i then
                    k = k - A(i, j) * x0(j);
                end
            end
            x0(i) = k / A(i, i);
        end
        if norm(x_1 - x0, 'inf') < TOL then
            break;
        end
        cont = cont + 1;
    end
    x = x0;
endfunction

function [x] = JacobiMethodChanged(A, b, x0, TOL, MAX_IT)
    n = size(b, 1);
    cont = 0;
    while cont < MAX_IT do
        x_1 = x0;
        for i = 1:n do
            k = b(i);
            for j = 1:n do
                if j ~= i then
                    k = k - A(i, j) * x0(j);
                end
            end
            x(i) = k / A(i, i);
        end
        x0 = x;
        if norm(x_1 - x0, 'inf') < TOL then
            break;
        end
        cont = cont + 1;
    end
endfunction