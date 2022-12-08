"""
Define confusion matrix function to assess fit based on maximum bin
"""

def conf_matrix(data):
    # TODO: add num_bins
    # if type of data isn't pandas dataframe: return ValueError
    # if data doesn't have the four requisite names - retrun ValueError
    df = data
    df_w = pd.pivot(df, index=['picid'], columns='bin')
    print(df_w.head())
    a = df_w.columns.get_level_values(0).astype(str)
    print(a)
    b = df_w.columns.get_level_values(1).astype(str)
    print(b)
    df_w.columns = [a,b]
    df_w.columns = df_w.columns.map('_'.join)
    print(df_w.head())
    df_w['max_true'] = df_w[['true_1', 'true_2', 'true_3', 
                         'true_4', 'true_5', 'true_6',
                         'true_7', 'true_8', 'true_9', 
                         'true_10']].idxmax(axis=1).str.removeprefix('true_')
    df_w['max_pred'] = df_w[['pred_1', 'pred_2', 'pred_3', 'pred_4', 
                       'pred_5', 'pred_6', 'pred_7', 'pred_8', 
                       'pred_9', 'pred_10']].idxmax(axis=1).str.removeprefix('pred_')
    cm1 = ConfusionMatrixDisplay(confusion_matrix(df_w['max_true'], df_w['max_pred']))
    return cm1
