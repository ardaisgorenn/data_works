import question_4
import pandas as pd

df = question_4.run(df_flag=True)


def find_median(df: pd.DataFrame) -> dict:
    """
    This function returns dictionary with countries as keys and median of their  daily_vaccinations
    """
    countries = df['country'].unique().tolist()
    data = {k: df[df['country'] == k]['daily_vaccinations'].median() for k in countries}
    return data


def sort_vals(d: dict) -> dict:
    """
    This function returns dictionary with sorted values of values with descending order
    """
    sorted_d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
    return sorted_d


def find_top_n(d: dict, n: int = 3) -> dict:
    """
    This function returns dictionary with top n values
    """
    top_d = {key: value for key, value in list(d.items())[0:n]}
    return top_d


def run():
    d = find_median(df)
    sorted_d = sort_vals(d)
    highest_d = find_top_n(sorted_d)
    for k, v in highest_d.items():
        print(f"{k} -> {v}")


if __name__ == '__main__':
    run()
