import sys

from loguru import logger

from controller import Controller
from view import View


def main():
    logger.remove(0)
    logger.add(
        "file.log",
        level="INFO",
        retention="3 days",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )
    
    controller = Controller()
    view = View()
    
    action = view.start_menu()
    controller.run(action)


if __name__ == '__main__':
    main()
