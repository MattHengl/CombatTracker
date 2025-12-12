import pytest
import NewCombatLogic
from Combatant import Combatant


class Tests:
    @pytest.fixture
    def setup_teardown(self):
        # Setup code (if needed)
        self.test_combatant = Combatant("TestGoblin", 15, 30)
        self.test_combatant_list: list[Combatant] = []
        yield self
        # Teardown code (if needed)

    @pytest.fixture
    def setup_teardown_frame(self):
        class MockEntry:
            def __init__(self, name, value):
                self._name = name
                self._value = value

            def winfo_name(self):
                return self._name

            def get(self):
                return self._value

        class MockFrame:
            def __init__(self, children):
                self._children = children

            def winfo_children(self):
                return self._children

        mock_entries = [
            MockEntry("combatant_name_1", "TestGoblin"),
            MockEntry("combatant_initiative_1", "15"),
            MockEntry("combatant_health_1", "30")
        ]
        self.mock_frame = MockFrame(mock_entries)

        yield self
        self.mock_frame = None

    def test_validate_and_create_combatant(self, setup_teardown):
        assert NewCombatLogic.validate_and_create_combatant("TestGoblin", "15", "30") == self.test_combatant

    def test_validation_and_create_combatant_invalid(self, setup_teardown):
        assert NewCombatLogic.validate_and_create_combatant("TestGoblin2", "15", "30") != self.test_combatant

    def test_extract_combatant_data(self, setup_teardown_frame):
        assert NewCombatLogic.extract_combatant_data(self.mock_frame) == {'name': "TestGoblin", 'initiative': "15", 'health': "30"}

    def test_extract_combatant_data_invalid(self, setup_teardown_frame):
        assert NewCombatLogic.extract_combatant_data(self.mock_frame) != {'name': "TestGoblin2", 'initiative': "15", 'health': "30"}

    def test_save_button_logic(self, setup_teardown_frame, setup_teardown):
        NewCombatLogic.save_button_logic(self.mock_frame, self.test_combatant_list)
        assert self.test_combatant_list[0] == Combatant("TestGoblin", 15, 30)

    def test_save_button_logic_invalid(self, setup_teardown_frame, setup_teardown):
        NewCombatLogic.save_button_logic(self.mock_frame, self.test_combatant_list)
        assert self.test_combatant_list[0] != Combatant("TestGoblin2", 15, 30)

