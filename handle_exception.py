import requests
from tb_rest_client.rest import ApiException

class GenericException(Exception):
    pass

def handle_custom_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.ConnectionError as conn_error:
            raise GenericException(f"Error connecting to ThingsBoard: {conn_error}")
        except ApiException as api_error:
            raise GenericException(f"ThingsBoard API exception: {api_error}")
        except FileNotFoundError as file_error:
            raise GenericException(f"Error reading environment variable file: {file_error}")
        except PermissionError as perm_error:
            raise GenericException(f"Permission error while reading file: {perm_error}")
        except OSError as os_error:
            raise GenericException(f"OS error while reading file: {os_error}")
        except KeyError as key_error:
            raise GenericException(f"Key error while reading environment variable, missing values: {key_error}")
        except ValueError as value_error:
            raise GenericException(f"Invalid value founded: {value_error}")
        except TypeError as type_error:
            raise GenericException(f"Invalid type founded: {type_error}")
        except Exception as e:
            raise GenericException(f"Unknown error while executing the function: {e}")
    return wrapper
