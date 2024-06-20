from collections import UserDict


class DotConfig(UserDict):
    def __getitem__(self, item):
        if item not in self:
            self[item] = DotConfig()
        return super().__getitem__(item)

    def __getattr__(self, item):
        return self.__getitem__(item)

    def __setattr__(self, key, value):
        return self.__setitem__(key, value)

    def __delattr__(self, item):
        return self.__delitem__(item)


class Config(DotConfig):
    pass
