def mse_tot(true, pred):
    """
    Returns total mean squared error based on true complexion distribution
    and predicted complexion distribution. 
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
    mse = (np.linalg.norm(t[['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']].iloc[0]-
              p[['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']].iloc[0]))**2/10
    mses = pd.Series(mse)
    index = 1
    for j in range(1,len(t)):
        mse = pd.Series((np.linalg.norm(t[['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']].iloc[index]-
                  p[['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']].iloc[index]))**2/10)
        mses = pd.concat([mses, mse])
        #print(mses)
        index += 1
    finalmse = sum(mses)/len(mses)
    return finalmse
