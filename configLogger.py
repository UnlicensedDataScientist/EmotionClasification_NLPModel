#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 11:50:55 2023

@author: Unlicensed Data Cientist
"""

import logging
import psutil
import colorlog

logging.basicConfig(filename='info.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Logger configuration
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter('%(log_color)s%(levelname)s:%(message)s'))
logger = colorlog.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

