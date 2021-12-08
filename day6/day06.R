#!/usr/bin/Rscript

number_vec <- readLines("data/data_06_example.txt") |>
    strsplit(",") |>
    unlist() |>
    as.numeric()
numbertable <- table(number_vec)
for (i in 1:18) {
    zero <- number_table[0]
    number_table[0]
}