from typing import Any

def remove_empty_keys(data: dict[str, Any] | list[Any] | Any) -> Any:
    """
    Remove any None, empty dict, or empty list from the data
    :param data: Data to format
    :type data:dict[str, Any] | list[Any] | Any
    :return: Formatted data
    :rtype: Any
    """
    if isinstance(data, dict):
        return {k: remove_empty_keys(v) for k, v in data.items() if v not in (None, [], {})}
    elif isinstance(data, list):
        return [remove_empty_keys(v) for v in data if v not in (None, [], {})]
    return data
