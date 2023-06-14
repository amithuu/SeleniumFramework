import time
import softest


# this we have not used anywhere as I have not used the comparison of the data in drop-down , we will use it in future!!


class Utilities(softest.TestCase):

    def util(self, lists, values):

        for result in lists:
            if values in result.text:
                result.click()
                break
        time.sleep(7)

# this is for soft assertion as we know if any testcase is going to fail we can use it so the flow will not stop!!!!!
    def softassert(self, lists, values):
        for result in lists:
            self.soft_assert(self.assertEqual, lists, values)
            if result.text == values:
                result.click()
                print("pass")
                break
            else:
                print("fail")
        time.sleep(7)
        self.assert_all()
# assert_all is for the report that to show.

