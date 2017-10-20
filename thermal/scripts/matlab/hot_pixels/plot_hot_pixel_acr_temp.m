function result = plot_hot_pixel_acr_temp ( RGB, RGBhot, temp, RGB_figPath, RGB_title )
    
    figure('visible', 'off'); hold on;
    
    title( RGB_title ); 
    xlabel = "Temperature range for hot pixel number measurement";
    ylabel = " Average Number of hot pixels across runs";    
       
    markerStr = strcat('-.',lower(RGB),'*'); axis square;
    plot( temp, RGBhot, markerStr); 
    saveas(gcf,RGB_figPath); hold off; result = 1;
    
end