from bayes_opt import BayesianOptimization
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier
import lightgbm as lgb
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import sys
import numpy as np

import warnings
warnings.filterwarnings("ignore")
xgb.set_config(verbosity=0)

# Functions for Bayesian Optimization:

###################################################################################################
# RANDOM FOREST's Bayesian Optmization Function
###################################################################################################


def random_forest_cv(n_estimators, min_samples_split, max_features, max_depth, data, targets):
    """Random Forest cross validation"""

    estimator = RandomForestClassifier(
        n_estimators=n_estimators,
        min_samples_split=min_samples_split,
        max_features=max_features,
        random_state=None,
        max_depth=max_depth)

    cval = cross_val_score(estimator, data, targets, scoring='f1_weighted', cv=5)

    return cval.mean()


def optimize_rfc(data, targets):
    """Apply Bayesian Optimization to Random Forest parameters."""

    def rfc_crossval(n_estimators, min_samples_split, max_features, max_depth):
        """Wrapper of RandomForest cross validation."""

        return random_forest_cv(
            n_estimators=int(n_estimators),
            min_samples_split=int(min_samples_split),
            max_features=int(max_features),
            max_depth=int(max_depth),
            data=data,
            targets=targets)

    optimizer = BayesianOptimization(
        f=rfc_crossval,
        pbounds={
            "n_estimators": (100, 200),
            "min_samples_split": (2, 10),
            "max_features": (1, 9),
            "max_depth": (1, 10)
        },
        random_state=None,
        verbose=2
    )
    optimizer.maximize(n_iter=50)

    return optimizer.max


###################################################################################################
# XGBoost Bayesian Optimization
###################################################################################################

def XGBoost_cv(n_estimators, max_depth, learning_rate, subsample, colsample_bytree, colsample_bylevel, colsample_bynode,
               data, targets):  #

    """XGBoost cross validation"""

    estimator = XGBClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        learning_rate=learning_rate,
        subsample=subsample,
        colsample_bytree=colsample_bytree,
        colsample_bylevel=colsample_bylevel,
        colsample_bynode=colsample_bynode,
        random_state=None, )

    cval = cross_val_score(estimator, data, targets, scoring='f1_weighted', cv=5)

    return cval.mean()


def optimize_XGB(data, targets):
    """Apply Bayesian Optimization to XGBoost classifier parameters."""

    def XGB_crossval(n_estimators, max_depth, learning_rate, subsample, colsample_bytree, colsample_bylevel,
                     colsample_bynode):

        """Wrapper of RandomForest cross validation."""
        return XGBoost_cv(
            n_estimators=int(n_estimators),
            max_depth=int(max_depth),
            learning_rate=max(min(learning_rate, 0.999), 1e-3),
            subsample=max(min(subsample, 0.999), 1e-3),
            colsample_bytree=max(min(colsample_bytree, 0.999), 1e-3),
            colsample_bylevel=max(min(colsample_bylevel, 0.999), 1e-3),
            colsample_bynode=max(min(colsample_bynode, 0.999), 1e-3),
            data=data,
            targets=targets)

    optimizer = BayesianOptimization(
        f=XGB_crossval,
        pbounds={
            "n_estimators": (100, 200),
            "max_depth": (1, 10),
            "learning_rate": (0.1, 0.999),
            "subsample": (0.5, 0.999),
            "colsample_bytree": (0.5, 0.999),
            "colsample_bylevel": (0.5, 0.999),
            "colsample_bynode": (0.5, 0.999),
        },
        random_state=None,
        verbose=2
    )
    optimizer.maximize(n_iter=50)

    return optimizer.max

###################################################################################################
# LGBM's Bayesian Optmization Function
###################################################################################################


def lgbm_cv(n_estimators, learning_rate, subsample, colsample_bytree, max_depth, data, targets):
    """Random Forest cross validation"""

    estimator = lgb.LGBMClassifier(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        subsample=subsample,
        colsample_bytree=colsample_bytree,
        random_state=None,
        max_depth=max_depth)

    cval = cross_val_score(estimator, data, targets, scoring='f1_weighted', cv=5)

    return cval.mean()


def optimize_lgbm(data, targets):
    """Apply Bayesian Optimization to Random Forest parameters."""

    def lgbm_crossval(n_estimators, learning_rate, subsample, colsample_bytree, max_depth):
        """Wrapper of RandomForest cross validation."""

        return lgbm_cv(
            n_estimators=int(n_estimators),
            learning_rate=max(min(learning_rate, 0.999), 1e-3),
            subsample=max(min(subsample, 0.999), 1e-3),
            colsample_bytree=max(min(colsample_bytree, 0.999), 1e-3),
            max_depth=int(max_depth),
            data=data,
            targets=targets)

    optimizer = BayesianOptimization(
        f=lgbm_crossval,
        pbounds={
            "n_estimators": (100, 200),
            "max_depth": (1, 10),
            "learning_rate": (0.1, 0.999),
            "subsample": (0.5, 0.999),
            "colsample_bytree": (0.5, 0.999)


        },
        random_state=None,
        verbose=2
    )
    optimizer.maximize(n_iter=50)

    return optimizer.max


###################################################################################################
# Data preparation
###################################################################################################

database = pd.read_csv('dataset/GDB_Bonin(2020)_update.csv')
database_preditores = database[['SiO2', 'TiO2', 'Al2O3', 'FeOt', 'MnO', 'MgO', 'CaO',
                                'K2O', 'Na2O']]
database_alvo = database[['Group']]

X_train, X_test, y_train, y_test = train_test_split(database_preditores, database_alvo, test_size=0.30,
                                                    stratify=database_alvo, random_state=42)

scaler = StandardScaler()
encoder = LabelEncoder()
X_train_scaled = scaler.fit_transform(X_train)
y_train_encoded = encoder.fit_transform(y_train)


###################################################################################################
# RANDOM FOREST's Bayesian Optmization
###################################################################################################

bo_random_forest = optimize_rfc(X_train_scaled, np.ravel(y_train_encoded))
params = bo_random_forest['params']
bo_rf = RandomForestClassifier(max_depth=params['max_depth'],
                                       max_features=params['max_features'],
                                       min_samples_split=int(params['min_samples_split']),
                                       n_estimators=int(params['n_estimators']))

###################################################################################################
# XGBoost Bayesian Optmization
###################################################################################################

bo_xboost = optimize_XGB(X_train_scaled, y_train_encoded)

# Parameters
params_xgb = bo_xboost['params']

# Model with best parameters
bo_xgb = XGBClassifier(colsample_bylevel=params_xgb['colsample_bylevel'],
                                colsample_bynode=params_xgb['colsample_bynode'],
                                colsample_bytree=params_xgb['colsample_bytree'],
                                learning_rate=params_xgb['learning_rate'],
                                max_depth=int(params_xgb['max_depth']),
                                n_estimators=int(params_xgb['n_estimators']),
                                subsample=params_xgb['subsample'])

###################################################################################################
# LGBM Bayesian Optmization
###################################################################################################

bo_lgbm = optimize_lgbm(X_train_scaled, y_train_encoded)

# Parameters
params_lgbm = bo_lgbm['params']

# Model with best parameters
bo_lgb = lgb.LGBMClassifier(colsample_bytree=params_lgbm['colsample_bytree'],
                                learning_rate=params_lgbm['learning_rate'],
                                max_depth=int(params_lgbm['max_depth']),
                                n_estimators=int(params_lgbm['n_estimators']),
                                subsample=params_lgbm['subsample'],)

###################################################################################################
# Saving Best models
###################################################################################################


sys.stdout = open('bo_rf.txt', 'w')
print(bo_rf)
sys.stdout.close()

sys.stdout = open('bo_xgb.txt', 'w')
print(bo_xgb)
sys.stdout.close()

sys.stdout = open('bo_lgbm.txt', 'w')
print(bo_lgb)
sys.stdout.close()
