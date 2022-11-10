import requests
import csv
import pandas as pd

URL = 'https://raw.githubusercontent.com/tarikkranda/pi_datasets/main/country_vaccination_stats.csv'


def find_valid(df: pd.DataFrame, country: str) -> bool:
    """
    This function returns false if country does not have any valid vaccination number yet
    """
    if df[df['country'] == country]['daily_vaccinations'].count() > 1 and \
            df[df['country'] == country]['daily_vaccinations'].unique().tolist()[0] != '':
        return True
    return False


def find_min(df: pd.DataFrame, country: str) -> int:
    """
    This function returns minium number of vacines with given country
    """
    return df[(df['country'] == country) & (df['daily_vaccinations'] != -1)]['daily_vaccinations'].min()


def run(df_flag=False):
    lines = requests.get(URL).text.splitlines()
    reader = csv.reader(lines)

    data_list = []
    for row in reader:
        data_list.append(row)

    df = pd.DataFrame(data=data_list[1:], columns=data_list[0])
    df['daily_vaccinations'].replace(to_replace='', value='-1', inplace=True)
    df['daily_vaccinations'] = df['daily_vaccinations'].astype(int)
    df['daily_vaccinations'] = df.apply(
        lambda x: find_min(df, x['country']) if x['daily_vaccinations'] == -1 else x['daily_vaccinations'], axis=1)

    df['daily_vaccinations'] = df.apply(
        lambda x: 0 if find_valid(df, x['country']) == False else x['daily_vaccinations'],
        axis=1)
    if df_flag:
        return df
    else:
        print('Code execution is over!')


if __name__ == '__main__':
    run()
