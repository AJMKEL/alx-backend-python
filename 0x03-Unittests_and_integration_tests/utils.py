#!/usr/bin/env python3
"""Utility functions"""

def access_nested_map(nested_map, path):
    """Access nested map value"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map

def get_json(url):
    """Dummy function to simulate API call"""
    import requests
    response = requests.get(url)
    return response.json()

def memoize(func):
    """Memoization decorator"""
    cache = {}
    def wrapper(*args, **kwargs):
        if func not in cache:
            cache[func] = func(*args, **kwargs)
        return cache[func]
    return wrapper
