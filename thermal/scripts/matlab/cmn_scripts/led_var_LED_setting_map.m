% This is a one-one map between led array loop variable and 
% LED_setting string 
if ( led == 1 ) 
    LED_setting = '0';
elseif (led == 2 )
    LED_setting = '3';
elseif (led == 3 )
    LED_setting = '5';
elseif (led == 4 )
    LED_setting = '6';
end
