import os
import logging
import logging.config
import yaml

def initLoger(path='conf\\logging.yaml', default_level=logging.INFO):
    if not os.path.exists('log'):
        os.mkdir('log')

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        
        logging.config.dictConfig(config)
        logging.getLogger(__name__).debug("Config '%s' is loaded.", path)
    else:
        logging.basicConfig(level=default_level)