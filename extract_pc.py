import extractors as xtr
import field_maps as fm


# df = xtr.extract('./data/boom-handle-exit.csv', fm.boom_field_map(), ['commPC'])
# df.to_csv('./processed_data/boom-pc.csv', sep=' ', header=None, index=False)

df = xtr.extract('./data/rocket-ping-exit.csv', fm.rocket_field_map(),
                 ['commPC'])
df.to_csv('./processed_data/rocket-pc.csv', sep=' ', header=None, index=False)
