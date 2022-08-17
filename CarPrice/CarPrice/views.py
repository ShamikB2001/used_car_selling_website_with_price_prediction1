
from django.shortcuts import render;
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.linear_model import Lasso
from sklearn import metrics
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline


def home(request):
    return render(request, "home.html")


def predict(request):
    return render(request, "predict.html")


def result(request):
    car = pd.read_csv(r'C:\Users\SHAMIK BANERJEE\OneDrive\Desktop\Django\CarPrice\Dataset\Model.csv')
    df = car.dropna()
    #df=df.drop(columns=["Car_Model_Name"])
    #T = df.drop(columns=["selling_price"])
    #J = df["selling_price"]
    #from sklearn.model_selection import train_test_split
   # T_train, T_test, J_train, J_test = train_test_split(T, J, test_size=0.2)
    #ohe = OneHotEncoder()
    #ohe.fit(T[['owner_type', 'seller_type', 'fuel_type', 'transmission_type']])
    #column_trans = make_column_transformer((OneHotEncoder(categories=ohe.categories_),
                                           # ['owner_type', 'seller_type', 'fuel_type',
                                             #'transmission_type']),
                                          # remainder='passthrough')

    T = df.drop(columns=["selling_price"])
    J = df["selling_price"]
    from sklearn.model_selection import train_test_split
    T_train, T_test, J_train, J_test = train_test_split(T, J, test_size=0.2)
    lr = LinearRegression()
    #pipe = make_pipeline(column_trans, lr)
    lr.fit(T_train, J_train)

    #var1 = int(request.GET['n1'])
    var2 = int(request.GET['n2'])
    var3 = int(request.GET['n3'])
    var4 = int(request.GET['n4'])
    var5 = int(request.GET['n5'])
    var6 = int(request.GET['n6'])
    var7 = float(request.GET['n7'])
    var8 = int(request.GET['n8'])
    var9 = float(request.GET['n9'])
    var10 = int(request.GET['n10'])
    var11 = int(request.GET['n11'])


    pred = lr.predict([[var2, var3,var4, var5, var6, var7, var8, var9, var10, var11]])

    pred=round(pred[0],2)
    price = "The predicted price is "+str(pred)+" Lakh"
    return render(request, "predict.html", {"result2": price})
 