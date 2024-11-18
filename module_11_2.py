# Интроспекция

def introspection_info(obj):
    obj_methods = []
    obj_attributes = []
    list_dir = dir(obj)
    for i in range (0, len(list_dir)):
        if '__' in list_dir[i]:
            obj_methods.append(list_dir[i])
        else:
            obj_attributes.append(list_dir[i])
    obj_info = {'type': obj.__class__.__name__, 'attributes': obj_attributes, 'methods': obj_methods,
                'module': __name__, 'callable': callable(obj)}
    return obj_info


number_info = introspection_info(42)
print(number_info)
