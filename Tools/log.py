import logging
import logging.config
from os import path


log_file_path = path.join(path.dirname(path.abspath(__file__)), '../log/mini.log')
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=log_file_path,
                filemode='w')