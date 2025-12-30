import pytest
import NewCombatLogic
from Combatant import Combatant


class Tests:
    def setup_teardown_tkinter(self):
        class MockStringVar:
            def __init__(self, name, value):
                self._name = name
                self._value = value
            def winfo_name(self):
                return self._name
            def get(self):
                return self._value

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

    def test_update_health_label(self, setup_teardown_tkinter):
        pass