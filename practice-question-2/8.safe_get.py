def safe_get(d, path):
    path_list = path.split(".")
    current_dict = d
    for key in path_list:
        current_dict = current_dict.get(key)
        if current_dict is None:
            return None
    return current_dict


d = {"user": {"profile": {"name": "Alice"}}}
print(safe_get(d, "user.profile.name"))
print(safe_get(d, "user.address.city"))
