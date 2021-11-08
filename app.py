import os, json, logging

class DumbDB(object):
    """
        DumbDB: A really stoopid database that just json dumps every value you give it :)

    """
    
    def __init__(self, location=None, file_name=None):
        if location == None:
            location = os.curdir
        if file_name == None:
            file_name = "data.json"
        full_path = os.path.join(location, file_name)
        self.full_path = os.path.expanduser(full_path)
        self.load(self.full_path)

    def load(self, full_path):
       if os.path.exists(full_path):
           self._load()
       else:
           self.data = {}
       return True

    def _load(self):
        self.data = json.load(open(self.full_path, "r"))

    def dumpdb(self):
        try:
            json.dump(self.data, open(self.full_path, "w"))
            return True
        except:
            return False

    def set(self, key, value):
        try:
            self.data[str(key)] = value
            self.dumpdb()
        except Exception as e:
            logging.error("Couldn't save values to db")
            logging.debug(str(e))
            return False

    def get(self, key, default=[]):
        try:
            return self.data[key]
        except KeyError as e:
            logging.error("Couldn't fetch values from db")
            logging.debug(str(e))
            return default

    def delete(self, key):
        if not key in self.data:
            return False
        del self.data[key]
        self.dumpdb()
        return True
