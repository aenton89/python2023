def flatten(sequence):
    flattened = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flattened.extend(flatten(item)) 
        else:
            flattened.append(item) 
    return flattened