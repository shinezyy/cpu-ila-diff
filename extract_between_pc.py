import extractors as xtr
import field_maps as fm
import trace_diff as td

start = 'e000f6fdc0'
end = 'e00113bae4'

df1 = xtr.extract_between_pc(
    (start, end), './data/boom-exit-ping.csv',
    fm.boom_field_map(),
    target_fields=[x for x in fm.boom_field_map().values()
                   if 'dontCare' not in x])

df1.to_csv("./processed_data/boom.csv")

df2 = xtr.extract_between_pc(
    (start, end), './data/rocket-ping-exit.csv',
    fm.rocket_field_map(),
    target_fields=[x for x in fm.rocket_field_map().values()
                   if 'dontCare' not in x])

df2.to_csv("./processed_data/rocket.csv")

# td.structured_diff(df1, df2)
