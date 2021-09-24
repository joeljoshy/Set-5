import unittest
import py1

class Test(unittest.TestCase):

    def test_getuser(self):

        response = py1.get_user(1)
        self.assertEqual(response,{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'})
    def test_getdetail(self):

        response = py1.get_detail(1)
        self.assertEqual(response, "quia et suscipit\n"
                                   "suscipit recusandae consequuntur expedita et cum\n"
                                   "reprehenderit molestiae ut ut quas totam\n"
                                   "nostrum rerum est autem sunt rem eveniet architecto")


if __name__=="__main__":
    unittest.main()