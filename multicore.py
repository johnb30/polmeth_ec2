from joblib import Parallel, delayed
import numpy as np
import scipy.stats as stats

def uniform_transform():
    sample = list()
    for i in xrange(1000):
        sample.append(stats.uniform.rvs(size=1000))
    sample = np.asarray(sample)
    exponential = -np.log(sample)
    return np.mean(exponential)
    
results = Parallel(n_jobs=-1)(delayed(uniform_transform)() 
            for _ in xrange(1000))
finalMean = np.mean(results)
