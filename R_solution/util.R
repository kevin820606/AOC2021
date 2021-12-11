#! /usr/bin/Rscript
read_question <- function(day, example) {
    origin <- sprintf("data/data_%02d", day)
    if (!dir.exists("data")) origin <- sprintf("../data/data_%02d", day)
    path <- ifelse(example,
        sprintf("%s_example.txt", origin), sprintf("%s.txt", origin)
    )
    read.table(path, col.names = "Question_input", colClasses = "character")
}