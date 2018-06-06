import requests

from cryptpredicter.models import BpiPriceUpdate

HISTORICAL_BPI = 'https://api.coindesk.com/v1/bpi/historical/close.json'


def populate_database():
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-01-01&end=2018-03-01'

    response = requests.get(url)
    data = response.json()
    i = 0
    for k, v in data['bpi'].items():
        row = BpiPriceUpdate(update_time=k, usd_value=v)
        row.save()
        i += 1
        yield (i)


def latest_value():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    response = requests.get(url)
    data = response.json()
    updated = data['time']['updatedISO']
    usd = data['bpi']['USD']['rate_float']
    gbp = data['bpi']['GBP']['rate_float']
    eur = data['bpi']['EUR']['rate_float']

    row = BpiPriceUpdate(update_time=updated, usd_value=usd, gbp_value=gbp,
                         eur_value=eur)
    row.save()
    return row


def get_json(url):
    response = requests.get(url)
    try:
        return response.json()
    except:
        return None


def get_currency_range(start, end, currency):
    url = '{}?start={}&end={}&currency={}'.format(HISTORICAL_BPI, start, end,
                                                  currency)
    json = get_json(url)
    currency_map = {
        'USD': 'usd_value',
        'EUR': 'eur_value',
        'GBP': 'gbp_value',
    }
    for update_date, index_value in json['bpi'].items():
        update = {
            'update_time': update_date,
            currency_map[currency]: index_value,
        }
        rows = BpiPriceUpdate.objects.filter(update_time=update_date).update(
            **update)
        if not rows:
            rows = BpiPriceUpdate.objects.create(**update)
        yield rows
