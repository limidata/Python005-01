# Python 标准库：日志处理
import logging


def log_audit():

    logging.basicConfig(filename='d:/test.log',
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(name)-8s (levelname)-8s [line: %(lineno)d] %(message)s')

    logging.debug('debug message')
    logging.info('debug message')
    logging.warning('debug message')
    logging.error('debug message')
    logging.critical('debug message')

if __name__ == '__main__':
    log_audit()
