function [x] = TridiagonalMatrixSolve(A, b)
    // Ax = b 
    n = size(A, 1);
    
    [a_, b_, c_] = SplitMatrix(A);
    d_ = b;
    
    cl = zeros(n, 1);
    dl = zeros(n, 1);

    cl(1) = c_(1)/b_(1);
    for i = 2:n 
        cl(i) = c_(i)/ (b_(i)-a_(i)*cl(i-1));
    end
    
    dl = d_(1) / b_(1);
    for i = 2:n
        dl(i) = (d_(i) - a_(i)*dl(i-1))/(b_(i) - a_(i)*cl(i-1));
    end
    
    x_(n) = dl(n);
    for i = n-1:-1:1
        x_(i) = dl(i) - cl(i) * x_(i+1);
    end
    
    x = x_;
endfunction

function [x, y, z] = SplitMatrix(A)
    a_ = zeros(n,1);
    b_ = zeros(n,1);
    c_ = zeros(n,1);
    
    for i = 1:n
        b_(i) = A(i, i);
        if i == 1 then
            a_(i) = 0
            c_(i) = A(i,i+1);
        elseif i == n then
            a_(i) = A(i,i-1);
            c_(i) = 0;
        else
            a_(i) = A(i,i-1);
            c_(i) = A(i,i+1);
        end
    end
    
    x = a_;
    y = b_;
    z = c_;
endfunction
