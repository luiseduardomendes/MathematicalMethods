function [x] = newton_raphson_method(f, x0, tol)
    while abs(f(x0)) < tol
        x0 = calc_next_x(f, x0);
    end
    x = x0;
endfunction

function [x] = calc_next_x (f, x0)
    x = x0 - f(x0) / diff(f, x0);
endfunction

function [x] = diff(f, x0)
    h = 1*10^-30;
    x = (f(x + h) + f(x)) / h;
endfunction
