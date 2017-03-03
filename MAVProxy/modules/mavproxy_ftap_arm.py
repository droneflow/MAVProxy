#!/usr/bin/env python
'''command long'''

import time, os
from pymavlink import mavutil

from MAVProxy.modules.lib import mp_module

class FtapArmModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(FtapArmModule, self).__init__(mpstate, "ftap_arm")
        self.add_command('arm_servos', self.cmd_arm_servos, "Arm only servos.")
        self.add_command('arm_motor', self.cmd_arm_motor, "Arm everything.")
        self.add_command('disarm', self.cmd_disarm, "Disarm all.")
        self.add_command('disarm_motor', self.cmd_disarm_motor, "Disarm motor");

    def cmd_arm_servos(self, args):
        print("Arming servos.")
        self.master.mav.ftap_safety_send(1) 
        self.master.mav.command_long_send(self.settings.target_system,
                              self.settings.target_component,
                              176,
                              0, 192, 0, 0, 0, 0, 0, 0)

    def cmd_arm_motor(self, args):
        print("Arming motor.")
        self.master.mav.ftap_safety_send(2) 
        self.master.mav.command_long_send(self.settings.target_system,
                      self.settings.target_component,
                      176,
                      0, 192, 0, 0, 0, 0, 0, 0)

    def cmd_disarm(self, args):
        print("Disarming all.")
        self.master.mav.ftap_safety_send(0);
        self.master.mav.command_long_send(self.settings.target_system,
                              self.settings.target_component,
                              176,
                              0, 64, 0, 0, 0, 0, 0, 0)

    def cmd_disarm_motor(self, args):
          print("Disarming motor.")
          self.master.mav.ftap_safety_send(1);

    def do_command(self, command):
          print command
          if command == 'arm_servos':
            print "here...."
            self.cmd_arm_servos('')
          elif command == 'disarm':
            self.cmd_disarm('')
          elif command == 'arm_motor':
            self.cmd_arm_motor('')
          elif command == 'disarm_motor':
            self.cmd_disarm_motor('')



def init(mpstate):
    '''initialise module'''
    return FtapArmModule(mpstate)
