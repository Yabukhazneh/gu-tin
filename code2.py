   # Read the input Excel file
    xls = pd.ExcelFile(file_path)
    
    # Read the two sheets into separate DataFrames
    df1 = pd.read_excel(xls, sheet_name=sheet_name1)
    df2 = pd.read_excel(xls, sheet_name=sheet_name2)
    
    # Perform the reconciliation by comparing the two DataFrames
    merged = df1.merge(df2, on='ID', how='outer', suffixes=('_1', '_2'), indicator=True)
    differences = merged[merged['_merge'] != 'both']
    
    # Identify differences within each row
    row_diff_df = differences.drop('_merge', axis=1).set_index('ID')
    row_diff_df = row_diff_df.groupby(row_diff_df.columns, axis=1).apply(lambda x: x.dropna(how='all')).stack().unstack()
    row_diff_df = row_diff_df.rename(columns=lambda c: c.split('_')[0])
    row_diff_df = row_diff_df.reset_index().rename(columns={'level_1': 'Column'})
    
    # Create a new Excel file with the differences
    with pd.ExcelWriter(output_file) as writer:
        differences.to_excel(writer, sheet_name='Differences', index=False)
        df1.to_excel(writer, sheet_name=sheet_name1, index=False)
        df2.to_excel(writer, sheet_name=sheet_name2, index=False)
        row_diff_df.to_excel(writer, sheet_name='Row Differences', index=False)

# Example usage
file_path = 'input.xlsx'
sheet_name1 = 'Sheet1'
sheet_name2 = 'Sheet2'
output_file = 'reconciliation_output.xlsx'

reconcile_sheets(file_path, sheet_name1, sheet_name2, output_file)
