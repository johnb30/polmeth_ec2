from IPython.parallel import Client
import numpy as np

cluster = Client(packer='pickle')
nodes = cluster[:]

def uniform_transform(z):
    import scipy.stats as stats
    import numpy as np
    results = list()
    for i in xrange(100):
        results.append(stats.uniform.rvs(size=100))
    results = np.asarray(results)
    exponential = -np.log(results)
    return np.mean(exponential)

gather = nodes.map_async(uniform_transform, xrange(100))
means = gather.get()
mean = np.mean(means)
