#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-07-27
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [ocp5](https://github.com/freezed/ocp5) project
"""

# DATABASE
DB_CONFIG = {
    'host': 'localhost',
    'user': 'loff',
    'pass': 'loff',
    'db': 'loff',
    'char': 'utf8',
    'file': 'create-db-loff.sql'
}

# API
FIELD_KEPT = [
    'product_name',
    'stores',
    'nutrition_grades',
    'categories_tags'
]