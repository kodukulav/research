
class RGB_hot_pixels_sensor_config_LED_Setting_temp:

    # All the hot_pixels are stored in dictionaries
    # A string combining configuration, LED Setting and temperature is generated
    # The string is used as a key to store the values in the dictionary
    red_hot_pixels   = {}
    green_hot_pixels = {}
    blue_hot_pixels  = {}

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 44C
    red_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_44C'] = (29)/4
    green_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_44C'] = (439)/4
    blue_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_44C'] = (97.6)/4

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 48C
    red_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_48C']   = 14.4
    green_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_48C'] = 426.1
    blue_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_48C']  = 85.3

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 56C
    red_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_56C']   = 29
    green_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_56C'] = 439
    blue_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_56C']  = 97.6

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 62C
    red_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_62C'] = (119.7)/2
    green_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_62C'] = (689)/2
    blue_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_62C'] = (185.4)/2

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 68C
    red_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_68C']   = 119.7
    green_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_68C'] = 689
    blue_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_68C']  = 185.4

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 74C
    red_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_74C'] = (587.3)/2
    green_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_74C'] = (1685.4)/2
    blue_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_74C'] = (661.2)/2

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 80C
    red_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_80C']   = 587.3
    green_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_80C'] = 1685.4
    blue_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_80C']  = 661.2

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 86C
    red_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_86C'] = (2671.9)/2
    green_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_86C'] = (6048.8)/2
    blue_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_86C'] = (2794.2)/2

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 92C
    red_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_92C']   = 2671.9
    green_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_92C'] = 6048.8
    blue_hot_pixels['32ms_4X_LED_Setting_0,3,5,6_temp_92C']  = 2794.2


    # The unique string is generated by combining the following in order
    # 1. Image sensor configuration : 32ms_4X
    # 2. LED Setting at which hot_pixels is computed  : 0,3,5,6
    # 3. Temperature at which the hot_pixels is computed: 48C, 56C, 68C, 80C, 92C
    # Then the string is formed combining the above three as follows
    # Generic: <1>_LED_Setting_<2>_temp_<3>
    # Example: 32ms_4X_LED_Setting_0,3,5,6_temp_48
    def ret_RGB_hot_pixels_at_config_LED_Setting_temp(self, unique_string ):
        return self.red_hot_pixels[unique_string], self.green_hot_pixels[unique_string], self.blue_hot_pixels[unique_string]
