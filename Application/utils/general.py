import os

def verify_or_create_folder(folder):
    if not os.path.exists(f'output/{folder}'):
        os.makedirs(f'output/{folder}')