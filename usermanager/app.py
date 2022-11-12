from . import endless_function

from InquirerPy import inquirer
from InquirerPy.base.control import Choice, Separator


class App:
    @endless_function
    def home(self) -> bool:
        return True

    def run(self):
        try:
            self.home()
        except Exception as ex:
            print(ex)
        finally:
            self.db.close_connection()
