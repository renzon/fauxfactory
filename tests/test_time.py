# -*- coding: utf-8 -*-

"""Tests for Time generator."""

from fauxfactory import generate_time

import unittest
import datetime


class TestTime(unittest.TestCase):
    """Test Time generator."""

    def test_generate_uuid_1(self):
        """
        @Test: Create a random UUID value
        @Feature: UUID Generator
        @Assert: A random UUID value is generated
        """

        for turn in range(100):
            result = generate_time()
            self.assertIsInstance(
                result, datetime.time,
                "A valid Time value was not generated.")
