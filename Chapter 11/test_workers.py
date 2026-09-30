import pytest
from workers import Employee

@pytest.fixture
def common_worker():
    """A worker that can be used for all test cases."""
    worker = Employee('Paul', 'Keiser', 60000)
    return worker

def test_give_default_raise(common_worker):
    """Test that the default raise works."""
    common_worker.give_raise()
    assert common_worker.salary == 65000

def test_give_custom_raise(common_worker):
    """Test that the custom raise works."""
    common_worker.give_raise(9000)
    assert common_worker.salary == 69000