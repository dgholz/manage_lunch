from configparser import ConfigParser
import os
import os.path
from pkg_resources import iter_entry_points

from manage_lunch import ManageLunch

class ManageLunchNoConfig(Exception): pass
class ManageLunchUnknownPlugin(Exception): pass

def find_config():
    here = os.getcwd()
    config_file = os.path.join(here, 'munch.ini')
    if not os.path.isfile(config_file):
        raise ManageLunchNoConfig(here)
    config = ConfigParser()
    config.read(config_file)
    return config

def make_sections(config):
    for section in config.sections():
        yield section, dict(config.items(section))

def get_plugins():
    return dict(list([(e.name, e.load()) for e in iter_entry_points('manage_lunch.plugin')]))

def assemble_munch(sections, plugin_classes):
    munch = ManageLunch()
    for title, payload in sections:
        plugin_class = plugin_classes.get(title, None)
        if plugin_class is None:
            raise ManageLunchUnknownPlugin(title)
        plugin = plugin_class(munch=munch, **payload)
        plugin.register()

    return munch

def build_munch():
    config = find_config()
    section_stream = make_sections(config)
    plugin_lookup = get_plugins()
    return assemble_munch(section_stream, plugin_lookup)
