###############################################
# Purpose: Creates or modifies sections of    #
# configuration files.                        #
#                                             #
# Licensed under the MIT license. See LICENSE #
# file in project root for details.           #
#                                             #
# https://github.com/tinfins/CMSC495-Group-3/ #
###############################################

#pylint:disable=C0103
from configparser import ConfigParser


class Settings:
    """
    Settings class to read and write application config to file
    """
    def __init__(self, config_file, section):
        """
        :param config_file:String:Name of config file to read/write
        :param section:String:Name of section to be added/modified
        """ 
        self.config = ConfigParser()
        self.configFile = config_file
        self.config.read(self.configFile)
        self.db_section = section
    
    def db_config_write(self, **settings):
        """
        Writes config to file
        :param:String:Database endpoint conn
        :return:String:host, username, password, db
        """
        # Try-except for duplicate section error, allowing field overwrites
        try:
            self.config.add_section(self.db_section)
        except:
            # This line will eventually be passed to a status bar in Gui
            print("Section already exists...overwriting data")
        
        # Unpacks all kwargs passed in and saves as config file field, value
        for field, value in settings.items():
            self.config.set(self.db_section, field, value)
        
        # Writes config to file
        with open(self.configFile, "w") as file:
            self.config.write(file)
        
        config_values = self.db_config_read()
        return config_values

    def db_config_read(self):
        """
        Reads config from file
        :return:String:host, username, password, db
        """
        config_values = dict(self.config.items(self.db_section))

        return config_values
