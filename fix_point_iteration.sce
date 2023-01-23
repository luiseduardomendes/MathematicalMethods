function [x0] = root_calculation(f, x, sig_digit)
    num_it = 0;
    deff('y = f(x)', f);
    tol = 0.5 * 10^(-sig_digit);
    max_it = 100 * 10 ^ (sig_digit);
    
    if abs(diff(f, x)) > 1 then
        disp('initial point not valid')
        x0 = %nan;
        return
    end
    
    while abs(f(x) - x) > tol & num_it < max_it 
        //disp([x, f(x), abs(f(x) - x)/(1-((f(x+0.00000005) - f(x))/0.00000005))]);
        x = f(x);
        num_it = num_it + 1;
    end
    if abs(f(x) - x) < tol
        x0 = f(x);
    else
        disp('function diverges')
        x0 = %nan
    end

endfunction

function [x0] = diff(f, x)
    x0 = (f(x+0.00000005) - f(x))/0.00000005;
endfunction

function [x0] = colebrook_white_equation(Re, Rh, eps)
    x0 = root_calculation(- 2 * log10(eps/(14.8*Rh) + 2.51/Re, )
endfunction
