#! /usr/bin/Rscript
source("R_solution/util.R", encoding = "UTF-8")
library("dplyr")

half_brackets <- r"(\)|\}|\]|\>)"
complete_brackets <- r"(\(\)|\{\}|\<\>|\[\])"
q1_score <- c(")" = 3, "]" = 57, "}" = 1197, ">" = 25137)
q2_score <- c("(" = 1, "[" = 2, "{" = 3, "<" = 4)
remove_complete_brackets <- function(line) {
    while (stringr::str_detect(line, complete_brackets)) {
        line <- stringr::str_remove_all(line, complete_brackets)
    }
    line
}

raw_data <- read_question(10, F) %>%
    mutate(
        no_bracket = sapply(Question_input, remove_complete_brackets),
        is_corrupted = stringr::str_detect(no_bracket, half_brackets),
        is_incomplete = !is_corrupted
    )

raw_data[raw_data$is_corrupted, ] %>%
    mutate(
        get_first_half = stringr::str_match(no_bracket, half_brackets),
        get_score = q1_score[get_first_half]
    ) %>%
    summarise(Q1_total = sum(get_score))

raw_data[raw_data$is_incomplete, ] %>%
    mutate(
        rev_bracket = stringi::stri_reverse(no_bracket),
        get_score = sapply(
            rev_bracket,
            function(line) {
                Reduce(
                    function(x, y) x * 5 + y,
                    sapply(
                        stringr::str_split(line, ""),
                        FUN = function(x) q2_score[x]
                    ), 0
                )
            }
        )
    ) %>%
    summarise(Q2_total = median(get_score))