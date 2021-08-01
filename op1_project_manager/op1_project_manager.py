import shutil
import os

class Op1ProjectManager:
    _current_slot = 0

    def __init__(self, max_slot=2):
        self._max_slot = max_slot

    def inrcrement_slot(self):
        if self._current_slot == self._max_slot:
            self._current_slot = 0
        else:
            self._current_slot += 1
    
    def decriment_slot(self):
        if self._current_slot == 0:
            self._current_slot = self._max_slot
        else:
            self._current_slot -= 1
    
    def backup(self):
        # Copy files from op1 to current slot folder on SD card
        print(self._current_slot)
    
    def restore(self):
        # Copy files from current slot folder on SD card to op1
        return