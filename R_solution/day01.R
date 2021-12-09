#! /usr/bin/Rscript

# read data
data_1 <- read.table("data/data_01.txt")
# Lag 1 data point
data_1$V1 |>
    diff() |>
    {
        function(x) x > 0
    }() |>
    sum()
# Lag 3 data point
data_1$V1 |>
    diff(3) |>
    {
        function(x) x > 0
    }() |>
    sum()