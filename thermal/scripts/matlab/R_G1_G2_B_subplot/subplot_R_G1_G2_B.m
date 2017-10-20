function display_RG1G2B = subplot_R_G1_G2_B ( img, title_name, file_name, hor_res, ver_res )

        % Capture the image in a matrix
        fid = fopen(img, 'r');
        im = fread(fid, hor_res*ver_res, 'uint8');
        im = reshape(im, hor_res, [])';

        % Split the bayer's image into R,G and B bands and store them
        % in R,G1,G2 and B matrices
        M = size(im, 1);
        N = size(im, 2);
        red_mask = repmat([1 0; 0 0], M/2, N/2);
        green_mask = repmat([0 1; 1 0], M/2, N/2);
        blue_mask = repmat([0 0; 0 1], M/2, N/2);

        Rmask = uint8(im.*red_mask);
        Gmask = uint8(im.*green_mask);
        Bmask = uint8(im.*blue_mask);

        R = Rmask(1:2:ver_res,1:2:hor_res);
        
        G1 = Gmask(1:2:ver_res,2:2:hor_res);
        G2 = Gmask(2:2:ver_res,1:2:hor_res);
        
        B = Bmask(2:2:ver_res,2:2:hor_res);
      
        % Plot R,G1,G2 and B in a single plot 
        figure('visible','off'); hold on; axis square;
        subplot(2,2,1); imshow(R);  title('Red');
        subplot(2,2,2); imshow(G1); title('Green1');
        subplot(2,2,3); imshow(G2); title('Green2');
        subplot(2,2,4); imshow(B);  title('Blue');
        title_name = strrep(title_name,'_','\_');
        suptitle(title_name); hold off;
        saveas(gcf,file_name);
        display_RG1G2B = 1;
        
end
