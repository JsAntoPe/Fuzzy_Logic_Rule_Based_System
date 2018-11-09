from RuleBasedSystem import fuzzyfunctions as fuzzy
from time import time

DictMarketValue = {
    'Low': [0, 0, 80, 100],
    'Medium': [50, 100, 210, 250],
    'High': [200, 300, 650, 850],
    'Very High': [650, 850, 1000, 1000]
}

fuzzy.two_dim_plot(DictMarketValue, 'Market fuzzy graph')

DictLocation = {
    'Bad': [0, 0, 1.7, 4],
    'Fair': [2.5, 5, 6, 8.5],
    'Excellent': [6, 8.3, 10, 10]
}

fuzzy.two_dim_plot(DictLocation,  'Location fuzzy graph')

DictHouse = {
    'Very Low': [0, 0, 3],
    'Low': [0, 3, 6],
    'Medium': [2, 5, 8],
    'High': [4, 7, 10],
    'Very High': [7, 10, 10]
}

fuzzy.two_dim_plot(DictHouse, 'House fuzzy graph')

firstMatrix = [
    ['Low', 0, 0, 'Low'],
    [0, 'Bad', 0, 'Low'],
    ['Low', 'Bad', 1, 'Very Low'],
    ['Medium', 'Bad', 1, 'Low'],
    ['High', 'Bad', 1, 'Medium'],
    ['Very High', 'Bad', 1, 'High'],
    ['Low', 'Fair', 1, 'Low'],
    ['Medium', 'Fair', 1, 'Medium'],
    ['High', 'Fair', 1, 'High'],
    ['Very High', 'Fair', 1, 'Very High'],
    ['Low', 'Excellent', 1, 'Medium'],
    ['Medium', 'Excellent', 1, 'High'],
    ['High', 'Excellent', 1, 'Very High'],
    ['Very High', 'Excellent', 1, 'Very High']
]

DictAssets = {
    'Low': [0, 0, 150],
    'Medium': [60, 250, 480, 650],
    'High': [500, 700, 1000, 1000]
}

fuzzy.two_dim_plot(DictAssets, 'Assets fuzzy graph')

DictIncome = {
    'Low': [0, 0, 13, 25],
    'Medium': [15, 35, 55],
    'High': [40, 60, 80],
    'Very High': [60, 80, 100, 100]
}

fuzzy.two_dim_plot(DictIncome, 'Income fuzzy graph')

DictApplicant = {
    'Low': [0, 0, 2, 4],
    'Medium': [2, 5, 8],
    'High': [6, 8, 10, 10]
}

fuzzy.two_dim_plot(DictApplicant, 'Applicant fuzzy graph')

secondMatrix = [
    ['Low', 'Low', 1, 'Low'],
    ['Low', 'Medium', 1, 'Low'],
    ['Low', 'High', 1, 'Medium'],
    ['Low', 'Very High', 1, 'High'],
    ['Medium', 'Low', 1, 'Low'],
    ['Medium', 'Medium', 1, 'Medium'],
    ['Medium', 'High', 1, 'High'],
    ['Medium', 'Very High', 1, 'High'],
    ['High', 'Low', 1, 'Medium'],
    ['High', 'Medium', 1, 'Medium'],
    ['High', 'High', 1, 'High'],
    ['High', 'Very High', 1, 'High'],
]

DictInterest = {
    'Low': [0, 0, 2, 5],
    'Medium': [2, 4, 6, 8],
    'High': [6, 8.5, 10, 10]
}

fuzzy.two_dim_plot(DictInterest, 'Interest fuzzy graph')

DictCredit = {
    'Very Low': [0, 0, 125],
    'Low': [0, 125, 250],
    'Medium': [125, 250, 375],
    'High': [250, 375, 500],
    'Very High': [375, 500, 500]
}

fuzzy.two_dim_plot(DictCredit, 'Credit fuzzy graph')

thirdMatrix = [
    ['Low', 'Medium', 0, 0, 1, 'Very Low'],
    ['Low', 'High', 0, 0, 1, 'Very Low'],
    ['Medium', 'High', 0, 0, 1, 'Low'],
    [0, 0, 'Low', 0, 1, 'Very Low'],
    [0, 0, 0, 'Very Low', 1, 'Very Low'],
    [0, 0, 'Medium', 'Very Low', 1, 'Low'],
    [0, 0, 'Medium', 'Low', 1, 'Low'],
    [0, 0, 'Medium', 'Medium', 1, 'Medium'],
    [0, 0, 'Medium', 'High', 1, 'High'],
    [0, 0, 'Medium', 'Very High', 1, 'High'],
    [0, 0, 'High', 'Very Low', 1, 'Low'],
    [0, 0, 'High', 'Low', 1, 'Medium'],
    [0, 0, 'High', 'Medium', 1, 'High'],
    [0, 0, 'High', 'High', 1, 'High'],
    [0, 0, 'High', 'Very High', 1, 'Very High']
]
initialtime = time()
fuzzy.three_dim_plot(firstMatrix,
                     [DictMarketValue, DictLocation],
                     [True, True],
                     DictHouse,
                     'House Clipping Mandani Graph',
                     fuzzy.centerofgravityfunction_clipping_mandani)
fuzzy.three_dim_plot(secondMatrix,
                     [DictAssets, DictIncome],
                     [True, True],
                     DictApplicant,
                     'Applicant Clipping Mandani Graph',
                     fuzzy.centerofgravityfunction_clipping_mandani)
fuzzy.three_dim_plot(thirdMatrix,
                     [DictIncome, DictInterest, DictApplicant, DictHouse],
                     [False, False, True, True],
                     DictCredit,
                     'Credit Applicant x House Clipping Graph',
                     fuzzy.centerofgravityfunction_clipping_mandani)
fuzzy.three_dim_plot(thirdMatrix,
                     [DictIncome, DictInterest, DictApplicant, DictHouse],
                     [False, True, True, False],
                     DictCredit,
                     'Credit Applicant x Interest Clipping Mandani Graph',
                     fuzzy.centerofgravityfunction_clipping_mandani)
endingtime = time()
print('Time for clipping mandani: ', endingtime - initialtime)
# SugenoSet
initialtime = time()
fuzzy.three_dim_plot(firstMatrix,
                     [DictMarketValue, DictLocation],
                     [True, True],
                     DictHouse,
                     'House Sugeno Graph',
                     fuzzy.centerofgravityfunction_sugeno)
fuzzy.three_dim_plot(secondMatrix,
                     [DictAssets, DictIncome],
                     [True, True],
                     DictApplicant,
                     'Applicant Sugeno Graph',
                     fuzzy.centerofgravityfunction_sugeno)
fuzzy.three_dim_plot(thirdMatrix,
                     [DictIncome, DictInterest, DictApplicant, DictHouse],
                     [False, False, True, True],
                     DictCredit,
                     'Credit Applicant x House Sugeno Graph',
                     fuzzy.centerofgravityfunction_sugeno)
fuzzy.three_dim_plot(thirdMatrix,
                     [DictIncome, DictInterest, DictApplicant, DictHouse],
                     [False, True, True, False],
                     DictCredit,
                     'Credit Applicant x Interest Sugeno Graph',
                     fuzzy.centerofgravityfunction_sugeno)
endingtime = time()
print('Time for sugeno: ', endingtime - initialtime)
#Scaled
initialtime = time()
fuzzy.three_dim_plot(firstMatrix,
                     [DictMarketValue, DictLocation],
                     [True, True],
                     DictHouse,
                     'House Scaling Graph',
                     fuzzy.centerofgravityfunction_scaled_mandani)
fuzzy.three_dim_plot(secondMatrix,
                     [DictAssets, DictIncome],
                     [True, True],
                     DictApplicant,
                     'Applicant Scaling Graph',
                     fuzzy.centerofgravityfunction_scaled_mandani)
fuzzy.three_dim_plot(thirdMatrix,
                     [DictIncome, DictInterest, DictApplicant, DictHouse],
                     [False, False, True, True],
                     DictCredit,
                     'Credit Applicant x House Scaling Graph',
                     fuzzy.centerofgravityfunction_scaled_mandani)
fuzzy.three_dim_plot(thirdMatrix,
                     [DictIncome, DictInterest, DictApplicant, DictHouse],
                     [False, True, True, False],
                     DictCredit,
                     'Credit Applicant x Interest Scaling Graph',
                     fuzzy.centerofgravityfunction_scaled_mandani)
endingtime = time()
print('Time for scaling mandani: ', endingtime - initialtime)
