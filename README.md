### Notes
* `sudo apt-get install eject`

# Create scripts to run sudo commands securly in python
### Change script ownership to root and make executable
eg.
* `sudo chown root:root ./scripts/mount_op1.sh`
* `sudo chmod 700 ./scripts/mount_op1.sh`

### Undo
* `sudo chown -R pi:pi ./scripts/mount_op1.sh`
* `sudo chmod -R 755 ./scripts/mount_op1.sh`

### Allow specific scripts to be run without sudo password
* Type sudo `visudo` at the terminal to open the sudo permissions (sudoers) file
* Around line 25, you'll see this line: %sudo ALL=(ALL:ALL) ALL
* Below that line, insert the following line, where username is your username:
```
pi  ALL=(ALL) NOPASSWD: /home/pi/Documents/development/op1_project_manager/scripts/mount_op1.sh
pi  ALL=(ALL) NOPASSWD: /home/pi/Documents/development/op1_project_manager/scripts/unmount_op1.sh
```
8 Exit the editor (Ctrl+X if nano)

### Call scripts from python
eg:
* `os.system('sudo ./scripts/mount_op1.sh')`