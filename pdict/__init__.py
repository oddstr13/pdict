import json


class AttrWrapper(object):
    _dict = None
    def __init__(self, d):
        assert isinstance(d, dict), ValueError("first argument must be instance of dict")
        object.__setattr__(self, "_dict", d)
    
    def __getattr__(self, name):
        _dict = object.__getattribute__(self, "_dict")
        return _dict[name]
    
    def __setattr__(self, name, value):
        _dict = object.__getattribute__(self, "_dict")
        _dict[name] = value
    
    def __delattr__(self, name):
        _dict = object.__getattribute__(self, "_dict")
        del _dict[name]


class PersistentDict(dict):
    filename = None
    filemode = "rt"
    encoding = "utf-8"
    backend  = json
    data = None

    def __init__(self, filename=None, encoding="utf-8", filemode="t", backend=json, *args, **kwargs):
        super(PersistentDict, self).__init__(*args, **kwargs)

        self.backend  = backend
        self.filename = filename
        self.filemode = filemode
        self.encoding = encoding
        self.data = AttrWrapper(self)

        if self.filename is not None:
            self.load()
    
    def load(self, filename=None, filemode=None, encoding=None, backend=None):
        if backend is not None:
            self.backend = backend
        if filemode is not None:
            self.filemode = filemode
        if encoding is not None:
            self.encoding = encoding
        if filename is not None:
            self.filename = filename
        
        if self.filename is not None:
            with open(self.filename, self.filemode + "r", encoding=self.encoding) as fh:
                self.clear()
                self.update(self.backend.load(fh))
        else:
            raise AttributeError("filename must not be `None`")
    
    def save(self, filename=None, filemode=None, encoding=None, backend=None):
        if backend is not None:
            self.backend = backend
        if filemode is not None:
            self.filemode = filemode
        if encoding is not None:
            self.encoding = encoding
        if filename is not None:
            self.filename = filename
        
        if self.filename is not None:
            with open(self.filename, self.filemode + "w", encoding=self.encoding) as fh:
                self.backend.dump(self, fh)


    def __setitem__(self, key, value):
        # optional processing here
        super(PersistentDict, self).__setitem__(key, value)
