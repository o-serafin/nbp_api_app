import requests
import datetime

nbp_url = 'http://api.nbp.pl/api/exchangerates'

def get_currencies() -> list:
    """Fuction returns list of available currency codes"""
    url = f'{nbp_url}/tables/a/'
    data = make_request(url)[0]['rates']
    if type(data) == str:
        return data
    currencies = []
    for item in data:
        currencies.append(item['code'])
    return currencies
   

def validate_date(date_text:str)->bool:
    """Validates if date is in YYYY-MM-DD format"""
    try:
        datetime.date.fromisoformat(date_text)
        return True
    except ValueError:
        return False


def make_request(url:str):
    """Make and validate request to the NBP API"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.content.decode('utf-8-sig')
        return eval(content)
    except Exception as error:
        return "ERROR:  " + str(error)

  
def validate_input(currency:str, parameter:str, validation_type:int):
    """Checks if user input is in correct format"""
    currencies = get_currencies()
    if currency not in currencies:
        return 'ERROR: Invalid currency code!'
    if validation_type == 1:
        if not validate_date(parameter):
            return 'ERROR: Date must be in YYYY-MM-DD format!'
    if validation_type == 2:
        if not parameter.isnumeric() or int(parameter) > 255:
            return 'ERROR: Number of days must be integer smaller or equal to 255!'
    return False
