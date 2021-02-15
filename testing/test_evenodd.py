# test_evenodd.py
#
# Source code from "Unit testing and Test Driven Development in Python"
# (https://gayatri.hashnode.dev/unit-testing-and-test-driven-development-in-python)
# written by Gayatri Kale.
#

import pytest


def evenOdd(value):

    if type(value) == int:

        if value % 2 == 0:

            return 'even'

        else:

            return 'odd'

    else:

        raise TypeError


def test_check_even():

    retval = evenOdd(2)
    assert retval == 'even'


def test_check_odd():

    retval = evenOdd(1)
    assert retval == 'odd'


def test_check_int():

    with pytest.raises(TypeError):

        evenOdd(1.5)
