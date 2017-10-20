%%%%%%%%%%%%%%%% GLOBAL %%%%%%%%%%%%%%%%%%%%%
% Add paths to pick up scripts from other area
addpath('./../fig/');
addpath('./../paths/');
addpath('./../cmn_scripts/');

% Global Variables for special run 
git_proc_data_path = 'C:\Users\Sai\Desktop\thermal\proc_data\';
git_exp_data_path  = 'C:\Users\Sai\Desktop\thermal\exp_data\';

reference_temp = 44; cold_temp = int2str(reference_temp);
max_pixel_val = 256; hor_res = 1280; ver_res = 720;

% % % % 
% 1 --> LED setting = 0  ||||  2 --> LED setting = 3
% 3 --> LED setting = 5  ||||  4 --> LED setting = 6
run_config = '32ms_4X_';hot_temp_arr = [ 48,56,68,80,92 ];
hot_temp = int2str(hot_temp_arr(5));
led_array = [1,2,3,4];
with_hot_pixel = 0;
% set it to 1 to generate data with all the pixels                    
% set it to 0 to generate data by removing hot pixels
%%%%%%%%%%%%%%%% GLOBAL %%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%% Create file store directory%%%%%%%%%%%
save_dir = strcat(git_proc_data_path, 'subplot_R_G1_G2_B\'); 

if ( ~exist( save_dir, 'dir' ) )
    mkdir (save_dir);
end

%%%%%%%%%%%%%%%%%%%%%%% Create file store directory%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%% Process through file after file %%%%%%%%%%%%
for led = led_array
    
    % Set input and output images cell arrays right
    % Remember to use only led as the loop variable 
    % since the script below only recognises it
    led_array_path_map; led_var_LED_setting_map;
    config_LED = strcat( run_config,'LED_setting_',LED_setting );
        
    for i = 1:size(input_img,1)
        % Create filename 
        % another variable with complete path including the file name
        temp_run   = strcat( '_',cold_temp, 'C_run_', int2str(i) ); 
        title_name  = strcat(config_LED,temp_run); 
        path_file_name = strcat(save_dir, title_name, '.jpg');

        % Grab the R,G1,G2 and B subplots of an image and store it in a file
        result = subplot_R_G1_G2_B( input_img{i}, title_name, path_file_name, hor_res, ver_res );
    end
    
    for i = 1:size(output_img,1)
        % Create filename 
        % another variable with complete path including the file name
        temp_run   = strcat( '_',hot_temp, 'C_run_', int2str(i) ); 
        title_name  = strcat(config_LED,temp_run); 
        path_file_name = strcat(save_dir, title_name, '.jpg');

        % Grab the R,G1,G2 and B subplots of an image and store it in a file
        result = subplot_R_G1_G2_B( output_img{i}, title_name, path_file_name, hor_res, ver_res );
    end
    
end
%%%%%%%%%%%%%%%%%%%%%%%% Process through file after file %%%%%%%%%%%%
