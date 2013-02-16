from IPython.parallel import Client
import numpy as np

cluster = Client(packer='pickle')
nodes = cluster[:]

def uniform_transform(z):
    import scipy.stats as stats
    import numpy as np
    sample = list()
    for i in xrange(1000):
        sample.append(stats.uniform.rvs(size=1000))
    sample = np.asarray(sample)
    exponential = -np.log(sample)
    return np.mean(exponential)

results = nodes.map_async(uniform_transform, xrange(1000))
means = results.get()
mean = np.mean(means)
