from loguru import logger


class Controller:
    def __init__(self):
        self.action = ""
    
    def run(self, action):
        logger.info(f"Контроллер запущен. Пользователь выбрал: {action}")
        self.action = action
        
