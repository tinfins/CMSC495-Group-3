from big_teacher.src.gui import LoginGui
from Settings import NoSettings
import logging.config


if __name__ == '__main__':
    check_settings = NoSettings.check_settings()
    if check_settings:
        LoginGui.main()
    else:
        NoSettings.create_logging_settings()
        logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
        logger = logging.getLogger(__name__)
        logger.info('config.ini file created')
        LoginGui.main()


