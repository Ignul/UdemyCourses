import unittest
from unittest.mock import patch
from example import Account


class ExampleTest(unittest.TestCase):

    def setUp(self):
        # Let's set up 2 accounts.
        self.acc1 = Account("John", "Lock", 50000)
        self.acc2 = Account("Jennifer", "Ann", 65025)

    def test_balance(self):
        self.assertEqual(self.acc1.balance, 50000)
        self.assertEqual(self.acc2.balance, 65025)

    def test_deposit(self):
        # Add 50$
        self.acc1.deposit(50)
        self.acc2.deposit(50)

        self.assertEqual(self.acc1.balance, 50050)
        self.assertEqual(self.acc2.balance, 65075)

        # Remove 50$
        self.acc1.deposit(-50)
        self.acc2.deposit(-50)

        self.assertEqual(self.acc1.balance, 50050)
        self.assertEqual(self.acc2.balance, 65075)

    def test_withdraw(self):
        # Withdraw 50$
        self.acc1.withdraw(50)
        self.acc2.withdraw(50)

        self.assertEqual(self.acc1.balance, 49950)
        self.assertEqual(self.acc2.balance, 64975)

        # Withdraw negative numbers.
        self.acc1.withdraw(-50)
        self.acc2.withdraw(-50)

        self.assertEqual(self.acc1.balance, 49950)
        self.assertEqual(self.acc2.balance, 64975)

    def test_get_email(self):
        with patch('example.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.text = f"{self.acc1.first_name}.{self.acc1.last_name}@localhost"

            response = self.acc1.retrieve_email()
            mock_get.assert_called_with("http://localhost/bankapi/Lock/John/email")
            self.assertEqual(response, "John.Lock@localhost")

            mock_get.return_value.ok = False

            response = self.acc2.retrieve_email()
            mock_get.assert_called_with("http://localhost/bankapi/Ann/Jennifer/email")
            self.assertEqual(response, "Bad Response!")


if __name__ == '__main__':
    unittest.main()
