from email.policy import strict

import pytest

@pytest.mark.xfail(strict=True, reason='Тест должен упасть')
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False