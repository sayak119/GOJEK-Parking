#! /usr/bin/python3
# -*- coding:utf-8 -*-

import os

def clear_tmp_file():
    pickle_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tmp')
    if os.path.exists(os.path.join(pickle_file_path, 'parking_lot.pickle')):
        os.remove(os.path.join(pickle_file_path, 'parking_lot.pickle'))
    else:
        pass

if __name__ == "__main__":
    clear_tmp_file()
