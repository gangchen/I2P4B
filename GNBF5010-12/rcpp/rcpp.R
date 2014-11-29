library(Rcpp)
library(inline)

src <- '
  Rcpp::NumericVector xa(a);

  double num1 = 0;
  double num2 = 1;
  double num_next = 1;
  int n = xa[0];
  Rcpp::NumericVector xab(xa[0]);

  if (n >=1)
    xab[xa[0]-n] = num1;
  if (n >=2)
    xab[xa[0]-n+1] = num2;
  for (int i = 0; i < n-1; i++){
    num_next = num1 + num2;
    xab[xa[0]-n+1+i] = num_next;
    num1 = num2;
    num2 = num_next;
  }

  return xab;
'

fibcxx <- cxxfunction(signature(a = "numeric"), src, plugin="Rcpp")
start = Sys.time()
r = fibcxx(1000)
end = Sys.time()
print(end-start)

fibR <- function(n){
  fibvals <- numeric(n)
  fibvals[1] <- 1
  fibvals[2] <- 1
  for (i in 3:n) {
    fibvals[i] <- fibvals[i-1]+fibvals[i-2]
  }
  fibvals
}
start = Sys.time()
r = fibR(1000)
end = Sys.time()
print(end-start)
