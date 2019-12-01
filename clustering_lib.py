import pandas as pd
import random as rnd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import math

# Finding optimal number of clusters by using silhouette score:
def n_cluster(df,A,B):
    
    num_clusters = np.arange(2,10)
    results = {}

    data = df[[A,B]].copy()
    for size in num_clusters:
        model = KMeans(n_clusters = size).fit(data)
        predictions = model.predict(data)
        results[size] = silhouette_score(data, predictions)

    best_size = max(results, key=results.get)
    return best_size

# K-means algorithm function:

def k_means(df,A,B,K):
    
    df = df[[A,B]].copy()
    n = len(df)
    R = rnd.randrange(0,n-1)
    k_list = [df.iloc[R]]
    
    i = 0
    distance = pd.DataFrame()

    while len(k_list) < K :

        point = k_list[i]
        new_df = df.apply(lambda x : (x - point)**2 , axis = 1)
        distance[i] = new_df.sum(axis = 1).apply(lambda x : x**(1/2))
        new_k = (distance.min(axis = 1)).idxmax()
        k_list.append(df.iloc[new_k])
        i += 1
        
    dist = pd.DataFrame()

    for i in range(len(k_list)) :

            point = k_list[i]
            new_df = df.apply(lambda x : (x - point)**2 , axis = 1)
            dist[i] = new_df.sum(axis = 1).apply(lambda x : x**(1/2))
            
    cluster = dist.idxmin(axis = 1)
    df["cluster"] = cluster

    cluster_pre = pd.Series(np.zeros(len(df)))
    
    while cluster.equals(cluster_pre) == False :
    
        centroid = df.groupby("cluster").mean()
        df = df.drop(['cluster'], axis=1)

        for i in range(len(centroid)):
            k_list[i] = centroid.iloc[i]

        for i in range(len(k_list)) :

            point = k_list[i]
            new_df = df.apply(lambda x : (x - point)**2 , axis = 1)
            dist[i] = new_df.sum(axis = 1).apply(lambda x : x**(1/2))

        cluster_pre = cluster    
        cluster = dist.idxmin(axis = 1)
        df["cluster"] = cluster
        return df, centroid
    
#  Rnad index for finding similarity between 2 clustering results:
    
def Rand_index(df ,df1):
    
    tuple_A = 0
    tuple_B = 0
    n = len(df)
    for j in range(n - 1):
        for h in range(j + 1, n):
            
            if df['cluster'].iloc[j] == df['cluster'].iloc[h] and df1['cluster'].iloc[j] == df1['cluster'].iloc[h]:
                tuple_A += 1
                
            elif df['cluster'].iloc[j] != df['cluster'].iloc[h] and df1['cluster'].iloc[j] != df1['cluster'].iloc[h]:
                tuple_B += 1

    Similarity =round((tuple_A + tuple_B)*100 / (math.factorial(n)/(2 * math.factorial(n-2))))
    
    print('Similarity between 2 clusters equals to %s%%'%(Similarity))