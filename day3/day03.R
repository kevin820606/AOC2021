data_3 <- read.table("data/data_03.txt", colClasses = "character")

completedata <- do.call(rbind, strsplit(data_3$V1, ""))
completedata |>