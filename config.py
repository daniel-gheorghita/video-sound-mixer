import configparser
import os

class Config():
    def __init__(self, file, logger = None):
        config = configparser.ConfigParser()
        config.read(file)

        self.input_folder = os.path.join(
                                os.path.join(
                                    os.path.dirname(__file__),
                                    config['GENERAL']['input_folder']))
        self.input_wav = os.path.join(
                                os.path.join(
                                    os.path.dirname(__file__),
                                    config['GENERAL']['input_wav']))
        self.input_image = os.path.join(
                                os.path.join(
                                    os.path.dirname(__file__),
                                    config['GENERAL']['input_image']))
        self.output_folder = os.path.join(
                                os.path.join(
                                    os.path.dirname(__file__), 
                                    config['GENERAL']['output_folder']))

        # how many seconds from the start of the input wav to preserve
        self.clean_seconds_start = config["MIXING"]["clean_seconds_start"]
        self.clean_seconds_start = [int(float(s)) for s in self.clean_seconds_start.replace(' ', '').split(',')]
        # how many seconds from the start of the input wav to preserve
        self.clean_seconds_end = config["MIXING"]["clean_seconds_end"]
        self.clean_seconds_end = [int(float(s)) for s in self.clean_seconds_end.replace(' ', '').split(',')]
        # how long should the output be (0 for preserving the original length)
        self.chunk_duration_seconds = int(float(config["MIXING"]["chunk_duration_seconds"]))
        #self.chunk_duration_seconds = [int(float(s)) for s in self.chunk_duration_seconds.replace(' ', '').split(',')]
        # how long should the output be (0 for preserving the original length)
        self.total_duration_seconds = config["MIXING"]["total_duration_seconds"]
        self.total_duration_seconds = [int(float(s)) for s in self.total_duration_seconds.replace(' ', '').split(',')]
        # how long should the output be (0 for preserving the original length)
        self.mixing_ratios_db = config["MIXING"]["mixing_ratios_db"]
        self.mixing_ratios_db = [int(float(s)) for s in self.mixing_ratios_db.replace(' ', '').split(',')]
        
        self.logger = logger