import unittest
from src.Models.database import Database
from src.Controllers.auth import login, signin

class UnitTest(unittest.TestCase):
    """
    def test_azerty(self):
        a="azerty"
        b="AZERTY"
        b=b.lower()
        self.assertEqual(a, b, "le test azerty n'a pas fonctionné")
    """

    def test_query(self):
        d = Database()
        d.drop()
        d.setup()
        a = d.execute("Select * from users").fetchall()
        print(a)
        self.assertTrue(a[0][1]=='erwan@mail.fr')
        self.assertTrue(a[0][2]=='b475e159b81477ac64accabe4514b50768e064abdfdc40529373dbab984b0b82')

if __name__ == "__main__":
    unittest.main()




