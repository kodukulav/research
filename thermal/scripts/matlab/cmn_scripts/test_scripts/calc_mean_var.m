tic
%%
%%%%%%%%%%%%%%%% GLOBAL %%%%%%%%%%%%%%%%%%%%%
% Global Variables for special run
reference_temp = 44;
hot_temp_arr = [ 56,68,80,92 ];
git_proc_data_path = 'C:\Users\Sai\Desktop\thermal\proc_data\';
git_exp_data_path  = 'C:\Users\Sai\Desktop\thermal\exp_data\';
max_pixel_val = 256;
hor_res = 1280;
ver_res = 720;

% set it to 1 to generate data with all the pixels
addpath('./fig/');
addpath('./paths/');

% set it to 0 to generate data by removing hot pixels
with_hot_pixel = 1;
run_config = '32ms_4X_';
cold_temp = int2str(reference_temp);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
led_array=[1];
LED_setting = '0';
hot_temp = int2str(hot_temp_arr(1));
k = 6;

mean_im = [];
stddev_im = [];

for led = led_array
    led_array_path_map;
    
    for i =1:size(output_img,1)
        disp(output_img{i});
        %fprintf ( ' Value of i is %d \n', i );
        fid = fopen(output_img{i}, 'r');
        im = fread(fid, hor_res*ver_res, 'uint8');
        im = reshape(im, hor_res, [])';
        
        if ( i == k )
            for t = 1:size(im,1)
                mean_im(1,t) = mean(im(t,:));
                stddev_im(1,t)  = ( std(double(im(t,:))) );
            end
            %%
            M = size(im, 1);
            N = size(im, 2);
            red_mask = repmat([1 0; 0 0], M/2, N/2);
            green_mask = repmat([0 1; 1 0], M/2, N/2);
            blue_mask = repmat([0 0; 0 1], M/2, N/2);
            
            R = uint8(im.*red_mask);
            G = uint8(im.*green_mask);
            B = uint8(im.*blue_mask);
            
            Rout=R(1:2:720,1:2:1280);
%             Rout = reshape(Rout,[] ,1);
            mean_R = mean(Rout');
            
            G1=G(1:2:720,:);
            G2=G(2:2:720,:);
            Gout=G1+G2;
%             Gout = reshape(Gout,[] ,1);
            mean_G = mean(Gout');
            
            Bout=B(2:2:720,2:2:1280);
%             Bout = reshape(Bout,[] ,1);
            mean_B = mean(Bout');
            %%
            figure(); hold on;
            title(strcat('Output Image Number:',int2str(i),'@',strrep(run_config,'_',':'),'LED setting=',LED_setting,'@',hot_temp,'C'));
            xlabel(strcat('Row Value@',hot_temp,'C') );
            ylabel(strcat('Mean of raw data image pixels@' ,hot_temp, 'C') );
            axis([0 ver_res 0 max_pixel_val]);
            plot(mean_G); hold off;
            
%             figure(); hold on;
            title(strcat('Output Image Number:',int2str(i),'@',strrep(run_config,'_',':'),'LED setting=',LED_setting,'@',hot_temp,'C'));
            xlabel(strcat('Row Value@',hot_temp,'C') );
            ylabel(strcat('StdDev of raw data image pixels@' ,hot_temp, 'C') );
%             plot(stddev_im); hold off;
            
            figure();hold on;
            imshow(im/255.0);hold off;
        end
        
    end
end