%%%%%%%%%%%%%%%% GLOBAL %%%%%%%%%%%%%%%%%%%%%
% Add paths to pick up scripts from other area
addpath('./fig/');
addpath('./paths/');
addpath('./cmn_scripts/');

% Global Variables for special run 
git_proc_data_path = 'C:\Users\Sai\Desktop\thermal\proc_data\';
git_exp_data_path  = 'C:\Users\Sai\Desktop\thermal\exp_data\';

reference_temp = 44; cold_temp = int2str(reference_temp);
max_pixel_val = 256; hor_res = 1280; ver_res = 720;
% % % % 
% 1 --> LED setting = 0  ||||  2 --> LED setting = 3
% 3 --> LED setting = 5  ||||  4 --> LED setting = 6
hot_temp_arr = [ 48,56,68,80,92 ];
run_config = '32ms_4X_';
hot_temp = int2str(hot_temp_arr(5));
led_array = [1,2,3,4];
with_hot_pixel = 1;
led_array_LED_setting_str;
% set it to 1 to generate data with all the pixels                    
% set it to 0 to generate data by removing hot pixels
%%%%%%%%%%%%%%%% GLOBAL %%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%% Create file store directory%%%%%%%%%%%
dir_name = strcat(run_config,'LED_',LED_setting,'_cold_',cold_temp,'C_hot_',hot_temp,'C');

if ( with_hot_pixel == 0 ) 
    dir_name = strcat( dir_name,'_wout_hotpix' );
end

save_dir = strcat( git_proc_data_path, dir_name);

if ( exist( save_dir, 'dir' ) )
    cmd_rmdir(save_dir);
end

mkdir (save_dir);
%%%%%%%%%%%%%%%%%%%%%%% Create file store directory%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%% File Names concatenated with paths %%%%%%%%%%%
red_figPath   = { strcat(save_dir,'\R_mean.jpg'), strcat(save_dir,'\R_std.jpg') };
green_figPath = { strcat(save_dir,'\G_mean.jpg'), strcat(save_dir,'\G_std.jpg') };
blue_figPath  = { strcat(save_dir,'\B_mean.jpg'), strcat(save_dir,'\B_std.jpg') };
%%%%%%%%%%%%%%%%%%%%%%% File Names concatenated with paths %%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%% Initialise all the globally used internal variables %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Rin_unique = []; Gin_unique = []; Bin_unique = [];
Rin = cell(4,1); Bin = cell(4,1); Gin = cell(4,1);

Rmean = []; Rstd = []; Gmean = []; Gstd = [];
Bmean = []; Bstd = [];

Racc  = cell(max_pixel_val(1,1),1); 
Gacc  = cell(max_pixel_val(1,1),1);
Bacc  = cell(max_pixel_val(1,1),1);
%%%%%%%%%%%%%%%%%%%%%%% Initialise all the globally used internal variables %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%% Take the average of the input images %%%%%%%%%%%%%%%%%%%%%%%%%%%%     
%%%%%%%%%%%%%%%%%%%%%%%% Generate Rin_unique,Bin_unique and Gin_unique %%%%%%%%%%%%%%%%%%%
tic 
for led = led_array
    im_denoised = zeros(hor_res*ver_res, 1);
    im = zeros(hor_res*ver_res, 1);
 
    led_array_path_map;    
    
    for i=1:size(input_img, 1)
        disp(input_img{i});
        fid = fopen(input_img{i}, 'r');
        im = fread(fid, hor_res*ver_res, 'uint8');
        im_denoised = im_denoised + im/size(input_img, 1);
        fclose(fid);
    end    
    
    im_denoised = reshape(im_denoised, hor_res, [])';  %Converting from row vector to a matrix with dimensions equal to image resolution
    M = size(im_denoised, 1);
    N = size(im_denoised, 2);
    red_mask   = repmat([1 0; 0 0], M/2, N/2);
    green_mask = repmat([0 1; 1 0], M/2, N/2);
    blue_mask  = repmat([0 0; 0 1], M/2, N/2);
    
    % Masks to extract R,G1,G2 and B from bayer's image
    R = uint8(im_denoised.*red_mask);
    G = uint8(im_denoised.*green_mask);
    B = uint8(im_denoised.*blue_mask);
    
    %% Extract R,G1,G2 and B pixels from bayer's image
    Rin{led} =R(1:2:720,1:2:1280);
    Rin{led} = reshape(Rin{led}, [], 1);
    
    G1=G(1:2:720,:);
    G2=G(2:2:720,:);
    Gin{led}=G1+G2;
    Gin{led} = reshape(Gin{led}, [], 1);
    
    Bin{led}=B(2:2:720,2:2:1280); 
    Bin{led}= reshape(Bin{led}, [], 1);
         
    Rin_unique = [ Rin_unique unique(Rin{led})'];
    Rin_unique = unique(Rin_unique);
    Gin_unique = [ Gin_unique unique(Gin{led})'];
    Gin_unique = unique(Gin_unique); 
    Bin_unique = [ Bin_unique unique(Bin{led})'];
    Bin_unique = unique(Bin_unique);  
end

%%%%%%%%%%%%%%%%%%%%%%%% Take the average of the input images %%%%%%%%%%%%%%%%%%%%%%%%%%%%     
%%%%%%%%%%%%%%%%%%%%%%%% Generate Rin_unique,Bin_unique and Gin_unique %%%%%%%%%%%%%%%%%%%     


%%%%%%%%%%%%%%%%%%%%%%%% Capture the pixel values related to unique values of Rin/Gin/Bin_unique arrays %%%%%%%%%%%%%%%%%%%%%%%%%%%%     
%%%%%%%%%%%%%%%%%%%%%%%% Have a storage box called R/G/Bacc for each value of Rin/Gin/Bin_unique %%%%%%%%%%%%%%%%%%%     
    
for led = led_array
    
    % Set output_img cell array depending on
    % LED setting and temperature set by the user of this program
    % Please look at led_array, LED_setting and hot_temp variables
    % to get an understanding on what this is doing
    led_array_path_map; 
     
    % Process the output image array element by element
    for i =1:size(output_img,1)
        disp(output_img{i});
        
        % Open the file and store the bayers image
        fid = fopen(output_img{i}, 'r');
        im = fread(fid, hor_res*ver_res, 'uint8');
        im = reshape(im, hor_res, [])';
        
        % Extract the R/G1/G2/B pixels from the bayers image
        % Also calculate the mean of these pixels to 
        % identify and isolate the hot pixels
        M = size(im, 1);
        N = size(im, 2);
        red_mask = repmat([1 0; 0 0], M/2, N/2);
        green_mask = repmat([0 1; 1 0], M/2, N/2);
        blue_mask = repmat([0 0; 0 1], M/2, N/2);

        R = uint8(im.*red_mask);
        G = uint8(im.*green_mask);
        B = uint8(im.*blue_mask);

        Rout=R(1:2:720,1:2:1280);
        Rout = reshape(Rout,[] ,1);
        mean_R = mean(Rout);
        
        G1=G(1:2:720,:);
        G2=G(2:2:720,:);
        Gout=G1+G2;
        Gout = reshape(Gout,[] ,1);
        mean_G = mean(Gout);
        
        Bout=B(2:2:720,2:2:1280);
        Bout = reshape(Bout,[] ,1);
        mean_B = mean(Bout);
          
        % storage collector for each unique input pixel brightness
        % input pixel means pixel observed at cold temperature 
        % In this case it is 44C
        %Red pixels 
        for r = Rin_unique
            %%disp(r);
            indices = find(Rin{led} == r);
            temper = [];
            for ind = indices'
                if (Rout(ind) < mean_R + 30) && (with_hot_pixel == 0)
                    temper = [temper Rout(ind)];
                elseif with_hot_pixel == 1
                    temper = [temper Rout(ind)];    
                end
            end
            Racc{r+1} = [ Racc{r+1} temper ];
        end
        
        %Green pixels
        for g = Gin_unique
            indices = find(Gin{led} == g);
            temper = [];
            for ind = indices'
                if (Gout(ind) < mean_G + 30) && (with_hot_pixel == 0)
                    temper = [temper Gout(ind)]; 
                elseif ( with_hot_pixel == 1 )
                    temper = [temper Gout(ind)];
                end
            end
            Gacc{g+1} = [ Gacc{g+1} temper ];
        end
        
        %Blue pixels
        for b = Bin_unique
            indices = find(Bin{led} == b);
            temper = [];
            for ind = indices'
                if (Bout(ind) < mean_B + 30) && ( with_hot_pixel == 0 )
                    temper = [temper Bout(ind)];
                elseif with_hot_pixel == 1
                    temper = [temper Bout(ind)];
                end
            end    
            Bacc{b+1} = [ Bacc{b+1} temper ];
        end  
        fclose(fid);
    end % output file loop
    
end %led loop
%%%%%%%%%%%%%%%%%%%%%%%% Capture the pixel values related to unique values of Rin/Gin/Bin_unique arrays %%%%%%%%%%%%%%%%%%%%%%%%%%%%     
%%%%%%%%%%%%%%%%%%%%%%%% Have a storage box called R/G/Bacc for each value of Rin/Gin/Bin_unique %%%%%%%%%%%%%%%%%%%     


%%%%%%%%%%%%%%%%%%%%%%%% Calculate the mean and std of output pixel values %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%% for each value of Rin/Gin/Bin_unique gathered in the storage box called R/G/Bacc  %%%%%%%%%%%%%%%%%%%     

for r = Rin_unique
%     Rmean = [ Rmean mean(Racc{r+1}) ];
    Rstd  = [ Rstd  std(double(Racc{r+1})) ];
end

for g = Gin_unique
%     Gmean = [ Gmean mean(Gacc{g+1}) ];
    Gstd  = [ Gstd  std(double(Gacc{g+1})) ];
end

for b = Bin_unique
%     Bmean = [ Bmean mean(Bacc{b+1}) ];
    Bstd  = [ Bstd  std(double(Bacc{b+1})) ];
end

%%%%%%%%%%%%% Calculate the mean and std of output pixel values %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%% for each value of Rin/Gin/Bin_unique gathered in the storage box called R/G/Bacc  %%%%%%%%%%%%%%%%%%%  



%%%%%%% Plot the mean and stddev of output pixels calculated  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%% for each input pixel value and store them in a directory as jpg image %%%%%%%%%%%%%%%%%%%%%%% 

% result = mean_fig   ( 'R', Rin_unique, Rmean, red_figPath{1}, hot_temp, cold_temp, run_config, LED_setting );
% result = stddev_fig ( 'R', Rin_unique, Rstd, red_figPath{2}, hot_temp, cold_temp,  run_config, LED_setting );
% result = mean_fig   ( 'G', Gin_unique, Gmean, green_figPath{1}, hot_temp, cold_temp, run_config, LED_setting );
% result = stddev_fig ( 'G', Gin_unique, Gstd, green_figPath{2}, hot_temp, cold_temp,  run_config, LED_setting );
% result = mean_fig   ( 'B', Bin_unique, Bmean, blue_figPath{1}, hot_temp, cold_temp,  run_config, LED_setting );
% result = stddev_fig ( 'B', Bin_unique, Bstd, blue_figPath{2}, hot_temp, cold_temp,  run_config, LED_setting );

%%%%%%% Plot the mean and stddev of output pixels calculated  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%% for each input pixel value and store them in a directory as jpg image %%%%%%%%%%%%%%%%%%%%%%% 

     
toc