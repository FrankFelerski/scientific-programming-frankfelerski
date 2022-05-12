def conversion_rules(value, units_in, units_out):
    if units_in == 'degree'and units_out == 'radian':
        from math import pi
        converted_value = value * pi / 180
    elif units_in == "km/h" and units_out == 'm/s':
        converted_value = 3600*value
