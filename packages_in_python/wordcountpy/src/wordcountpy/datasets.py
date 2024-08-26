from importlib import resources

def get_flatland():
    with resources.path('pycounts.data','zen.txt') as f:
        data_file_path = f
    return data_file_path