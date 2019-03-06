import field_maps as fm
import pandas as pd


def fix_delayed_wb(inf: str, outf:str):
    df = pd.read_csv(inf, header=0, index_col=None)
    df.to_csv(outf, index=False)


if __name__ == '__main__':
    fix_delayed_wb('./processed_data/rocket.csv',
                   './processed_data/rocket-fix.csv')
