# Function to rank top 10 correlations
def rank_correlations(corr_matrix):
    # flattening matrix
    flattened_matrix = corr_matrix.stack().reset_index()
    #renaming columns
    flattened_matrix.columns = ['Variable_1', 'Variable_2', 'Correlation']
    # removing duplicate variable names
    flattened_matrix = flattened_matrix.loc[flattened_matrix['Variable_1'] != flattened_matrix['Variable_2']]
    corr_column = flattened_matrix['Correlation']
    flattened_matrix = flattened_matrix.iloc[abs(corr_column).argsort()[::-1]]
    flattened_matrix = flattened_matrix.loc[flattened_matrix['Correlation'].duplicated()]
    #print(f'Top 10 Variable Correlations: \n{flattened_matrix.head(10)}')
    return flattened_matrix.head(10)