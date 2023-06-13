import time

class Utilities:

    def util(self, lists, values):

        for result in lists:
            if values in result.text:
                result.click()
                break
        time.sleep(7)
