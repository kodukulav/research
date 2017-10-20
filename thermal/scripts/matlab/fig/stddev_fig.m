        
function result = stddev_fig ( RGB, RGBin_unique, RGB_std, RGB_figPath, hot_temp, cold_temp, run_config, LED_setting )
    
    figure('visible', 'off');hold on;
    
    part1 = strcat("Standard Deviation of ",RGB," channel image pixels at ",hot_temp,"C vs image pixels at ",cold_temp,'C');
    part2 = strcat( "Configuration: ", strrep(run_config,'_',' ')," and LED setting = ", LED_setting);
    title( {part1,part2} );
    xlabel(strcat("Brightness values of image pixels at ",cold_temp,'C') );
    ylabel(strcat("Std Dev of brightness values of image pixels at ",hot_temp,'C') );    
    markerStr = strcat(lower(RGB),'*');
       
    axis([0 255 0 100]); axis square;
    
%     RGBin_unique_col   = double(RGBin_unique'); %x
%     RGB_std_col        = double(RGB_std');     %y
%     RGB_std_fit        = fit ( RGBin_unique_col, RGB_std_col, 'linearinterp' );
%     plot ( RGB_std_fit, RGBin_unique_col, RGB_std_col, markerStr ); 

    plot(RGBin_unique,RGB_std, markerStr);
    saveas(gcf,RGB_figPath); hold off; result = 1;
end
    