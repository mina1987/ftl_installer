# -*- coding: utf-8 -*-
import argparse
import ftl_installer
import logging
import pprint
import yaml

class ConfigHandler(object):
    '''
    Class to handle the configuration given with `--config` option
    '''

    def __init__(self, config_file):
        with open(config_file) as config_file:
            self.stored_config = yaml.safe_load(config_file)


class Parser(object):
    ''' The parser. '''
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Ansible based installer framework.')

        self.parser.add_argument('-V', '--version', action='version',
                                 version="ftl_installer-{0}".format(ftl_installer.__version__))

        self.parser.add_argument('-v', '--verbose', action='store_true', dest='verbose',
                                 default=False, help='show verbose output')

        self.parser.add_argument('-q', '--quiet', action='store_true', dest='quiet',
                                 default=False, help='supress output')

        self.parser.add_argument('-c', '--config', help='config file')


def main():  # pragma: no cover
    ''' This is the entrypoint for ftl_installer '''
    parser = Parser()
    args = parser.parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    ftl_logger = logging.getLogger('ftl')
    ftl_logger.setLevel(log_level)

    ftl_stream_handler = logging.StreamHandler() if not args.quiet else logging.NullHandler()
    log_string = "%(message)s"
    ftl_stream_formatter = logging.Formatter(log_string)
    ftl_stream_handler.setFormatter(ftl_stream_formatter)
    ftl_stream_handler.setLevel(log_level)

    ftl_logger.addHandler(ftl_stream_handler)
    ftl_logger.debug("initialized ftl-logging at level: {0}".format(log_level))

    # If the configuration file is provided, parse and store it.
    if args.config:
        ftl_config = ConfigHandler(args.config)
        # for test purpose, remove later
        pprint.pprint(ftl_config.stored_config)

    # Do stuff.
    # args.cmd(args)


if __name__ == '__main__':  # pragma: no cover
    main()
