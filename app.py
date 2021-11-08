import os, json, logging
class DumbDB(object):
    """
        DumbDB: A really stoopud database that just json dumps every value you give it :)

    """
    
    def __init__(self, location=None):
        if location == None:
            location = "data.json"
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
       if os.path.exists(location):
           self._load()
       else:
           self.data = {}
       return True

    def _load(self):
        self.data = json.load(open(self.location, "r"))

    def dumpdb(self):
        try:
            json.dump(self.data, open(self.location, "w"))
            return True
        except:
            return False

    def set(self, key, value):
        try:
            self.data[str(key)] = value
            self.dumpdb()
        except Exception as e:
            logging.error("Couldn't save values to db", str(e))
            return False

    def get(self, key, default=[]):
        try:
            return self.data[key]
        except KeyError as e:
            logging.error("Couldn't fetch values from db", str(e))
            return default

    def delete(self, key):
        if not key in self.data:
            return False
        del self.data[key]
        self.dumpdb()
        return True
