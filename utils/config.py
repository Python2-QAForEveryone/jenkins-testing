import os
import strictyaml as yaml
from collections import namedtuple


class Config:
    """
    Class for initializing config
    """

    config_file = os.environ.get('CONFIG', 'data/config.yaml').lower()
    default_config = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_file)

    @staticmethod
    def get_yaml(file: str):
        # Check that file exists in specified path
        if not os.path.exists(file):
            print(f'Config file not found: {file}')
            raise Exception('Config file not found')
        # Reading file
        f = open(file, 'r').read()
        print(f'Loading file: {file}')
        conf = yaml.load(f)
        return conf.data

    @staticmethod
    def get_config(file: str = default_config):
        """
        Method for parsing config file
        :param file: path to config
        :return: config object with the same structure as yaml file
        """
        # Getting environment variable for running tests, if non set up default will be set to local
        env = os.environ.get('ENV', 'local').lower()
        # Allowing to set staging env values to stage, stg or staging
        if env.lower() == 'travis':
            env = 'travis'
        # If not proper config specified
        print(f'Picking environment: {env}')
        print(f'Loading config file: {file}')
        # Loading yaml file
        conf = Config.get_yaml(file)
        # Setting up local config for appropriate environment
        env_config = conf['environment'][env.lower()]

        return Config.get_object_from_dict(env_config), env

    @staticmethod
    def get_object_from_dict(dictionary):
        for k, v in dictionary.items():
            if isinstance(v, dict):
                dictionary[k] = Config.get_object_from_dict(v)
        return namedtuple('object', dictionary.keys())(*dictionary.values())
