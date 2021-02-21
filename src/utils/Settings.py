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
    Settings class to read and write settings config to file
    '''

    def __init__(self, config_file):
        '''
        :param config_file:String:Name of config file to read/write
        :param section:String:Name of section to be added/modified
        '''
        self.logger = logging.getLogger(__name__)
        self.config = configparser.ConfigParser(interpolation=None)
        self.config_file = config_file
        self.config.read(self.config_file)
        self.config_values = None

    def db_config_write(self, section, **settings):
        '''
        Writes config to file
        :params section:String:config section to write
        :param:String:key='value' format
        :return:Dict:key value pairs from config section
        '''
        # Try-except for duplicate section error, allowing field overwrites
        try:
            self.config.add_section(section)
        except:
            # This line will eventually be passed to a status bar in Gui
            self.logger.info(f"{section} section already exists...overwriting data")

        # Unpacks all kwargs passed in and saves as config file field, value
        for field, value in settings.items():
            if field == 'class_':
                self.config.set(section, field[:-1], value.format())
            else:
                self.config.set(section, field, value.format())
            self.logger.info(f'config.ini {section} updated')
        return self.config

    def write_config(self, config):
        '''
        Writes config to disk
        '''
        with open(self.config_file, 'w') as file:
            self.config.write(file)

    def db_config_read(self, section):
        '''
        Reads config from file
        :params section:String:config section to read
        :return:Dict:key value pairs from config section
        '''
        try:
            self.config_values = dict(self.config.items(section))
            return self.config_values
        except configparser.NoSectionError as error:
            self.logger.error(error)

    def check_log_dir(self, directory):
        '''
        Checks for log directory and settings file
        :return:True if directory and file are found
        '''
        return bool(os.path.isdir(directory))

    def check_log_config(self, file):
        '''
        Check for defaultconfig.ini
        :params file:Check for config file on system
        :return:True if file exists
        '''
        return bool(os.path.isfile(file))

    def create_log_settings(self, file, directory, dir_true):
        '''
        Creates
        '''
        # Check for log dir, create if not
        if not dir_true:
            os.mkdir(directory)
            self.logger.info('logs directory created')
        # Make logger settings in config.ini
        self.db_config_write(section='loggers', keys='root')
        self.db_config_write(section='handlers', keys='stream_handler,file_handler')
        self.db_config_write(section='formatters', keys='simple,complex')
        self.db_config_write(section='logger_root', level='INFO', handlers='stream_handler,file_handler')
        self.db_config_write(section='handler_file_handler', class_='FileHandler', formatter='complex',
                                 level='INFO', args="('src/logs/big_teacher.log',)")
        self.db_config_write(section='handler_stream_handler', class_='StreamHandler', level='INFO',
                                 formatter='simple', args="(sys.stderr,)")
        self.db_config_write(section='formatter_simple',
                                 format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.db_config_write(section='formatter_complex',
                                 format='%(asctime)s - %(name)s - %(levelname)s - %(module)s : %(lineno)d - %(message)s')
        return True
