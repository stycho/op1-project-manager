import os

class Op1Device:
    OP1_UUID = '54FF-1FEE'
    OP1_MOUNT_POINT = '/media/op1'
    MOUNT_SCRIPT = '/home/pi/Documents/development/op1_project_manager/scripts/mount_op1.sh'
    UNMOUNT_SCRIPT = '/home/pi/Documents/development/op1_project_manager/scripts/unmount_op1.sh'

    def __init__(self):
        return

    def mount_drive(self):
        os.system(f'{self.MOUNT_SCRIPT} {self.OP1_UUID}')

    def unmount_drive(self):
        os.system(f'{self.UNMOUNT_SCRIPT} {self.OP1_UUID}')

    def check_is_mounted(self):
        return

    def get_op1_mount_point(self):
        return self.OP1_MOUNT_POINT
