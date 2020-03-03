#! -*- coding: utf-8 -*-

from src import *
from sklearn import linear_model

# step1: read the data
df = pd.read_csv('data/EngineRelevance.csv', index_col=0, dtype={'id_mdsum': str})
df.fillna(0, inplace=True)
df = df.dropna(axis=0,how='any')

# step2: method 
X_title = ['hit_term_count','qhit_term_ratio','qhit_term_weight','qhit_term_weight2',
       'qhit_term_weight_core','dhit_term_ratio','dhit_term_weight',
       'dhit_term_weight2','dhit_term_weight_core','jaccard',
       'jaccard_qweight','jaccard_dweight','tfidf','tfidf_norm',
       'bm25','bm25_norm']
Y_title = ['label2']
X = df[X_title] 
Y = df[Y_title]

model = linear_model.LinearRegression(fit_intercept=False)
model.fit(X, Y)
# display(model.intercept_)  
# display(model.coef_)  
# display(model.score(X,Y))
coef_linear = model.coef_[0]
print("[least square (LS)], the coefficients are:")
print("    %s\n"%coef_linear)
df['LS']=model.predict(X)

model.coef_ = (model.coef_[0] + abs(model.coef_[0]))/2
coef_linear = model.coef_
print("[non-negative least square (NLS)], the coefficients are:")
print("    %s\n"%coef_linear)
df['NLS']=model.predict(X)

coef_linear = non_negetive(X,Y)
model.coef_ = coef_linear
print("[non-negative linear regression (NNLR)], the coefficients are:")
print("    %s\n"%coef_linear)
df['NNLR']=model.predict(X)

coef_linear = gradient_truncation(X,Y)
model.coef_ = coef_linear
print("[gradient truncation (GT)], the coefficients are:")
print("    %s\n"%coef_linear)
df['GT']=model.predict(X)

# step3: metric comparison
from sklearn import metrics
from sklearn.metrics import auc
seqnum_columns = ['LS','NLS','NNLR','GT']
y_label = "label2"
label_list = list(df[y_label])
rmse_list  = []
for item in seqnum_columns:
    tmp_list = list(df[item])
    rmse_list.append(RMSE(label_list,tmp_list))
metric_df = new_metric(df,seqnum_columns,y_label)
metric_df['rmse'] = rmse_list
print(metric_df)
