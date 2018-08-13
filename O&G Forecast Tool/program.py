import webpage_download


def main():
    print_header()
    cmd = user_command()
    user_date = webpage_download.get_valdate_from_user()
    webpage_select(cmd, user_date)


def print_header():
    print('------------------------------------')
    print('       O&G PRICE FORECASTS          ')
    print('------------------------------------')
    print()


def user_command():
    cmd = input('''From what sources do you want to download forecast data?
    a = All sources
    r = REA Deloitte (updated quarterly)
    s = Sproule (updated monthly)
    m = McDaniel (updated quarterly)
    e = eia (updated annually)
    u = eiu (updated monthly - requires package selection)
    g = GLJ (updated quarterly)
    ''')
    return cmd


def webpage_select(cmd, user_date):
    if cmd == 'a':
        webpage_download.get_rea(user_date)
        webpage_download.get_sproule()
        webpage_download.get_mcdaniel(user_date)
        webpage_download.get_eia()
        webpage_download.get_eiu()
        webpage_download.get_glj(user_date)
    elif cmd == 'r':
        webpage_download.get_rea(user_date)
    elif cmd == 's':
        webpage_download.get_sproule()
    elif cmd == 'm':
        webpage_download.get_mcdaniel(user_date)
    elif cmd == 'e':
        webpage_download.get_eia()
    elif cmd == 'u':
        webpage_download.get_eiu()
    elif cmd == 'g':
        webpage_download.get_glj(user_date)
    else:
        print('Invalid command!')


if __name__ == '__main__': main()
