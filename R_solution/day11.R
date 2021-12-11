#! /usr/bin/Rscript
source("util.R")
raw_data <- read_question(11, T)
split_to_matrix <- function(lines) {
    mat <- matrix(ncol = 10, nrow = 0)

    for (line in lines) {
        mat <- rbind(mat, unlist(strsplit(line, "")) |>
            sapply(as.numeric, simplify = TRUE, USE.NAMES = FALSE))
    }
    mat
}

get_surround <- function(point, dont_move) {
    move <- c(-11, -10, -9, -1, 1, 9, 10, 11)
    aftermove <- point + move
    aftermove[aftermove > 0 & aftermove < 101 & !aftermove %in% dont_move]
}

add_energy <- function(mat) {
    flash <- 1:100
    flashed <- c()
    while (length(flash)) {
        for (fl in flash) mat[fl] <- mat[fl] + 1
        flash <- sapply(which(mat >= 10), get_surround, flashed)
        print(flash)
        flashed <- unique(c(flashed, which(mat >= 10)))
    }
    mat[flashed] <- 0
    mat
}

q1_solution <- function(mat, times) {
    for (i in 1:times) mat <- add_energy(mat)
    mat
}

question_mat <- split_to_matrix(raw_data$Question_input)
print(q1_solution(question_mat, 2))
