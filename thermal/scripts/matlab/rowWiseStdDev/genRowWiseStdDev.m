clear;
clc;

hor_res = 1280;
ver_res = 720;
fileName = 'C:\Users\Sai\Desktop\thermal\exp_data\32ms_4x_0_r3_20170919_1026\70';
fid = fopen(fileName, 'r');
im = fread(fid, hor_res*ver_res, 'uint8');
im = reshape(im, hor_res, [])';
R_rowNum = [];
R_stdDev = [];

G_rowNum = [];
G_stdDev = [];

B_rowNum = [];
B_stdDev = [];

M = size(im, 1);
N = size(im, 2);
red_mask = repmat([1 0; 0 0], M/2, N/2);
green_mask = repmat([0 1; 1 0], M/2, N/2);
blue_mask = repmat([0 0; 0 1], M/2, N/2);

R = im.*red_mask;
G = im.*green_mask;
B = im.*blue_mask;

Rout=R(1:2:720,1:2:1280);

G1=G(1:2:720,:);
G2=G(2:2:720,:);
Gout=G1+G2;

Bout=B(2:2:720,2:2:1280);

%Red channel

for i = 1:size(Rout, 1)
    R_rowNum = [R_rowNum i];
    R_stdDev = [R_stdDev std(Rout(i:i,:))];
end

% Green channel

for i = 1:size(Gout, 1)
    G_rowNum = [G_rowNum i];
    G_stdDev = [G_stdDev std(Rout(i:i,:))];
end

% Blue channel

for i = 1:size(Bout, 1)
    B_rowNum = [B_rowNum i];
    B_stdDev = [B_stdDev std(Rout(i:i,:))];
end

figure();
plot(R_rowNum, R_stdDev, 'r*');


figure();
plot(G_rowNum, G_stdDev, 'g*');

figure();
plot(B_rowNum, B_stdDev, 'b*');
        