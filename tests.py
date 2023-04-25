import requests
import unittest

root = 'http://127.0.0.1:5000/'

class CorrectInputs(unittest.TestCase):
    
    def test_avg_exchange_rate(self):
        expected_result = '2.7824'
        date= '2020-11-10'
        currency = 'AUD'
        response = requests.get(root+f'exchanges/{currency}/{date}')
        content = response.content.decode('utf-8-sig')
        self.assertEqual(content, expected_result)


    def test_min_max_avg_value(self):
        expected_result = {"max_exch_rate": 4.3742,"min_exch_rate": 4.1905}
        currency = 'USD'
        days = '23'
        response = requests.get(root+f'min-max/{currency}/{days}')
        content = response.content.decode('utf-8-sig')
        self.assertEqual(eval(content), expected_result)


    def test_min_major_diff(self):
        expected_result = {"date": "2023-04-04","difference": "0.0084"}
        currency = 'NOK'
        days = '14'
        response = requests.get(root+f'major-diff/{currency}/{days}')
        content = response.content.decode('utf-8-sig')
        self.assertEqual(eval(content), expected_result)

class IncorrectInputs(unittest.TestCase):

    def test_invalid_currency(self):
        expected_result = 'ERROR: Invalid currency code!'
        date= '2020-11-10'
        currency = 'NOoK'
        response = requests.get(root+f'exchanges/{currency}/{date}')
        content = response.content.decode('utf-8-sig')
        self.assertEqual(content, expected_result)


    def test_invalid_date_format(self):
        expected_result = "ERROR: Date must be in YYYY-MM-DD format!"
        date= '2020-11sss'
        currency = 'NOK'
        response = requests.get(root+f'exchanges/{currency}/{date}')
        content = response.content.decode('utf-8-sig')
        self.assertEqual(content, expected_result)


    def test_invalid_number_of_days(self):
        expected_result = "ERROR: Number of days must be integer smaller or equal to 255!"
        currency = 'NOK'
        days = '14s'
        response = requests.get(root+f'major-diff/{currency}/{days}')
        content = response.content.decode('utf-8-sig')
        self.assertEqual(content, expected_result)

class OtherErrors(unittest.TestCase):

    def test_weekend_date(self):
        expected_result = 'ERROR:  404 Client Error: Not Found - Brak danych for url: http://api.nbp.pl/api/exchangerates/rates/a/USD/2020-10-10/'
        date= '2020-10-10'
        currency = 'USD'
        response = requests.get(root+f'exchanges/{currency}/{date}')
        content = response.content.decode('utf-8-sig')
        self.assertEqual(content, expected_result)


    def test_date_out_off_range(self):
        expected_result = "ERROR:  404 Client Error: Bark danych / No data available for url: http://api.nbp.pl/api/exchangerates/rates/a/USD/1027-10-10/"
        date= '1027-10-10'
        currency = 'USD'
        response = requests.get(root+f'exchanges/{currency}/{date}')
        content = response.content.decode('utf-8-sig')
        self.assertEqual(content, expected_result)


if __name__ == '__main__':
    unittest.main()