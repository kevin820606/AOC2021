#! /usr/bin/Rscript
source("util.R")
raw_data <- read_question(11, F)
split_to_matrix <- function(lines) {
    mat <- matrix(ncol = 10, nrow = 0)

    for (line in lines) {
        mat <- rbind(mat, unlist(strsplit(line, "")) |>
            sapply(as.numeric, simplify = TRUE, USE.NAMES = FALSE))
    }
    mat
}

get_surround <- function(point) {
    back_move <- c(-11, -1, 9) + point
    horizon_move <- c(-10, 10) + point
    forward_move <- c(-9, 1, 11) + point
    all_point <- c(
        back_move[back_move %% 10 != 0],
        horizon_move, forward_move[(forward_move - 1) %% 10 != 0]
    )
    all_point[all_point > 0 & all_point < 101]
}
add_energy <- function(mat) {
    flash <- 1:100
    flashed <- c()
    repeat {
        for (fl in flash) mat[fl] <- mat[fl] + 1
        poppoint <- which(mat >= 10)[!which(mat >= 10) %in% flashed]
        flash <- sapply(poppoint, get_surround)
        flashed <- unique(c(flashed, which(mat >= 10)))
        if (sum(unlist(flash)) == 0) break
    }
    mat[flashed] <- 0
    mat
}

q1_solution <- function(mat, times) {
    init <- 0
    for (i in 1:times) {
        mat <- add_energy(mat)
        init <- init + sum(mat == 0)
    }
    init
}

q2_solution <- function(mat) {
    times <- 0
    repeat{
        times <- times + 1
        mat <- add_energy(mat)
        if (length(unique(as.vector(mat))) == 1) break
    }
    times
}

question_mat <- split_to_matrix(raw_data$Question_input)
print(q1_solution(question_mat, 100))
print(q2_solution(question_mat))