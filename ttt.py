import os

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)
target_path_1 = os.path.join(os.path.dirname(__file__), 'images', 'map.png')

print('target_path_1: ', target_path_1)
images\map.png