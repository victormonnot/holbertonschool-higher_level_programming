#!/usr/bin/python3
"""file"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML file to a Python dictionary.

    Args:
        filename (str): Input XML file.

    Returns:
        dict: Deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
