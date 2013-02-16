library(snow)
library(doSNOW)
library(foreach)

#Replace MASTER and NODE001 with the appropriate IP Address
cl = makeCluster(c("MASTER.compute-1.amazonaws.com", "NODE001.compute-1.amazonaws.com"), type="SOCK")
registerDoSNOW(cl)

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
