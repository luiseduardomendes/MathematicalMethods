function [] = plotter(f, a, b, gtitle, ylab)
    if ~exists('gtitle', 'local') then
        gtitle = ""
    end
    if ~exists('ylab', 'local') then
        ylab = "y"
    end
    x = linspace(a, b, 1000);
    xgrid();    
    xlabel('x');
    ylabel(ylab);
    title(gtitle);
    plot(x, f(x));
endfunction
