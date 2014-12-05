cgR <- function(){
  print("This is Hello World from cgR Package")
}

cgFibsum <- function(n){
    if ((n == 0) | (n == 1))
        return(1)
    else
        return(cgFibsum(n-1) + cgFibsum(n-2))
}
