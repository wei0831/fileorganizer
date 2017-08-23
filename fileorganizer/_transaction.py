#!/usr/bin/python
""" _transaction.py

"""
import os
import _helper
import shutil
import logging

__author__ = "Jack Chang <wei0831@gmail.com>"


class Transaction:
    """ TODO
    """

    def __init__(self, old, new, action):
        """ TODO
        """
        self.loger = logging.getLogger(self.__class__.__name__)
        self.old = old
        self.new = new
        self.action = action
        self.status = {"dup": False, "done": False}

    def commit(self):
        """ TODO
        """
        if self.action == "mv":
            new_dir = os.path.dirname(self.new)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            new_file = os.path.basename(self.new)
            new_file_name = os.path.splitext(new_file)[0]
            new_file_ext = os.path.splitext(new_file)[1]
            if new_file in os.listdir(new_dir):
                self.status["dup"] = True
                i = 0
                new_file_name_attempt = self.new
                while os.path.exists(new_file_name_attempt):
                    i += 1
                    new_file_name_attempt = os.path.join(
                        new_dir,
                        new_file_name + "[Copy" + str(i) + "]" + new_file_ext)
                self.new = new_file_name_attempt
                self.loger.warning("[Duplicated] [%s]", self.new)

            shutil.move(self.old, self.new)
            self.status["done"] = True
            self.loger.info("[Moved] [%s] -> [%s]", self.old, self.new)

        if self.action == "rmdir":
            shutil.rmtree(self.old, ignore_errors=False, onerror=_helper.handleRemoveReadonly)
            self.status["done"] = True
            self.loger.info("[RMDIR] [%s]", self.old)

    def __str__(self):
        return "[%s] [%s] -> [%s]" % (self.action, self.old, self.new)

    def __repr__(self):
        return "<%s, %s, %s, %s>" % (self.action, self.old, self.new,
                                     self.status)
