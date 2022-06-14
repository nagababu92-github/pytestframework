import inspect
import logging

import pytest
import logging
from tests.conftest import Basef

@pytest.mark.usefixtures("setup")
class BasicTest(Basef):
    pass
