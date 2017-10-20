%%%%%%%%%%%%%%%% GLOBAL %%%%%%%%%%%%%%%%%%%%%
% Add paths to pick up scripts from other area
addpath('./fig/');
addpath('./paths/');
addpath('./cmn_scripts/');
addpath('./hot_pixels/');

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
led_array = [1,2,3,4];
with_hot_pixel = 1;
led_array_LED_setting_str;
add_on_mean = 30;
% set it to 1 to generate data with all the pixels                    
% set it to 0 to generate data by removing hot pixels
%%%%%%%%%%%%%%%% GLOBAL %%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%% Create Directory %%%%%%%%%%%%%%%%%%%
dir_name = strcat('hot_pixels_',run_config,'LED_setting_0,3,5,6');
save_dir = strcat( git_proc_data_path, dir_name);

if ( exist( save_dir, 'dir' ) )
    cmd_rmdir(save_dir);
end

mkdir (save_dir);
%%%%%%%%%%%%%%%%%%%%%%%%%%% Create Directory %%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%% Initialise all the globally used internal variables %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Rhot = [];        Bhot= [];        Ghot = []; 
%%%%%%%%%%%%%%%%%%%%%%% Initialise all the globally used internal variables %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%% Capture the pixel values related to unique values of Rin/Gin/Bin_unique arrays %%%%%%%%%%%%%%%%%%%%%%%%%%%%     
%%%%%%%%%%%%%%%%%%%%%%%% Have a storage box called R/G/Bacc for each value of Rin/Gin/Bin_unique %%%%%%%%%%%%%%%%%%%     
    
for led = led_array
    
    for temp = 1:size(hot_temp_arr,2)
        
        Rhot(led,temp) = 0; Ghot(led,temp) = 0; Bhot(led,temp) = 0;
        
        hot_temp = int2str( hot_temp_arr(1,temp) );
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
            for r = Rout'
                if (r > mean_R+add_on_mean) 
                    Rhot(led,temp) = Rhot(led,temp) + 1;  
                end 
            end

            %Green pixels
            for g = Gout'
                if (g > mean_G+add_on_mean)
                    Ghot(led,temp) = Ghot(led,temp) + 1;
                end
            end

            %Blue pixels
            for b = Bout'
                if ( b > mean_B+add_on_mean)
                    Bhot(led,temp) = Bhot(led,temp) + 1; 
                end
            end    
            fclose(fid);
        end % output file loop
        
        % R/G/B hot temperature numbers
        Rhot(led,temp) = Rhot(led,temp)/size(output_img,1);
        Ghot(led,temp) = Ghot(led,temp)/size(output_img,1);
        Bhot(led,temp) = Bhot(led,temp)/size(output_img,1);
        
    end % temperature loop
    
    % Plot the R/G/B images for one led setting across temperature
    led_var_LED_setting_map;
    RGB_title = strcat(run_config,"LED_setting_",LED_setting);
    RGB_title = strrep(RGB_title,'_','\_');
    Rpath = strcat(save_dir,'\R_LED_',LED_setting,'.bmp'); 
    Gpath = strcat(save_dir,'\G_LED_',LED_setting,'.bmp'); 
    Bpath = strcat(save_dir,'\B_LED_',LED_setting,'.bmp'); 
    
    result = plot_hot_pixel_acr_temp ( 'R', Rhot(led,:), hot_temp_arr, Rpath, RGB_title ); 
    result = plot_hot_pixel_acr_temp ( 'G', Ghot(led,:), hot_temp_arr, Gpath, RGB_title ); 
    result = plot_hot_pixel_acr_temp ( 'B', Bhot(led,:), hot_temp_arr, Bpath, RGB_title ); 
    
end %led loop

for temp = 1:size(hot_temp_arr,2)
    Rhot_led(1,temp) = mean( Rhot(:, temp) );
    Ghot_led(1,temp) = mean( Ghot(:, temp) );
    Bhot_led(1,temp) = mean( Bhot(:, temp) );
end

RGB_title = strcat(run_config,"LED_setting_0,3,5,6");
RGB_title = strrep(RGB_title,'_','\_');
Rpath = strcat(save_dir,'\R_LED_0_3_5_6.bmp'); 
Gpath = strcat(save_dir,'\G_LED_0_3_5_6.bmp'); 
Bpath = strcat(save_dir,'\B_LED_0_3_5_6.bmp'); 
    
result = plot_hot_pixel_acr_temp ( 'R', Rhot_led, hot_temp_arr, Rpath, RGB_title ); 
result = plot_hot_pixel_acr_temp ( 'G', Ghot_led, hot_temp_arr, Gpath, RGB_title ); 
result = plot_hot_pixel_acr_temp ( 'B', Bhot_led, hot_temp_arr, Bpath, RGB_title ); 

%%%%%%%%%%%%%%%%%%%%%%%% Capture the pixel values related to unique values of Rin/Gin/Bin_unique arrays %%%%%%%%%%%%%%%%%%%%%%%%%%%%     
%%%%%%%%%%%%%%%%%%%%%%%% Have a storage box called R/G/Bacc for each value of Rin/Gin/Bin_unique %%%%%%%%%%%%%%%%%%%     
