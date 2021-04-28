import numpy as np
from numpy.core.fromnumeric import mean
def clean_raw_data(df):
    """ Takes a dataframe and performs four steps:
            - Selects columns for modeling
            - For numeric variables, replaces 0 values with mean for that region
            - Fills invalid construction_year values with the mean construction_year
            - Converts strings to categorical variables
            
        :param df: A raw dataframe that has been read into pandas
        :returns: A dataframe with the preprocessing performed.
    """
    useful_columns = ['amount_tsh', 'gps_height', 'longitude', 'latitude', 'region', 'population',
    'construction_year', 'extraction_type_class', 'management_group', 'quality_group', 'source_type',
    'waterpoint_type', 'status_group']
    df_input = df[useful_columns].copy()
    zero_is_bad_value = ['longitude', 'population']
    other_bad_value = ['latitude']
    # df_input = replace_value_with_grouped_mean(df_input)
    # df_input = replace_value_with_grouped_mean(df_input, np.nan, 'construction_mean')
    for col in useful_columns:
        if df_input[col].dtype == 'object':
            df_input[col] = df_input[col].astype("category")
            # print('change col {} format'.format(col))
        if col == 'construction_year':
            invalid_rows = df_input[col] <=1000
            valid_mean = df_input.loc[(~invalid_rows) ,col].mean()
            df_input.loc[invalid_rows, col] = valid_mean
            # print('change all construction year less than 1000 to mean')
        if col in zero_is_bad_value:
            df_input = replace_value_with_grouped_mean(df_input, 0, col, 'region')
            print("Change col {} from 0 to mean".format(col))
        if col in other_bad_value:
            df_input = replace_value_with_grouped_mean(df_input, -2e-8, col, 'region')
            print("Change col {} from -2e-8 to mean".format(col))

    return df_input
    
def replace_value_with_grouped_mean(df, value, column, to_groupby):
    """ For a given numeric value (e.g., 0) in a particular column, take the
        mean of column (excluding value) grouped by to_groupby and return that
        column with the value replaced by that mean.

        :param df: The dataframe to operate on.
        :param value: The value in column that should be replaced.
        :param column: The column in which replacements need to be made.
        :param to_groupby: Groupby this variable and take the mean of column.
                           Replace value with the group's mean.
        :returns: The data frame with the invalid values replaced
    """
    df_input = df.copy()
    invalid_rows = (df_input[column].eq(value))
    print(invalid_rows.eq(True).sum())

    # Calculate mean for each region
    group_mean = (df_input[~invalid_rows]
    .groupby(to_groupby)[column]
    .mean())

    print(group_mean)

    # Populate region mean for every rows in dataframe
    mean_values = group_mean[df_input[to_groupby].values].fillna(0)
    print(np.isnan(mean_values).sum())

    # put values in invalid rows
    df_input.loc[invalid_rows, column] = mean_values[invalid_rows]

    return df_input
