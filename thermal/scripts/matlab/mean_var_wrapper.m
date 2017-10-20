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
hp = '0'; file_name = 'mean_var_changed.m';

% LED setting = 0,3,5,6 individually at 48C, 56C, 68C, 80C, 92C
for j = 1:4
    for i = 1:5
        perl('update_mean_var.pl', file_name, int2str(j) , int2str(i), hp);
        mean_var_changed;
    end
end 

%LED setting = 0,3,5,6 combined at 48C, 56C, 68C, 80C, 92C
for iter = 1:5
    perl('update_mean_var.pl', file_name, '1,2,3,4', int2str(iter), hp);
    mean_var_changed;
end

toc