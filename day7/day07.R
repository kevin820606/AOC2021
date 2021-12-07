#!/usr/bin/Rscript
number_vec <- readLines("data/data_07.txt", n = 1) |>
    strsplit(",") |>
    unlist() |>
    as.numeric()
minmax <- min(number_vec):max(number_vec)
# Q1
sapply(minmax, FUN = function(x) sum(abs(number_vec - x))) |> min()
# Q2
q2_fun <- function(x) {
    dist <- abs(number_vec - x)
    sum(((1 + dist) * dist) / 2)
}
sapply(minmax, FUN = q2_fun) |> min()