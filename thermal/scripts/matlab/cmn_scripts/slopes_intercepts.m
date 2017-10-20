xr1 = 120; xr2 = 150; c = 0;
Riu = Bin_unique; 
Rim = Bmean;
for x= xr1:xr2
    xi = x;
    fi = find (xi == Riu);
    yi = (Rim(fi));
    ci = yi - xi;
    c = c + ci/(xr2-xr1);
end
fprintf ( "intercept: %d \n",c);

xr1 = 105; xr2 = 108; 
c = 0; mi = 0; xold = 0; yold = 0;
for x= xr1:xr2
    xi = x;
    fi = find (xi == Riu);
    yi = (Rim(fi));
    mt = 0;
    if ( x > xr1 )
        mt = (yold - yi)/(xold - xi); 
    end
    xold = xi; yold = yi;
    mi = mi + mt/(xr2 - xr1);
end
    c = yold - (mi * xold);
fprintf ( "slope:%d, intercept: %d \n",mi,c);

