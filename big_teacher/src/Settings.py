###############################################
# Purpose: Creates or modifies sections of    #
# configuration files.                        #
#                                             #
# Licensed under the MIT license. See LICENSE #
# file in project root for details.           #
#                                             #
# https://github.com/tinfins/CMSC495-Group-3/ #
###############################################

import configparser
import os
import sys
import logging


class Settings:
    """
    Settings class to read and write application config to file
    """

    def __init__(self, config_file, section):
        """
        :param config_file:String:Name of config file to read/write
        :param section:String:Name of section to be added/modified
        """
        self.config = configparser.ConfigParser(interpolation=None)
        self.configFile = config_file
        self.config.read(self.configFile)
        self.config_section = section

    def db_config_write(self, **settings):
        '''
        Writes config to file
        :param:String:Database endpoint conn
        :return:String:host, username, password, db
        '''
        logger = logging.getLogger(__name__)
        # Try-except for duplicate section error, allowing field overwrites
        try:
            self.config.add_section(self.config_section)
        except:
            # This line will eventually be passed to a status bar in Gui
            logger.info(f"{self.config_section} section already exists...overwriting data")

        # Unpacks all kwargs passed in and saves as config file field, value
        for field, value in settings.items():
            if field == 'class_':
                self.config.set(self.config_section, field[:-1], value.format())
            else:
                self.config.set(self.config_section, field, value.format())

        # Writes config to file
        with open(self.configFile, "w") as file:
            self.config.write(file)

        config_values = self.db_config_read()
        logger.info(f'config.ini {self.config_section} updated')
        return config_values

    def db_config_read(self):
        """
        Reads config from file
        :return:String:host, username, password, db
        """
        logger = logging.getLogger(__name__)
        try:
            config_values = dict(self.config.items(self.config_section))
            return config_values
        except configparser.NoSectionError as error:
            logger.error(error)


class NoSettings:
    # Refactor for modularity
    @classmethod
    def check_settings(cls):
        if os.path.exists('config.ini'):
            return True

    # Needs refactored for modularity?
    @classmethod
    def create_logging_settings(cls):
        Settings('config.ini', 'loggers').db_config_write(keys='root')
        Settings('config.ini', 'handlers').db_config_write(keys='stream_handler,file_handler')
        Settings('config.ini', 'formatters').db_config_write(keys='simple,complex')
        Settings('config.ini', 'logger_root').db_config_write(level='INFO', handlers='stream_handler,file_handler')
        Settings('config.ini', 'handler_file_handler').db_config_write(class_='FileHandler', formatter='complex',
                                                                       level='INFO', args="('big_teacher/logs/big_teacher.log',)")
        Settings('config.ini', 'handler_stream_handler').db_config_write(class_='StreamHandler', level='NOTSET',
                                                                         formatter='simple', args="(sys.stderr,)")
        Settings('config.ini', 'formatter_simple').db_config_write(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        Settings('config.ini', 'formatter_complex').db_config_write(
            format='%(asctime)s - %(name)s - %(levelname)s - %(module)s : %(lineno)d - %(message)s')
