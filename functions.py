from utilities import nbp_url, make_request, validate_input


def avg_exchange_rate(currency: str, date: str) -> str:
    """
    Takes currency code and date in format, returns
    average exchange rate for that currency on that date.
    """
    is_data_wrong = validate_input(currency, date, 1)
    if is_data_wrong:
        return is_data_wrong
    
    url = f'{nbp_url}/rates/a/{currency}/{date}/'
    data = make_request(url)
    if type(data) == str:
        return data
    
    return str(data['rates'][0]['mid'])
    

def major_difference(currency: str, days: str) -> dict:
    """
    Takes currency code and number of last quotations (days), returns
    a dictionary with biggest daily difference between the buy and aks 
    rates from last n days and date when it happened.
    """
    is_data_wrong = validate_input(currency, days, 2)
    if is_data_wrong:
        return is_data_wrong

    url = f'{nbp_url}/rates/c/{currency}/last/{days}/'
    data = make_request(url)
    if type(data) == str:
        return data
    data = data['rates']
    max_diff = data[0]['ask'] - data[0]['bid']
    date = data[0]['effectiveDate']
    for day in data:
        bid = day['bid']
        ask = day['ask']
        diff = ask - bid
        if diff > max_diff:
            date = day['effectiveDate']
            max_diff = diff

    return {'date': date, 'difference': str(round(max_diff,5))}


def min_max_average(currency: str, days: str) -> dict:
    """
    Takes currency code and the number of last quotations (days), returns a
    dictionary with the min and max average exchange rate for that currency
    from last n days.
    """
    is_data_wrong = validate_input(currency, days, 2)
    if is_data_wrong:
        return is_data_wrong
    
    url = f'{nbp_url}/rates/a/{currency}/last/{days}/'
    data = make_request(url)
    if type(data) == str:
        return data
    data = data['rates']
    max_rate = data[0]['mid']
    min_rate = max_rate
    for day in data:
        rate = day['mid']
        if rate < min_rate:
            min_rate = rate
        if rate > max_rate:
            max_rate = rate

    return {'min_exch_rate': min_rate, 'max_exch_rate': max_rate}
    
