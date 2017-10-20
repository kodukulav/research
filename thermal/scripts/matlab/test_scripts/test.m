
% x2 = [1,4,5,6];
% y = [20,30,40,50];
% 
% figure(); axis square;
% plot(x2,y,'-.r*');
% xbounds = xlim();
% set(gca, 'xtick', xbounds(1):0.25:xbounds(2))
% set(gca,'position',[0.05 0.08 0.8 0.9])
% saveas(gcf,'./test.bmp');
% % set(gca,'xticklabel',x.');

% Riu = Gin_unique; 
% Rim = Gmean;
% xr1 = 75; xr2 = 105; c = 0;
% for x= xr1:xr2
%     xi = x;
%     fi = find (xi == Riu);
%     yi = (Rim(fi));
%     ci = yi - xi;
%     c = c + ci/(xr2-xr1);
% end
% fprintf ( "intercept: %d \n",c);
% 
% xr1 = 117; xr2 = 120; 
% c = 0; mi = 0; xold = 0; yold = 0;
% for x= xr1:xr2
%     xi = x;
%     fi = find (xi == Riu);
%     yi = (Rim(fi));
%     mt = 0;
%     if ( x > xr1 )
%         mt = (yold - yi)/(xold - xi); 
%     end
%     xold = xi; yold = yi;
%     mi = mi + mt/(xr2 - xr1);
% end
%     c = yold - (mi * xold);
% fprintf ( "slope:%d, intercept: %d \n",mi,c);

Ymat = Gmean_of_stds;
Xmat = hot_temp_arr;
cal_mat = []; k2 = []; k1 = [];

for i = 1:size(Rmean_of_stds,2)-2
    
    Inter_top = (Ymat(1,i+1)*Ymat(1,i+1)) - ( Ymat(1,i+2)*Ymat(1,i));
    Inter_bot = (2*Ymat(1,i+1)) - ( Ymat(1,i) + Ymat(1,i+2) );
    k1(1,i) = Inter_top/Inter_bot;
    Inter2_log = ( (Ymat(1,i+1) - k1(1,i))/(Ymat(1,i) - k1(1,i)) );
    k3(1,i) = log(Inter2_log)/(12*log(4));
    k2(1,i) = ( Ymat(1,i+1) - k1(1,i) )/( power( 3,(k3(1,i)* Xmat(1,i+1)) ) );
end







