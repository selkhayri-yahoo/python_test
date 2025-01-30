#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:04:04 2025

@author: sami
"""

def in_autotests_we_trust(a, b):
    if a == b:
        print('Test passed')
    else:
        print('Test failed')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)

# This comment is my new comment
