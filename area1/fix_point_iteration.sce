function [x0] = root_calculation(f, x, sig_digit)
    num_it = 0;
    tol = 0.5 * 10^(-sig_digit);
    max_it = 100 * 10 ^ (sig_digit);
    
    
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
