library("dplyr")
data_3 <- read.table("data/data_03.txt", colClasses = "character")
data_split <- data.frame(do.call(rbind, strsplit(data_3$V1, "")))

get_one_zero <- function(data_vector) {
    one_count <- sum(data_vector == "1")
    zero_count <- sum(data_vector == "0")
    c(one_count, zero_count)
}
get_higher <- function(data_vector) {
    one_count <- get_one_zero(data_vector = data_vector)[1]
    zero_count <- get_one_zero(data_vector = data_vector)[2]
    compares <- one_count >= zero_count
    if (compares) {
        return("1")
    }
    "0"
}

get_lower <- function(data_vector) {
    one_count <- get_one_zero(data_vector = data_vector)[1]
    zero_count <- get_one_zero(data_vector = data_vector)[2]
    compares <- one_count > zero_count
    if (compares) {
        return("0")
    }
    "1"
}

gamma <- data_split %>%
    summarise_all(.funs = get_higher) %>%
    do.call(paste0, .) %>%
    strtoi(2)
epsilon <- data_split %>%
    summarise_all(.funs = get_lower) %>%
    do.call(paste0, .) %>%
    strtoi(2)
print(gamma * epsilon)




ogr <- data_split %>%
    filter(X1 == get_higher(X1)) %>%
    filter(X2 == get_higher(X2)) %>%
    filter(X3 == get_higher(X3)) %>%
    filter(X4 == get_higher(X4)) %>%
    filter(X5 == get_higher(X5)) %>%
    filter(X6 == get_higher(X6)) %>%
    filter(X7 == get_higher(X7)) %>%
    filter(X8 == get_higher(X8)) %>%
    filter(X9 == get_higher(X9)) %>%
    filter(X10 == get_higher(X10)) %>%
    filter(X11 == get_higher(X11)) %>%
    filter(X12 == get_higher(X12)) %>%
    do.call(paste0, .) %>%
    strtoi(2)
csr <- data_split %>%
    filter(X1 == get_lower(X1)) %>%
    filter(X2 == get_lower(X2)) %>%
    filter(X3 == get_lower(X3)) %>%
    filter(X4 == get_lower(X4)) %>%
    filter(X5 == get_lower(X5)) %>%
    filter(X6 == get_lower(X6)) %>%
    filter(X7 == get_lower(X7)) %>%
    filter(X8 == get_lower(X8)) %>%
    filter(X9 == get_lower(X9)) %>%
    do.call(paste0, .) %>%
    strtoi(2)

# filter(X10 == get_lower(X10)) %>%
# filter(X11 == get_lower(X11)) %>%
# filter(X12 == get_lower(X12)) %>%
# do.call(paste0, .) %>%
# strtoi(2)
print(csr * ogr)