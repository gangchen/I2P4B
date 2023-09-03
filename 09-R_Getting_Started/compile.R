library(compiler)

f <- function(n, x=1) for (i in 1:n) x=1/(1+x)
cf = cmpfun(f)

system.time(f(1e6))

system.time(cf(1e6))
