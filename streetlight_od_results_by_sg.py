import os
import pandas as pd
import sqlalchemy
from sqlalchemy import text

pd.set_option('future.no_silent_downcasting', True)
pd.set_option('display.max_columns', None)

def create_db_engine():
    dialect = 'postgresql'
    driver = 'psycopg2'
    db_name = 'postgres'
    db_user = 'da_analytics'
    db_password = os.environ['db_password'] # Use env variable
    db_host = '10.98.4.86'
    db_port = '5432'

    conn_string = f'{dialect}+{driver}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    eng = sqlalchemy.create_engine(conn_string)

    return eng

def load_data(eng):
    with eng.connect() as connection:
        data = connection.execute(text('select * from us50.stl_od_signalgroup_maltest order by random() limit 10000'))
        df = pd.DataFrame(data)

    return df

def column_to_string(df, column_name, element, new_column):
    df[new_column] = df[column_name].str.split('_').str[element]

def get_origin(df):
    column_to_string(df, 'o_name', 3, 'origin_name')
    column_to_string(df, 'o_name', 4, 'o_direction')
    df['origin'] = df['origin_name'] + '_' + df['o_direction']
    return

def get_destination(df):
    column_to_string(df, 'd_name', 3, 'destination_name')
    column_to_string(df, 'd_name', 4, 'd_direction')
    df['destination'] = df['destination_name'] + '_' + df['d_direction']
    return

def reshape_array(df):
    df_grouped = df.groupby(['data_period', 'daytype', 'daypart'])

    df_keys = df_grouped.groups.keys()

    for df_key in df_keys:
        df_key_list = list(df_key)

        data_period = df_key_list[0]
        daytype = df_key_list[1]
        daypart = df_key_list[2]

        print(data_period, daytype, daypart)

        group = df_grouped.get_group(df_key)

        group_tuple = [tuple(r) for r in group[['origin', 'destination', 'stl_volume']].to_numpy()]

        df_group = pd.DataFrame(group_tuple, columns=['origin', 'destination', 'stl_volume'])

        od_matrix = df_group.pivot_table(
            index='origin',
            columns='destination',
            values='stl_volume',
            fill_value=0  # fill missing pairs with zero
        )

        # print(od_matrix)


def main():
    eng = create_db_engine()
    df = load_data(eng)
    get_origin(df)
    get_destination(df)
    reshape_array(df)


if __name__ == '__main__':
    main()

# TODO: test appears in github
