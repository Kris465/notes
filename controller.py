from loguru import logger


class Controller:
    def __init__(self):
        self.action = ""

    def run(self, action):
        logger.info(f"Контроллер запущен. Пользователь выбрал: {action}")
        self.action = action
        match action:
            case 1:
                self.create_note()
            case 2:
                self.update_note()
            case 3:
                self.delete_note()
            case 4:
                self.show_all_notes()

    def create_note(self):
        pass

    def update_note(self):
        pass

    def delete_note(self):
        pass

    def show_all_notes(self):
        pass
