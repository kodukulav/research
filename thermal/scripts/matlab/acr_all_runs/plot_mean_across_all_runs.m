function makeplot = plot_mean_across_all_runs( RGB, mean, temp, save_file  )
    
    figure('visible', 'off'); hold on;axis square;
    
    title( strcat(RGB,' Channel Plot of means across 56C,68C,80C,92C' ) );
    xlabel('Temperature');
    ylabel('Mean of the brightness of all pixels');
    markerStr = strcat(lower(RGB),'*-');
    
    plot(mean, markerStr);
    set(gca,'xticklabel',temp.');
    saveas(gcf,save_file); hold off; makeplot = 1;
end
  