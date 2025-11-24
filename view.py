from loguru import logger


class View:
    def __init__(self):
        self.action = ""
        
    def start_menu(self):
        logger.info("Пользовательское меню вызвано")
        print("Я-приложение заметки.")
        print("1. Создать заметку\n",
              "2. Редактировать заметку\n",
              "3. Удалить заметку\n")
        action = int(input("Введите вариант: "))
        return action
