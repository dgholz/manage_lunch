'''Command-line tool for managing lunches'''
import argparse
from pkg_resources import iter_entry_points

from manage_lunch import ManageLunch

def add_subcommands(parser, subcommands):
    for entrypoint in subcommands:
        command = entrypoint.load()
        subparser = parser.add_parser(entrypoint.name, description=command.__doc__)
        command.add_arguments(subparser)
        subparser.set_defaults(command=command)

def add_arguments(parser):
    command_parser = parser.add_subparsers(title='Commands')
    add_subcommands(command_parser, iter_entry_points('manage_lunch.command'))
    return parser

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    opts = add_arguments(parser).parse_args()
    optsd = vars(opts)
    command = optsd.pop('command')
    command(manage_lunch=ManageLunch(), **optsd).run()
