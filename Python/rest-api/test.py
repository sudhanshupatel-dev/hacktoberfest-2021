def validCoffee(coffee_object):
    if('name' in coffee_object and 'origin' in coffee_object and 'usage' in coffee_object and 'side' in coffee_object):
        return True
    else:
        return False

valid_object = {
    "name": "valid_name",
    "origin": "valid_origin",
    "usage": "valid_usage",
    "side": "valid_side"
}
name_object = {
    "origin": "valid_origin",
    "usage": "valid_usage",
    "side": "valid_side"
}
origin_object = {
    "name": "valid_name",
    "usage": "valid_usage",
    "side": "valid_side"
}
usage_object = {
    "name": "valid_name",
    "origin": "valid_origin",
    "side": "valid_side"
}
side_object = {
    "name": "valid_name",
    "origin": "valid_origin",
    "usage": "valid_usage",
}
empty_object = {}

