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
    
In the search sorting scene, in order to facilitate comparison, we chose AUC and RMSE for comparison.

By running the code "Non_negative_regression_demo.py". The readers will get the following results.

