
class VALIDATOR(object):
    def __init__(self, error_message="error", *args, **kwargs):
        self.error_message = error_message

    def __call__(self, value):
        # (value, None) - valid
        # (value, error_message) - invalid
        return (value, None)
