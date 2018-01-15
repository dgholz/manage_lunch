import collections.abc
from configparser import ConfigParser
import os
import os.path
from pkg_resources import iter_entry_points

import six
from werkzeug.datastructures import MultiDict

from manage_lunch import ManageLunch

class ManageLunchNoConfig(Exception): pass
class ManageLunchUnknownPlugin(Exception): pass

def find_config():
    here = os.getcwd()
    config_file = os.path.join(here, 'munch.ini')
    if not os.path.isfile(config_file):
        raise ManageLunchNoConfig(here)
    config = ConfigParser(strict=False, dict_type=MultiDict)
    config.read(config_file)
    return config

def make_sequence(config):
    for section in config.sections():
        yield section, dict(config.items(section))

def get_plugins():
    return dict(list([(e.name, e.load()) for e in iter_entry_points('manage_lunch.plugin')]))

def assemble_munch(sequence, plugin_classes):
    munch = ManageLunch()
    for title, payload in sequence:
        plugin_class = plugin_classes.get(title, None)
        if plugin_class is None:
            raise ManageLunchUnknownPlugin(title)
        try:
            aliases = plugin_class.multivalue_aliases()
        except AttributeError:
            aliases = {}

        def scalar(val):
            return isinstance(val, six.string_types) or not isinstance(val, collections.abc.Sequence)

        for k, v in payload.items():
            if k in aliases:
                payload.pop(k)
                if scalar(v):
                    v = [v]
                payload[aliases[k]] = v

        plugin = plugin_class(munch=munch, **payload)
        plugin.register()

    return munch

def build_munch():
    config = find_config()
    sequence = make_sequence(config)
    plugin_lookup = get_plugins()
    return assemble_munch(sequence, plugin_lookup)
