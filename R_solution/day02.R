#!/usr/bin/Rscript

# read data
data_2 <- read.table("data/data_02.txt", col.names = c("action", "distance"))


# data refator
ans_data <- data.frame("action" = "Begin", "horizontal" = 0, "vertical" = 0)

data_2["horizontal"] <- data_2$distance
data_2$horizontal[data_2$action != "forward"] <- 0

data_2["vertical"] <- data_2$distance
data_2$vertical[data_2$action == "forward"] <- 0
data_2$vertical[data_2$action == "up"] <-
    -data_2$vertical[data_2$action == "up"]
data_2$distance <- NULL

ans_data <- rbind(ans_data, data_2)

# Q1
endpoint <- c(sum(ans_data$horizontal), sum(ans_data$vertical))
print(prod(endpoint))

# Q2
ans_data["aim"] <- cumsum(ans_data$vertical)
ans_data["vertical"] <- ans_data$aim * ans_data$horizontal

endpoint_V2 <- c(sum(ans_data$horizontal), sum(ans_data$vertical))
print(prod(endpoint_V2))