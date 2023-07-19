"""
Unit tests for the measure module
"""

import pytest
import numpy as np

import bootcamp_2023 

def test_calculate_distance():

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1.0
    calculated_distance = bootcamp_2023.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance