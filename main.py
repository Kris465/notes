import sys

from loguru import logger

from controller import Controller


def main():
    logger.remove(0)
    logger.add(
        "file.log",
        level="INFO",
        retention="3 days",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )
    
    controller = Controller()
    controller.run()


if __name__ == '__main__':
    main()
