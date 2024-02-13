#!/usr/bin/python3
import json


def from_json_string(my_str):
    """get Json string into object

        Args:
                my_str (json str): string to object

        Returns:
                object
        """
    file = json.loads(my_str)
    return file
