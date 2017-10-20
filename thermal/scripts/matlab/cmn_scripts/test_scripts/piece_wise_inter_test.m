
x = [1, 2,   3,   4, 5,     6,   7,  8;]';
y = [2, 4.1, 5.9, 8, 10.2, 11.8, 13.8,16;]';
xi = (1:0.25:4)';
disp( size(xi));
p = polyfit ( x,y,1);

%yi = interp1(x,y,xi,'linear');
%yi = fit(x,y,'linearinterp');
yi = polyval(p,x);

disp(yi(1));

% disp( yi );
figure; axis square;markerStr = strcat('r*'); hold on;
% plot( yi, x , y);
plot( x, y, 'r*' ) 
plot( x , yi,'o')

hold off;

%plot ( x,y,'r*',xi,yi);
% 
% yfit = fit ( x,y,'linearinterp');
% plot (yfit, x,y);


