"""Using the datasets, finds a non-hispanic white match for each african-american applicant."""
import pandas as pd
import numpy as np
from tqdm import tqdm

data_b = pd.read_pickle(r'data_b.pkl')
data_w = pd.read_pickle(r'data_w.pkl')
print('Data loaded')

## Loan to Value Ratio
data_b['loan_to_value_ratio']= pd.to_numeric(data_b['loan_to_value_ratio'],errors= 'coerce')
data_w['loan_to_value_ratio']= pd.to_numeric(data_w['loan_to_value_ratio'],errors= 'coerce') 
bins=np.array([40, 60, 79, 81, 90, 100])
data_b['LV'] = np.digitize(data_b['loan_to_value_ratio'],bins)
data_b.loc[pd.isna(data_b['loan_to_value_ratio']), 'LV']=8
data_w['LV'] = np.digitize(data_w['loan_to_value_ratio'],bins)
data_w.loc[pd.isna(data_w['loan_to_value_ratio']), 'LV']=8  

## Debt to Income Ratio
data_w.loc[data_w['debt_to_income_ratio']=='<20%','debt_to_income_ratio']=15
data_w.loc[data_w['debt_to_income_ratio']=='20%-<30%','debt_to_income_ratio']=25
data_w.loc[data_w['debt_to_income_ratio']=='30%-<36%','debt_to_income_ratio']=33
data_w.loc[data_w['debt_to_income_ratio']=='50%-60%','debt_to_income_ratio']=55
data_w.loc[data_w['debt_to_income_ratio']=='>60%','debt_to_income_ratio']=65
data_w.loc[data_w['debt_to_income_ratio']=='Exempt','debt_to_income_ratio']=-1
data_w['debt_to_income_ratio'] = pd.to_numeric(data_w['debt_to_income_ratio'])

data_b.loc[data_b['debt_to_income_ratio']=='<20%','debt_to_income_ratio']=15
data_b.loc[data_b['debt_to_income_ratio']=='20%-<30%','debt_to_income_ratio']=25
data_b.loc[data_b['debt_to_income_ratio']=='30%-<36%','debt_to_income_ratio']=33
data_b.loc[data_b['debt_to_income_ratio']=='50%-60%','debt_to_income_ratio']=55
data_b.loc[data_b['debt_to_income_ratio']=='>60%','debt_to_income_ratio']=65
data_b.loc[data_b['debt_to_income_ratio']=='Exempt','debt_to_income_ratio']=-1
data_b['debt_to_income_ratio'] = pd.to_numeric(data_b['debt_to_income_ratio'])

bins=np.array([0, 20, 30, 36, 40, 45, 50, 60])
data_b['DI'] = np.digitize(data_b['debt_to_income_ratio'],bins)
data_b.loc[pd.isna(data_b['debt_to_income_ratio']), 'DI']=9
data_w['DI'] = np.digitize(data_w['debt_to_income_ratio'],bins)
data_w.loc[pd.isna(data_w['debt_to_income_ratio']), 'DI']=9

## Income
bins=np.array([32,53,107,374])
data_b['income_brackets'] = np.digitize(data_b['income'],bins)
data_b.loc[pd.isna(data_b['income']), 'income_brackets']=5
data_w['income_brackets'] = np.digitize(data_w['income'],bins)
data_w.loc[pd.isna(data_w['income']), 'income_brackets']=5

match_list = []
for index, row in tqdm(data_b.iterrows(),total=data_b.shape[0]):
    income = row['income_brackets']
    sex = row['applicant_sex']
    state = row['state_code']
    age = row['applicant_age']
    lien = row['lien_status']
    lvr = row['LV']
    di = row['DI']
    ltype = row['loan_type']
    mws=data_w[(data_w['applicant_sex']==sex)&(data_w['state_code']==state)&
        (data_w['income_brackets']==income)&(data_w['applicant_age']==age)&
        (data_w['lien_status']==lien) & (data_w['LV']==lvr) 
        & (data_w['DI']==di) & (data_w['loan_type']==ltype)]
    if mws.shape[0]>0:
        match_list.extend([row,mws.sample().iloc[0]])

matched = pd.DataFrame(match_list)
matched.to_csv(r'matched.csv')
