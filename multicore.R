library(foreach)
library(doParallel)

cl = makeCluster(3)
registerDoParallel(cl)

unif.trans = function(){
    results = matrix(nrow=100,ncol=100)
    for(i in 1:100){
    results[i,] = runif(100) 
    exponential = -log(results)
    }
    return(mean(exponential))
  }

x = foreach(i=1:100, .combine='c') %dopar% unif.trans()
mean(x)
