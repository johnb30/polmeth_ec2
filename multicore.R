library(foreach)
library(doParallel)

cl = makeCluster(3)
registerDoParallel(cl)

unif.transform = function(){
    sample = matrix(nrow=100,ncol=100)
    for(i in 1:100){
    sample[i,] = runif(100) 
    exponential = -log(sample)
    }
    return(mean(exponential))
  }

x = foreach(i=1:100, .combine='c') %dopar% unif.transform()
mean(x)
