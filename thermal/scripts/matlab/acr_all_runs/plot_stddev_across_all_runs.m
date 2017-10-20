function makeplot = plot_stddev_across_all_runs( RGB, std, temp, save_file  )
    
    figure('visible', 'off'); hold on;axis square;
    
    title( strcat(RGB,' Channel Plot of stddev across 56C,68C,80C,92C' ) );
    xlabel('Temperature');
    ylabel('Mean of the stddev of all pixels');
    markerStr = strcat(lower(RGB),'*-');
    
    plot(std, markerStr);
    set(gca,'xticklabel',temp.');
    saveas(gcf,save_file); hold off; makeplot = 1;
end
  