#! /usr/bin/env python
# -*- coding: utf-8 -*-
# S.D.G

"""MUCT AAM Holistic



:author: Ben Johnston
:license: 3-Clause BSD

"""

# Imports
from muctAAM import MuctAAM

model = MuctAAM('/home/bjoh3944/predPap-ben/datasets/muct/muct-images',
    basename='muct_aam_hol')
model.load_data()
model.train_model(diagonal=None,max_shape_components=None, max_appearance_components=None)
model.fit_model()
model.predict_test_set()
model.generate_cdf()
