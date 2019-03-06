import pandas as pd
import field_maps as fm


def extract(f: str, field_map: dict, target_fields: [str] = None):
    df = pd.read_csv(f, sep=',', header=0, index_col=None)
    df.rename(columns=field_map, inplace=True)
    valids = df['valid'] == True

    if not target_fields is None:
        df = df[valids][target_fields]
    else:
        df = df[valids]
    return df


def extract_between_pc(
        pc_range: (str, str), f: str, field_map: dict,
        target_fields: [str] = None):

    if not target_fields is None:
        assert 'commPC' in target_fields

    df = extract(f, field_map, target_fields).reset_index()
    df = df.drop(['index'], axis=1)
    start, end = pc_range
    start_label = df[df['commPC'] == start].index[0]
    end_label = df[df['commPC'] == end].index[0] # 0: choose the first hit
    end_label = min(end_label + 100, len(df))
    return df.loc[start_label: end_label]


if __name__ == '__main__':
    dfx = extract('./data/boom-bug.csv', fm.boom_field_map(), ['commPC'])
    print(dfx)
