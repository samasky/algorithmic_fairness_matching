# Fair Training of ML Algorithms on Mortgage Lending Data via Causal Matching

This repository contains the code for the following paper:



## Steps to run the code

### 1. Download the data
Use the following code to download the HMDA data:
```bash
wget https://ffiec.cfpb.gov/data-browser/data/2020?category=nationwide&actions_taken=1,3&races=Black%20or%20African%20American,White
```
The data dictionary can be found [here](https://ffiec.cfpb.gov/documentation/2021/derived-data-fields/).

### 2. Preprocess the data
Use the `Preprocess.ipynb` notebook to preprocess the data and save the results in the pickle format.

### 3. Causal Matching
Run `matching.py` to perform causal matching. This script might take some time to run.

### 4. Extract Insights
Extract insights from the data using `Insights.ipynb` notebook.

### 5. Train ML Algorithms and Evaluate their Fairness
Use `Classification of Approval.ipynb` and `Regression on Interest Rate.ipynb` to train ML algorithms on the *mortgage approval* and *interest rate* prediction task. The notebooks generate the results in the paper.


## Contact
Please contact Sama Ghoba <sghoba@seattleu.edu> for questions about the paper and code.