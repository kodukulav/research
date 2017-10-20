tic 
addpath('./R_G1_G2_B_subplot/'); file_name = './R_G1_G2_B_subplot/gen_subplot_RG1G2B_acr_runs.m';
hp = '0';

%LED setting = 0,3,5,6 combined at 48C, 56C, 68C, 80C, 92C
for iter = 1:5
    perl('update_mean_var.pl', file_name, '1,2,3,4', int2str(iter), hp);
    gen_subplot_RG1G2B_acr_runs;
end