class ManageLunchRole:
    @classmethod
    def does(cls, role_name):
        def get_roles(cls):
            try:
                ancestors = cls.__mro__
            except AttributeError:
                from inspect import getmro
                ancestors = getmro(cls)
            for ancestor in ancestors:
                if issubclass(ancestor, ManageLunchRole):
                    yield ancestor

        if type(cls) != type:
            cls = type(cls)
        return role_name in [_.__name__ for _ in get_roles(cls)]
