LED_setting = '';

for t = 1:size(led_array,2)
    
    % Set the led setting values matching a string
    if ( led_array(1,t) == 1 ) 
        LED_setting = strcat( LED_setting,'0' );
    
    elseif( led_array(1,t) == 2 ) 
        LED_setting = strcat( LED_setting,'3' );
    
    elseif ( led_array(1,t) == 3 ) 
        LED_setting = strcat( LED_setting,'5' );
    
    elseif ( led_array(1,t) == 4 ) 
        LED_setting = strcat( LED_setting,'6' );
    end
    
    % Conditions to add , to the LED_setting string
    if ( t~= size(led_array,2) && size(led_array,2) >= 2 )
        LED_setting = strcat( LED_setting,',' );
    end
    
end