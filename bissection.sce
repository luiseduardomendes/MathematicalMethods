function [p] = bissection(f, a, b, TOL, N)
    i = 0;
    while (i < N)
        p = (a + b)/2;
        fa = f(a);
        fp = f(p);
        if (fp == 0 | (b-a)/2 < TOL) then
            disp(i);
            return 
        end
        if (fa * fp < 0) then
            b = p;
        else
            a = p;
        end        
        i = i + 1;
    end
    error('Iteration limit exceed!');
end
