"""
Define confusion matrix function to assess fit based on maximum bin
"""

def conf_matrix(true, pred):
    """
    This function creates a confusion matrix comparing the true
    "primary color bin" (the bin representing the highest percentage of the photo)
    to the primary color bin predicted by the method in question.
    It takes two arguments: true and pred, which are both pandas
    dataframes including these columns: "picid" which is a unique 
    identifier of each image (and can be used to link across dataframes)
    and ten columns numbered from 0 to 9 which index the bins.
    """
    pred = pred.reset_index(drop=True)
    true = true.reset_index(drop=True)
    # check if true and pred are the correct type
    if not type(true) == pd.core.frame.DataFrame:
        raise ValueError("true needs to be a pandas dataframe")
    if not type(pred) == pd.core.frame.DataFrame:
        raise ValueError("pred needs to be a pandas dataframe")
    # check if true and pred contain the right variables
    reqvars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'picid']
    for v in reqvars:
        if v not in true.columns:
            raise ValueError("true needs column named " + v)
        if v not in pred.columns:
            raise ValueError("pred needs column named " + v)    
    # check that picid is a unique identifier
    if not true.nunique()['picid']==len(true):
        raise ValueError("picid does not uniquely identify obs in true")
    if not pred.nunique()['picid']==len(pred):
        raise ValueError("picid does not uniquely identify obs in pred")
    # check that all picids in true are in pred and vice versa
    for i in range(0,len(pred)):
        if pred['picid'][i] not in true.picid.values:
            raise ValueError('all picids in pred need to be in true')
    for i in range(0,len(true)):
        if true['picid'][i] not in pred.picid.values:
            raise ValueError('all picids in true need to be in pred')
    # check that columns 0 through 9 are numeric
    ## TODO
    true['max_true'] = true[['0', '1', '2', '3', '4', '5', '6', 
                             '7', '8', '9']].idxmax(axis=1)
    pred['max_pred'] = pred[['0', '1', '2', '3', '4', '5', '6', 
                             '7', '8', '9']].idxmax(axis=1)
    tp = true[['picid', 'max_true']].merge(pred[['picid', 'max_pred']], on='picid')
    unique = np.unique(tp[['max_true', 'max_pred']].values)
    unique.sort()
    cm = ConfusionMatrixDisplay(confusion_matrix(tp['max_true'], tp['max_pred']),
                          display_labels=unique)
    return cm
    