import pandas as pd


def structured_diff(dfx: pd.DataFrame, dfy: pd.DataFrame):
    for (index, x), (_, y) in zip(dfx.iterrows(), dfy.iterrows()):
        if x.commPC != y.commPC:
            print(f'{index}: PC diff: {x.commPC}, {y.commPC}')

        if x.wbValueValid and y.wbValueValid:
            if x.wbValue != y.wbValue:
                if x.wbValue.startswith('ff'):
                    continue
                print(f'{index}: @PC:{x.commPC}, wb value diff: {x.wbValue}, '
                      f'{y.wbValue}')

