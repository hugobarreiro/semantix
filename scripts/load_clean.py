import pandas as pd
from zipfile import ZipFile


def load_clean():
    with ZipFile('data/bank.zip') as file:
        with file.open('bank-full.csv') as raw:
            bank = pd.read_csv(
                raw,
                sep=';',
                dtype=dict(
                    age='UInt8',
                    job='category',
                    marital='category',
                    education=pd.api.types.CategoricalDtype(
                        categories=["primary", "secondary", "tertiary"],
                        ordered=True
                    ),
                    default='bool',
                    balance='Int64',
                    housing='bool',
                    loan='bool',
                    contact='category',
                    day='UInt8',
                    month=pd.api.types.CategoricalDtype(
                        categories=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'],
                        ordered=True
                    ),
                    duration='UInt16',
                    campaign='UInt8',
                    previous='UInt16',
                    poutcome='category',
                    y='bool'
                ),
                true_values=['yes'],
                false_values=['no'],
                na_values=['unknown']
            )

    bank['pdays'] = bank['pdays'].replace(-1, pd.NA).astype('UInt16')

    bank.to_pickle('data/clean.pkl.gz', compression='gzip')


if __name__ == '__main__':
    load_clean()
