#!/usr/bin/python
""" _transaction.py

"""
import os
import shutil

__author__ = "Jack Chang <wei0831@gmail.com>"


class Transaction:
    """ TODO
    """

    def __init__(self, old, new, action):
        """ TODO
        """
        self.old = old
        self.new = new
        self.action = action
        self.status = {"dup": False, "done": False}

    def commit(self):
        """ TODO
        """
        if self.action == "move":
            new_dir = os.path.dirname(self.new)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)

            new_file_name = os.path.splitext(os.path.basename(self.new))[0]
            new_file_ext = os.path.splitext(os.path.basename(self.new))[1]
            if os.path.exists(self.new):
                self.status["dup"] = True
                i = 0
                new_file_name_attempt = self.new
                while os.path.exists(new_file_name_attempt):
                    i += 1
                    new_file_name_attempt = os.path.join(
                        new_dir,
                        new_file_name + "[Copy" + str(i) + "]" + new_file_ext)
                self.new = new_file_name_attempt

            shutil.move(self.old, self.new)
            self.status["done"] = True

        if self.action == "rmdir":
            os.rmdir(self.old)
            self.status["done"] = True

    def __str__(self):
        return "[%s] [%s] -> [%s] [%s]" % (self.action, self.old, self.new,
                                           self.status)

    def __repr__(self):
        return "<%s, %s, %s, %s>" % (self.action, self.old, self.new,
                                     self.status)
