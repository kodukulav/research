
Red(1,1) = 0.82; Red(1,2) = -35.2;  Red(1,3) = 3.73;
Red(2,1) = 2.7;  Red(2,2) = -45.1;  Red(2,3) = 9.4;
Red(3,1) = 11.2; Red(3,2) = -56;    Red(3,3) = 20.1;
Red(4,1) = 36.1; Red(4,2) = -100.7; Red(4,3) = 48.1;

Rw(1,1) = 0.414; Rw(1,2) = 0; Rw(1,3) = 0.53;
Rw(2,1) = 0.425; Rw(2,2) = 0; Rw(2,3) = 0.52;
Rw(3,1) = 0.425; Rw(3,2) = 0; Rw(3,3) = 0.52;
Rw(4,1) = 0.425; Rw(4,2) = 0; Rw(4,3) = 0.52;

Blue(1,1) = 0.37; Blue(1,2) = -171;   Blue(1,3) = 2.12;
Blue(2,1) = 2.2;  Blue(2,2) = -261.6; Blue(2,3) = 6.2;
Blue(3,1) = 8.9;  Blue(3,2) = -333.6; Blue(3,3) = 14.2;
Blue(4,1) = 33.8; Blue(4,2) = -570.6; Blue(4,3) = 43.3;

Bw(1,1) = 0.41; Bw(1,2) = 0; Bw(1,3) = 0.586;
Bw(2,1) = 0.41; Bw(2,2) = 0; Bw(2,3) = 0.586;
Bw(3,1) = 0.41; Bw(3,2) = 0; Bw(3,3) = 0.586;
Bw(4,1) = 0.41; Bw(4,2) = 0; Bw(4,3) = 0.586;

Green(1,1) = 0.74; Green(1,2) = -205.8;  Green(1,3) = 3.35;
Green(2,1) = 3.03; Green(2,2) = -325;    Green(2,3) = 8.5;
Green(3,1) = 10;   Green(3,2) = -380.7;  Green(3,3) = 17.3;
Green(4,1) = 34.9; Green(4,2) = -608;    Green(4,3) = 47.4;

Gw(1,1) = 0.465; Gw(1,2) = 0; Gw(1,3) = 0.53;
Gw(2,1) = 0.465; Gw(2,2) = 0; Gw(2,3) = 0.53;
Gw(3,1) = 0.465; Gw(3,2) = 0; Gw(3,3) = 0.53;
Gw(4,1) = 0.465; Gw(4,2) = 0; Gw(4,3) = 0.53;



R_cal   = []; G_cal   = []; B_cal   = [];
R_dy_rn = []; G_dy_rn = []; B_dy_rn = [];

for i = 1:4
   R_cal(i,1) = ( Red(i,1) * Rw(i,1) )   + ( Red(i,3) * Rw(i,3) );    		
   G_cal(i,1) = ( Green(i,1) * Gw(i,1) ) + ( Green(i,3) * Gw(i,3) );    		
   B_cal(i,1) = ( Blue(i,1) * Bw(i,1) )  + ( Blue(i,3) * Bw(i,3) );    		
   R_dy_rn(1,i) = 10*log10(255/R_cal(i,1));
   G_dy_rn(1,i) = 10*log10(255/G_cal(i,1));
   B_dy_rn(1,i) = 10*log10(255/B_cal(i,1));
end

temp = [56,68,80,92];

Rpath = 'R_dyn_rng.jpg';
Gpath = 'G_dyn_rng.jpg';
Bpath = 'B_dyn_rng.jpg';

% addpath(".\");
result = dyn_rng_fig( 'R', R_dy_rn, temp, Rpath);
result = dyn_rng_fig( 'G', G_dy_rn, temp, Gpath);
result = dyn_rng_fig( 'B', B_dy_rn, temp, Bpath);




