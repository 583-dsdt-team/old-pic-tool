def mse_by_bin(true, pred):
    """
    Returns a pandas dataframe with ten mean square error results,
    one for each complexion bin. 
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
    t['mse0'] = (t['0']-p['0'])**2
    t['mse1'] = (t['1']-p['1'])**2
    t['mse2'] = (t['2']-p['2'])**2
    t['mse3'] = (t['3']-p['3'])**2
    t['mse4'] = (t['4']-p['4'])**2
    t['mse5'] = (t['5']-p['5'])**2
    t['mse6'] = (t['6']-p['6'])**2
    t['mse7'] = (t['7']-p['7'])**2
    t['mse8'] = (t['8']-p['8'])**2
    t['mse9'] = (t['9']-p['9'])**2
    mses = pd.DataFrame({
        'complexbin' : [0,1,2,3,4,5,6,7,8,9],
        'mse' : [sum(t['mse0'])/len(t['mse0']), 
            sum(t['mse1'])/len(t['mse1']),
            sum(t['mse2'])/len(t['mse2']),
            sum(t['mse3'])/len(t['mse3']),
            sum(t['mse4'])/len(t['mse4']),
            sum(t['mse5'])/len(t['mse5']),
            sum(t['mse6'])/len(t['mse6']),
            sum(t['mse7'])/len(t['mse7']),
            sum(t['mse8'])/len(t['mse8']),
            sum(t['mse9'])/len(t['mse9'])]
    })
    return mses
