from dndlib.utils.config_ops import digest_config


class Container(object):
    def __init__(self, **kwargs):
        digest_config(self, kwargs)

    def add(self, *items):
        """
        Generic method to add items to Container.
        Must be implemented by subclasses.
        """
        raise Exception(
            "Container.add is not implemented; it is up to derived classes to implement")

    def remove(self, *items):
        """
        Generic method to remove items from Container.
        Must be implemented by subclasses.
        """
        raise Exception(
            "Container.remove is not implemented; it is up to derived classes to implement")
