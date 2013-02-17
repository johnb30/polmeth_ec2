from joblib import Parallel, delayed
import numpy as np
import scipy.stats as stats

def uniform_trans():
    results = list()
    for i in xrange(100):
        results.append(stats.uniform.rvs(size=100))
    results = np.asarray(results)
    exponential = -np.log(results)
    return np.mean(exponential)
    
means = Parallel(n_jobs=-1)(delayed(uniform_trans)() 
            for _ in xrange(100))
finalMean = np.mean(means)
