import pytest


@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True
