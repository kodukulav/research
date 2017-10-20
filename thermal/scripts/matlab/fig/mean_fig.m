        
function result = mean_fig ( RGB, RGBin_unique, RGB_mean, RGB_figPath, hot_temp, cold_temp, run_config, LED_setting )
    
    figure('visible', 'off'); hold on;
    
    part1 = strcat( "Mean of ",RGB," channel image pixels at ",hot_temp,"C vs image pixels at ",cold_temp,'C');
    part2 = strcat( "Configuration: ", strrep(run_config,'_',' '), " and LED setting = ", LED_setting);
    title( {part1,part2} ); markerStr = strcat(lower(RGB),'*');
    xlabel(strcat("Brightness values of image pixels at ",cold_temp,'C') );
    ylabel(strcat("Mean of brightness values of image pixels at ",hot_temp,'C') );    
       
    axis([0 255 0 255]); axis square;
    
    plot(RGBin_unique,RGB_mean, markerStr);
    grid on; grid minor;
    xbounds = xlim();
    set(gca, 'xtick', xbounds(1):15:xbounds(2));
    set(gca,'position',[0.05 0.08 0.9 0.9]);
    ybounds = ylim();
    set(gca, 'ytick', ybounds(1):15:ybounds(2));
    set(gca,'position',[0.05 0.08 0.9 0.9]);
    
    saveas(gcf,RGB_figPath); hold off; result = 1;
end
    