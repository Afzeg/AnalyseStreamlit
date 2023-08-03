import unittest
from src.Models.database import User
from src.Controllers.auth import login, signin

class UnitTest(unittest.TestCase):


    def test_query(self):
        d = User()
        d.drop()
        d.setup("mail", "password")
        a = d.execute("Select * from users").fetchall()
        print(a)
        self.assertTrue(a[0][1]=='mail')
        self.assertTrue(a[0][2]=='password')

if __name__ == "__main__":
    unittest.main()
