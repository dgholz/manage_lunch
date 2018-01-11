'''Command-line tool for managing lunches'''
import argparse
from pkg_resources import iter_entry_points

from manage_lunch import ManageLunch

def add_arguments(parser):
    return parser

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    opts = add_arguments(parser).parse_args()
    ManageLunch(**optsd)
