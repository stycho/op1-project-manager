import shutil
import os
import time
from op1_device.op1_device import Op1Device

class ProjectManager:
    BACKUP_FOLDER_PATH = '/home/pi/op1_backup'
    _current_slot = 0

    def __init__(self, max_slot=2):
        self._max_slot = max_slot
        self._device = Op1Device()
        self._op1_path = self._device.get_op1_mount_point()
        self._mount_drive()

    def increment_slot(self):
        if self._current_slot == self._max_slot:
            self._current_slot = 0
        else:
            self._current_slot += 1
        return self._current_slot
    
    def decrement_slot(self):
        if self._current_slot == 0:
            self._current_slot = self._max_slot
        else:
            self._current_slot -= 1
        return self._current_slot
    
    def backup(self):
        # Copy files from op1 to current slot folder on SD card
        backup_folder = self._get_backup_slot_path()
        shutil.rmtree(backup_folder)
        shutil.copytree(self._op1_path, backup_folder)

        print(f'Backup complete to: Slot {self._current_slot}')
    
    def restore(self):
        # Copy files from current slot folder on SD card to op1
        backup_folder = self._get_backup_slot_path()
        # shutil.rmtree(self._op1_path)
        # shutil.copytree(backup_folder, self._op1_path)
        os.system(f'cp -R {backup_folder} {self._op1_path}')

        print(f'Restore complete from: Slot {self._current_slot}')

    def _mount_drive(self):
        self._device.mount_drive()

    def _unmount_drive(self):
        self._device.unmount_drive()

    def end(self):
        time.sleep(0.5)
        self._unmount_drive()
    
    def _get_backup_slot_path(self):
        return f'{self.BACKUP_FOLDER_PATH}/{self._current_slot}'
