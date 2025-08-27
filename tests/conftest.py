from datetime import datetime

import pytest


@pytest.fixture(scope="function")
def frozen_datetime() -> datetime:
    return datetime(day=27, month=8, year=2025)
