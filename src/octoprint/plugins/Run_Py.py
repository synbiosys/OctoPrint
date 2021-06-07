# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import sys
import time

import octoprint.plugin


class Run_PyPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):  # test
        self._logger.info("Run_py set up")
        script_path = (
            "/usr/bin/python3 /mnt/c/Repos/Synwave/data_acquisition/data_collection.py"
        )
        try:
            r = os.system(script_path)
        except:
            self._logger.error("Script could not be run")

    def hook_gcode_sent(
        self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs
    ):
        script_path = "python /mnt/c/Repos/octoprint/src/octoprint/plugins/hello_test.py"
        if gcode and cmd[:4] == "G0":
            self._logger.info("G0 registered")
            try:
                r = os.system(script_path)
            except:
                self._logger.error("Script could not be run")


__plugin_name__ = "Run Py"
__plugin_version__ = "1.0.0"
__plugin_description__ = "A plugin for OctoPrint to run a python script on a set trigger"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = Run_PyPlugin()


# def __plugin_load__():
# 	plugin = Run_PyPlugin()
#
# 	global __plugin_implementation__
# 	__plugin_implementation__ = plugin
#
# 	global __plugin_hooks__
# 	__plugin_hooks__ = {"octoprint.comm.protocol.action": plugin.custom_action_handler}
