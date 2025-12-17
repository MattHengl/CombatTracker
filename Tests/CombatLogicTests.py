import pytest
import NewCombatLogic
from Combatant import Combatant


class Tests:
    @pytest.fixture
    def setup_teardown(self):
        # Setup code (if needed)
        yield self
        # Teardown code (if needed)