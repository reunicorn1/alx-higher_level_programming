#!/usr/bin/python3
"""
This is module '7-add_item' supplying the function ''add_item''
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(string):
    """This function takes a list of strings and append them to an existing
    list or creates a new list if not found

    Args:
       string (list): list of strings
    """
    try:
        with open("add_item.json", "r+", encoding="utf-8") as f:
            pass
    except FileNotFoundError:
        with open("add_item.json", "w", encoding="utf-8") as f:
            json.dump([], f)
    if not string:
        return
    my_list = load_from_json_file("add_item.json")
    my_list += string
    save_to_json_file(my_list, "add_item.json")


string = sys.argv[1:]
add_item(string)
