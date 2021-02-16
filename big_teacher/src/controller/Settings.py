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
import logging


class Settings:
    '''
    Settings class to read and write application config to file
    '''
    def __init__(self, config_file):
        '''
        :param config_file:String:Name of config file to read/write
        :param section:String:Name of section to be added/modified
        '''
        self.config = configparser.ConfigParser(interpolation=None)
        self.configFile = config_file
        self.config.read(self.configFile)

    def db_config_write(self, section, **settings):
        '''
        Writes config to file
        :params section:String:config section to write
        :param:String:key='value' format
        :return:Dict:key value pairs from config section
        '''
        logger = logging.getLogger(__name__)
        # Try-except for duplicate section error, allowing field overwrites
        try:
            self.config.add_section(section)
        except:
            # This line will eventually be passed to a status bar in Gui
            logger.info(f"{section} section already exists...overwriting data")

        # Unpacks all kwargs passed in and saves as config file field, value
        for field, value in settings.items():
            if field == 'class_':
                self.config.set(section, field[:-1], value.format())
            else:
                self.config.set(section, field, value.format())

        # Writes config to file
        with open(self.configFile, "w") as file:
            self.config.write(file)

        config_values = self.db_config_read(section)
        logger.info(f'config.ini {section} updated')
        return config_values

    def db_config_read(self, section):
        '''
        Reads config from file
        :params section:String:config section to read
        :return:Dict:key value pairs from config section
        '''
        logger = logging.getLogger(__name__)
        try:
            config_values = dict(self.config.items(section))
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
        settings = Settings('config.ini')
        # Set logger settings in config.ini
        settings.db_config_write(section='loggers', keys='root')
        settings.db_config_write(section='handlers', keys='stream_handler,file_handler')
        settings.db_config_write(section='formatters', keys='simple,complex')
        settings.db_config_write(section='logger_root', level='INFO', handlers='stream_handler,file_handler')
        settings.db_config_write(section='handler_file_handler', class_='FileHandler', formatter='complex', level='INFO', args="('big_teacher/logs/big_teacher.log',)")
        settings.db_config_write(section='handler_stream_handler', class_='StreamHandler', level='INFO', formatter='simple', args="(sys.stderr,)")
        settings.db_config_write(section='formatter_simple', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        settings.db_config_write(section='formatter_complex', format='%(asctime)s - %(name)s - %(levelname)s - %(module)s : %(lineno)d - %(message)s')
