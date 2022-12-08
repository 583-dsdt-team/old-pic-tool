import pandas as pd
import numpy as np

def mse(true, pred, bybin):
    """
    Returns a pandas dataframe with ten mean square error results,
    one for each complexion bin.
    It takes three arguments: 
    First, true and pred, which are both pandas dataframes including these 
    columns: "picid" which is a unique identifier of each image (and can 
    be used to link across dataframes) and ten columns numbered from 0 to 9 
    which index the bins.
    bybin is a boolean; when True the function returns a MSE value for each
    color bin; when False the function returns returns a single MSE for the
    entire set of bins.
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
    if bybin==True:
        true['mse0'] = (true['0']-pred['0'])**2
        true['mse1'] = (true['1']-pred['1'])**2
        true['mse2'] = (true['2']-pred['2'])**2
        true['mse3'] = (true['3']-pred['3'])**2
        true['mse4'] = (true['4']-pred['4'])**2
        true['mse5'] = (true['5']-pred['5'])**2
        true['mse6'] = (true['6']-pred['6'])**2
        true['mse7'] = (true['7']-pred['7'])**2
        true['mse8'] = (true['8']-pred['8'])**2
        true['mse9'] = (true['9']-pred['9'])**2
        mses = pd.DataFrame({
            'complexbin' : [0,1,2,3,4,5,6,7,8,9],
            'mse' : [sum(true['mse0'])/len(true['mse0']), 
                sum(true['mse1'])/len(true['mse1']),
                sum(true['mse2'])/len(true['mse2']),
                sum(true['mse3'])/len(true['mse3']),
                sum(true['mse4'])/len(true['mse4']),
                sum(true['mse5'])/len(true['mse5']),
                sum(true['mse6'])/len(true['mse6']),
                sum(true['mse7'])/len(true['mse7']),
                sum(true['mse8'])/len(true['mse8']),
                sum(true['mse9'])/len(true['mse9'])]
        })
        return mses
    if bybin==False:
        mse = (np.linalg.norm(true[['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']].iloc[0]-
              pred[['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']].iloc[0]))**2/10
        mses = pd.Series(mse)
        index = 1
        for j in range(1,len(true)):
            mse = pd.Series((np.linalg.norm(true[['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']].iloc[index]-
                      pred[['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']].iloc[index]))**2/10)
            mses = pd.concat([mses, mse])
            #print(mses)
            index += 1
        finalmse = sum(mses)/len(mses)
        return finalmse
