import unittest
from src.Models.database import Database
from src.Controllers.auth import login, signin

class UnitTest(unittest.TestCase):


    def test_query(self):
        d = Database()
        d.drop()
        d.setup()
        a = d.execute("Select * from users").fetchall()
        print(a)
        self.assertTrue(a[0][1]=='erwan@mail.fr')
        self.assertTrue(a[0][2]=='932a8e294c3c14a0f47ad4df4890bf25b034038ba88fe9fddf4b727076cc12ef')

if __name__ == "__main__":
    unittest.main()




