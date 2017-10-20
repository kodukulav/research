        
function result = dyn_rng_fig ( RGB, RGB_dy_rn, temp, RGB_figPath )
    
    figure('visible', 'off'); hold on;
    
    title( strcat(lower(RGB), "channel dynamic range(dB) vs temperature(C)") ); 
    xlabel(" Temperature in Celsius ");
    ylabel(" Dynamic range of pixels in dB" );    
    markerStr = strcat('-.',lower(RGB),'*');   
    axis square;
    
    plot(temp, RGB_dy_rn, markerStr);
%     grid on; grid minor;
%     xbounds = xlim();
%     set(gca, 'xtick', xbounds(1):15:xbounds(2));
%     set(gca,'position',[0.05 0.08 0.9 0.9]);
%     ybounds = ylim();
%     set(gca, 'ytick', ybounds(1):15:ybounds(2));
%     set(gca,'position',[0.05 0.08 0.9 0.9]);

    saveas(gcf,RGB_figPath); hold off; result = 1;
end
    