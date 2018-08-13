import webbrowser
import datetime


def get_valdate_from_user():
    month = int(input('Input valuation month [MM].'))
    day = int(input('Input valuation day [DD].'))
    year = int(input('Input valuation year [YYYY].'))

    val_date = datetime.date(year, month, day)
    print('The valuation date is {}.'.format(val_date))
    return val_date


def get_glj(glj_date):
    y = str.strip(str(glj_date.year), '20')
    if glj_date.month < 4 and glj_date.month >= 1:
        # month = 1
        m = 'jan'
    elif glj_date.month < 7 and glj_date.month > 4:
        # month = 4
        m = 'apr'
    elif glj_date.month < 10 and glj_date.month > 7:
        # month = 7
        m = 'jul'
    elif glj_date.month == 12 and glj_date.month > 10:
        # month = 10
        m = 'oct'
    # else:
    #     exit()
    # month = 12
    # m = 'dec'
    d = m + y
    webbrowser.open_new_tab('https://www.gljpc.com/sites/default/files/pricing/{}.xlsx'.format(d))
    # webbrowser.open_new_tab('https://www.gljpc.com/historical-forecasts')
    # 'https://www.gljpc.com/sites/default/files/pricing/jul18.xlsx'


def get_sproule():
    webbrowser.open_new_tab('https://sproule.com/forecasts/archives')


def get_mcdaniel(mcdaniel_date):
    y = str.strip(str(mcdaniel_date.year), '20')
    if mcdaniel_date.month < 4 and mcdaniel_date.month >= 1:
        month = 1
        m = '01'
    elif mcdaniel_date.month < 7 and mcdaniel_date.month > 4:
        month = 4
        m = '04'
    elif mcdaniel_date.month < 10 and mcdaniel_date.month > 7:
        month = 7
        m = '07'
    elif mcdaniel_date.month == 12 and mcdaniel_date.month > 10:
        month = 10
        m = '10'
    d = y + m + '01'
    print(d)
    webbrowser.open_new_tab('https://www.mcdan.com/download/excel/{}'.format(d))
    # webbrowser.open_new_tab('https://www.mcdan.com/priceforecast')
    # webbrowser.open_new_tab('https://www.mcdan.com/download/excel/180701'


def get_eia():
    webbrowser.open_new_tab('https://www.eia.gov/outlooks/aeo/excel/hrnocpp/aeotab_12.xlsx')


def get_rea(rea_date):
    now = datetime.datetime.now()
    if rea_date.month == now.month:
        webbrowser.open_new_tab(
        'https://www2.deloitte.com/ca/en/pages/resource-evaluation-and-advisory/articles/deloitte-canadian-price-forecast.html')
    else:
        webbrowser.open_new_tab(
        'https://www2.deloitte.com/ca/en/pages/resource-evaluation-and-advisory/articles/price-forecast-archives.html')
    # current link 'https://www2.deloitte.com/content/dam/Deloitte/ca/Documents/REA/ca-en-Oil-Gas-REA-Price-Forecast-Jun2018.pdf'


def get_eiu():
    webbrowser.open_new_tab('data.eiu.com/default.aspx')
