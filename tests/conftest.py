import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as _activities


_ORIGINAL_ACTIVITIES = copy.deepcopy(_activities)


@pytest.fixture(autouse=True)
def reset_activities():
    # Restore the in-memory activities before each test
    _activities.clear()
    _activities.update(copy.deepcopy(_ORIGINAL_ACTIVITIES))
    yield


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
