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
            if os.path.exists(self.new):
                self.status["dup"] = True
                dirpath = os.path.dirname(self.new)
                filename = os.path.splitext(os.path.basename(self.new))[0]
                fileext = os.path.splitext(os.path.basename(self.new))[1]
                i = 0
                newname_attempt = self.new
                while os.path.exists(newname_attempt):
                    i += 1
                    newname_attempt = os.path.join(
                        dirpath, filename + "[Copy" + str(i) + "]" + fileext)
                self.new = newname_attempt

            shutil.move(self.old, self.new)
            self.status["done"] = True

    def __str__(self):
        return "[%s] [%s] -> [%s] [%s]" % (self.action, self.old, self.new,
                                           self.status)

    def __repr__(self):
        return "<%s, %s, %s, %s>" % (self.action, self.old, self.new,
                                     self.status)
