# Non-negative-linear-regression
## the definition of data
  For the input query and returned document pairs (we denote (q,d)), we calculated 14 physically relevant correlation values. The larger the value of each of the 14 features, the higher the correlation of (query, document) pair, that is, the dependent variable("label2" in data/EngineRelevance.csv) have positive correlation with all independent variables. Therefore, this question is Non-Negative Linear Regression Problems.

independent variables name is: 

    qhit_term_count:    hits number for recall documentn in recall query
    
    qhit_term_ratio:    hits ratio for recall document segmentation in query

    qhit_term_weight:   hits weight for recall document segmentation in query

    qhit_term_weight2:  hits weight for recall document segmentation in query

    qhit_term_weight_core: hits weight for core recall document segmentation in query

    dhit_term_ratio:    hits ratio for query segmentation in document

    dhit_term_weight:   hits weight for query segmentation in document
    
    dhit_term_weight2:  hits weight for query segmentation in document
    
    dhit_term_weight_core: hits weight for core query document segmentation in document
    
    jaccard: jaccard similarity between query and document
    
    jaccard_qweight: similarity between query and document using query segmentation weight
    
    jaccard_dweight: similarity between query and document using document segmentation weight

    tfidf: tfidf value for query and dicument
    
    tfidf_norm: normalized tfidf value for query and dicument
    
    bm25： bm25 value between query and dicument
    
    bm25_norm: normalized tfidf value between query and dicument

dependent variables name is: 
    
    label2: whether relevant or not?
    
In the search sorting scene, in order to facilitate comparison, we chose AUC and RMSE for comparison.

By running the code "Non_negative_regression_demo.py". The readers will get the following results.
      
     [least square (LS)], the coefficients are:
       [ 0.01245128 -0.40390261 -0.0191926  -0.52963571  0.20836933  0.21884406
       -0.05320568 -0.02270426  0.11965694 -0.57252524  0.48290015  0.00831857
       -0.00658889 -0.20222227  0.020237    1.11454091]

     [non-negative least square (NLS)], the coefficients are:
        [0.01245128 0.         0.         0.         0.20836933 0.21884406
         0.         0.         0.11965694 0.         0.48290015 0.00831857
         0.         0.         0.020237   1.11454091]

     [non-negative linear regression (NNLR)], the coefficients are:
        [0.00090505 0.05289951 0.09156436 0.05211574 0.10416422 0.00429807
         0.00641059 0.00409428 0.00968512 0.00114789 0.07732478 0.00118315
         0.0019383  0.06258468 0.0103732  0.13788792]

     [gradient truncation (GT)], the coefficients are:
        [0.04793231 0.08881607 0.08788822 0.08778685 0.08748704 0.09209439
         0.09177271 0.09185865 0.09140391 0.09384025 0.08980766 0.09344165
         0.         0.08790583 0.         0.08829649]

     method    auc       rmse
      LS     0.851463  0.200439
      NLS    0.841941  0.529146
      NNLR   0.843245  0.204014
      GT     0.823391  0.217370
