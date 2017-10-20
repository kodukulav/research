

class RGB_stddev_sensor_config_LED_Setting_temp:

    # All the stddev are stored in dictionaries
    # A string combining configuration, LED Setting and temperature is generated
    # The string is used as a key to store the values in the dictionary
    red_stddev   = {}
    blue_stddev  = {}
    green_stddev = {}

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 44C
    red_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_44C']   = 11.66818762
    green_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_44C'] = 9.792110408
    blue_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_44C']  = 8.664170536

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 48C
    red_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_48C']   = 11.6456
    green_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_48C'] = 9.339
    blue_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_48C']  = 8.0973

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 56C
    red_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_56C']   = 12.0608
    green_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_56C'] = 9.6157
    blue_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_56C']  = 8.3122

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 62C
    red_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_62C']   = 12.33661304
    green_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_62C'] = 9.370513026
    blue_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_62C']  = 7.996343866

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 68C
    red_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_68C']   = 13.5667
    green_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_68C'] = 10.3505
    blue_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_68C']  = 9.3642

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 74C
    red_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_74C']   = 14.42481112
    green_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_74C'] = 10.77623618
    blue_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_74C']  = 10.06847349

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 80C
    red_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_80C']   = 15.647
    green_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_80C'] = 11.401
    blue_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_80C']  = 11.1489

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 86C
    red_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_86C']   = 17.92993432
    green_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_86C'] = 13.68788725
    blue_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_86C']  = 13.99654461

    # Sensor_Config = 32ms_4X, LED_Setting = 0,3,5,6 Temperature = 92C
    red_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_92C']   = 20.1393
    green_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_92C'] = 15.641
    blue_stddev['32ms_4X_LED_Setting_0,3,5,6_temp_92C']  = 16.472


    # The unique string is generated by combining the following in order
    # 1. Image sensor configuration : 32ms_4X
    # 2. LED Setting used to compute stddev : 0,3,5,6
    # 3. Temperature at which the stddev is needed: 48C, 56C, 68C, 80C, 92C
    # Then the string is formed combining the above three as follows
    # Generic: <1>_LED_Setting_<2>_temp_<3>
    # Example: 32ms_4X_LED_Setting_0,3,5,6_temp_48
    def ret_RGB_stddev_at_config_LED_Setting_temp(self, unique_string ):
        return self.red_stddev[unique_string], self.green_stddev[unique_string], self.blue_stddev[unique_string]