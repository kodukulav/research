path = strcat('./paths/',run_config);

% LED setting of 0
if led == 1 
    addpath ( strcat(path,'LED_0/') );
    temp_map_in_path;
    rmpath ( strcat(path,'LED_0/') );
    
% LED setting of 3
elseif led == 2 
    addpath ( strcat(path,'LED_3/') );
    temp_map_in_path;
    rmpath ( strcat(path,'LED_3/') );
    
% LED setting of 5
elseif led == 3 
    addpath ( strcat(path,'LED_5/') );
    temp_map_in_path;
    rmpath ( strcat(path,'LED_5/') );
    
% LED Setting of 6
elseif led == 4
    addpath ( strcat(path,'LED_6/') );
    temp_map_in_path;
    rmpath ( strcat(path,'LED_6/') );
end
    
