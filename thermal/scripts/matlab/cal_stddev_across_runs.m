% ARGUMENTS 1 and 2 are dependant and should reflect the same
% Since both of them are concerned with LED setting
%ARGUMENT 1 : led_array 
% Valid values are 1,2,3,4
% 1 -> LED setting = 0, 2-> LED setting = 3
% 3 -> LED setting = 5, 4-> LED setting = 6

%ARGUMENT 2 : LED_setting 
% Valid values are 0,3,5,6

%ARGUMENT 3 : hot_temp
% Valid values are 1,2,3,4
% 1 -> 56C, 2-> 68C, 3->80C, 4->92C

%ARGUMENT 4 : with_hot_pixel = 1;
% Valid values are 0/1
% 0 - removes hot pixels 
% 1 - all pixels
tic 
addpath('./acr_all_runs/');

hp = '1';
max_pixel_val = 256; file_name = 'mean_var_changed.m';

Rm56 = []; Rm68 = []; Rm80 = []; Rm92 = [];Rm48 = [];
Gm56 = []; Gm68 = []; Gm80 = []; Gm92 = [];Gm48 = [];
Bm56 = []; Bm68 = []; Bm80 = []; Bm92 = [];Bm48 = [];

Rs56 = []; Rs68 = []; Rs80 = []; Rs92 = [];Rs48 = [];
Gs56 = []; Gs68 = []; Gs80 = []; Gs92 = [];Gs48 = [];
Bs56 = []; Bs68 = []; Bs80 = []; Bs92 = [];Bs48 = [];

Ru56 = []; Ru68 = []; Ru80 = []; Ru92 = [];Ru48 = [];
Gu56 = []; Gu68 = []; Gu80 = []; Gu92 = [];Gu48 = [];
Bu56 = []; Bu68 = []; Bu80 = []; Bu92 = [];Bu48 = [];



%LED setting = 0,3,5,6 at 56C, 68C, 80C, 92C
for iter = 1:5
    perl('update_mean_var.pl', file_name, '1,2,3,4', int2str(iter), hp);
    mean_var_changed;
    
    if ( iter == 1 )
        Rm48 = Rmean; Gm48 = Gmean; Bm48 = Bmean;
        Rs48 = Rstd;  Gs48 = Gstd;  Bs48 = Bstd;
        Ru48 = Rin_unique;  Gu48 = Gin_unique;  Bu48 = Bin_unique;
    end
    
    if ( iter == 2 )
        Rm56 = Rmean; Gm56 = Gmean; Bm56 = Bmean;
        Rs56 = Rstd;  Gs56 = Gstd;  Bs56 = Bstd;
        Ru56 = Rin_unique;  Gu56 = Gin_unique;  Bu56 = Bin_unique;
    end
    
    if ( iter == 3 )
        Rm68 = Rmean; Gm68 = Gmean; Bm68 = Bmean;
        Rs68 = Rstd;  Gs68 = Gstd;  Bs68 = Bstd;
        Ru68 = Rin_unique;  Gu68 = Gin_unique;  Bu68 = Bin_unique;
    end
    
    if ( iter == 4 )
        Rm80 = Rmean; Gm80 = Gmean; Bm80 = Bmean;
        Rs80 = Rstd;  Gs80 = Gstd;  Bs80 = Bstd;
        Ru80 = Rin_unique;  Gu80 = Gin_unique;  Bu80 = Bin_unique;
    end
    
    if ( iter == 5 )
        Rm92 = Rmean; Gm92 = Gmean; Bm92 = Bmean;
        Rs92 = Rstd;  Gs92 = Gstd;  Bs92 = Bstd;
        Ru92 = Rin_unique;  Gu92 = Gin_unique;  Bu92 = Bin_unique;
    end
        
end

% Rmean_of_means(1,5) = nanmean(Rm48);Gmean_of_means(1,5) = nanmean(Gm48);Bmean_of_means(1,5) = nanmean(Bm48);
% Rmean_of_means(1,1) = nanmean(Rm56);Gmean_of_means(1,1) = nanmean(Gm56);Bmean_of_means(1,1) = nanmean(Bm56);
% Rmean_of_means(1,2) = nanmean(Rm68);Gmean_of_means(1,2) = nanmean(Gm68);Bmean_of_means(1,2) = nanmean(Bm68);
% Rmean_of_means(1,3) = nanmean(Rm80);Gmean_of_means(1,3) = nanmean(Gm80);Bmean_of_means(1,3) = nanmean(Bm80);
% Rmean_of_means(1,4) = nanmean(Rm92);Gmean_of_means(1,4) = nanmean(Gm92);Bmean_of_means(1,4) = nanmean(Bm92);

Rmean_of_stds(1,1) = nanmean(Rs48);Gmean_of_stds(1,1) = nanmean(Gs48);Bmean_of_stds(1,1) = nanmean(Bs48);  
Rmean_of_stds(1,2) = nanmean(Rs56);Gmean_of_stds(1,2) = nanmean(Gs56);Bmean_of_stds(1,2) = nanmean(Bs56);  
Rmean_of_stds(1,3) = nanmean(Rs68);Gmean_of_stds(1,3) = nanmean(Gs68);Bmean_of_stds(1,3) = nanmean(Bs68);  
Rmean_of_stds(1,4) = nanmean(Rs80);Gmean_of_stds(1,4) = nanmean(Gs80);Bmean_of_stds(1,4) = nanmean(Bs80);  
Rmean_of_stds(1,5) = nanmean(Rs92);Gmean_of_stds(1,5) = nanmean(Gs92);Bmean_of_stds(1,5) = nanmean(Bs92);  


temp = {'48','56','68','80','92'};

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Create directory to store the files
% Hard-coded path for saving generated images
dir_name = 'stddev_across_44C_48C_56C_68C_80C_92C';

if ( with_hot_pixel == 0 ) 
    dir_name = strcat( dir_name,'_wout_hotpix' );
end

save_dir = strcat( git_proc_data_path, dir_name);

if ( exist( save_dir, 'dir' ) )
    cmd_rmdir(save_dir);
end

mkdir (save_dir);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% plot_mean_across_all_runs('R', Rmean_of_means, temp, strcat(save_dir,'\','Rmean_all_temp.jpg')); 
% plot_mean_across_all_runs('G', Gmean_of_means, temp, strcat(save_dir,'\','Gmean_all_temp.jpg')); 
% plot_mean_across_all_runs('B', Bmean_of_means, temp, strcat(save_dir,'\','Bmean_all_temp.jpg')); 

% plot_stddev_across_all_runs('R', Rmean_of_stds, temp, strcat(save_dir,'\','Rstd_all_temp.jpg')); 
% plot_stddev_across_all_runs('G', Gmean_of_stds, temp, strcat(save_dir,'\','Gstd_all_temp.jpg')); 
% plot_stddev_across_all_runs('B', Bmean_of_stds, temp, strcat(save_dir,'\','Bstd_all_temp.jpg')); 





toc