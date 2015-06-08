# -*- coding: utf-8 -*-
"""pytest for `radtrack.srw_enums`

:copyright: Copyright (c) 2015 RadiaBeam Technologies, LLC.  All Rights Reserved.
:license: Apache, see LICENSE for more details.
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from io import open

import pytest

from radtrack import srw_enums


def test_density_method():
    """Verify a couple of values exist"""
    d = srw_enums.DensityMethod
    assert d(0) == d.NEAR_FIELD, \
        'DensityMethod.NEAR_FIELD should be 0'
    assert d(1).has_name('FAR_FIELD'), \
        'DensityMethod.FAR_FIELD has name FAR_FIELD'
    assert d.from_anything('NEAR_FIELD').value == 0, \
        'from_anything(NEAR_FIELD) should return an enum with value 0'
    assert d.from_anything(1) == d.FAR_FIELD, \
        'from_anything(1) should return FAR_FIELD'
