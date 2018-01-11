'''Command-line tool for managing lunches'''
import argparse
from pkg_resources import iter_entry_points
import sys

from manage_lunch import ManageLunch

def add_subcommands(parser, subcommands):
    for entrypoint in subcommands:
        command = entrypoint.load()
        doc = sys.modules[command.__module__].__doc__
        subparser = parser.add_parser(entrypoint.name, help=doc)
        command.add_arguments(subparser)
        subparser.set_defaults(command=command)

def add_arguments(parser):
    command_parser = parser.add_subparsers(title='Commands')
    add_subcommands(command_parser, iter_entry_points('manage_lunch.command'))
    return parser

def get_plugins():
    for entrypoint in iter_entry_points('manage_lunch.plugin'):
        yield entrypoint.load()

def assemble_munch():
    munch = ManageLunch()
    for plugin_class in get_plugins():
        plugin = plugin_class(munch)
        plugin.register()
    return munch

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    opts = add_arguments(parser).parse_args()
    optsd = vars(opts)
    command = optsd.pop('command', None)
    if command is not None:
        command(munch=assemble_munch(), **optsd).run()
    else:
        parser.print_help()
