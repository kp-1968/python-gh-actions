def get_err_support():
    return '{0} in a {1} cannot be greater than {2}. {0} given = {3}', {
        'years': ('', 10000000000),
        'months': ('year', 12),
        'weeks': ('month', 5),
        'days': ('week', 31),
        'hours': ('day', 23),
        'minutes': ('hour', 59),
        'seconds': ('minute', 59),
    }


def validate_iso_8601_duration_dict(duration: dict) -> None:
    if type(duration) is not dict:
        raise TypeError("Expected duration to be of type<'dict'>")
    err_msg, validation_vals = get_err_support()
    for k, v in duration.items():
        if v is not None and v > validation_vals[k][1]:
            raise ValueError(err_msg.format(k.capitalize(), validation_vals[k][0], validation_vals[k][1], v))
