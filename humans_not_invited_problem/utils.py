"""
Utils.
"""
import json


def save_json(data: dict, filename: str = "tags2images.json") -> None:
    """Save dict in json format.

    Parameters
    ----------
    data : dict
        The dict.
    filename : str, optional
        The filename to save, by default "tags2images.json"
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_json(filename: str = "tags2images.json") -> dict:
    """Load the dict form json file.

    Parameters
    ----------
    filename : str, optional
        The filename to load, by default "tags2images.json"

    Returns
    -------
    dict
        The dict.
    """
    with open(filename, "r") as file:
        return json.load(file)
