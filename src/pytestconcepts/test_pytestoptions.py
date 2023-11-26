import os

import pytest

"""
1. In the below example, we have three tests, and we do pytest filename.py, it doesn't do anything
to run all these tests, we have to pytest -s filename.py
-s = standard output
-v = verbose, it will provide more details like what is the filename, what is methodname, test status

2. Out of these three methods, if we wanted to run only one of them, after the filename add double and mention function name
pytest filename::functionname

3. Let say there is case, where we want to run tests based on the partial text, we can do that one too
pytest filename -k "partialtestname"

4. To go even further, we can make use of pytest.mark, we can tag or group test based on our needs, and to the run the
marked test, it is similar to point 3, instead of -k we have to -m, if we run the test, it will throw some warning regarding
the marker, and asking us to register the marker, it is pretty simple, checkout the pytest.ini file

5. Now, if we want to execute both the different markers, we can club both of them with an or operator and similarly we can
use and operator too, but for that more than one marker must be present on the test and use not operator to ignore the test

6. There's a better way to do point 5, that is use the skip field which provided by pytest itself @pytest.mark.skip, 
and we can also add some reason to it why we're skipping the test 7. To add something more interesting with point 6, 
we have skipif marker, which is to add a condition and skip the test when it is satisfies condition 
@pytest.mark.skipif(condition,reason="msg")"""


@pytest.mark.functional
def test_regression():
    print("performing regression testing")


@pytest.mark.functional
def test_smoke():
    print("performing smoke testing")


@pytest.mark.functional
def test_exploratory():
    print("performing exploratory testing")


@pytest.mark.functional
@pytest.mark.non_functional
def test_api():
    print("Performing api testing")


@pytest.mark.non_functional
def test_security():
    print("performing security testing")


@pytest.mark.skipif(os.name == "nt", reason="Not a part of the test coverage, so removing it")
def test_performance():
    #The os.name finds the name of the operating system dependent module.
    print("Performing performance testing | " + os.name)
