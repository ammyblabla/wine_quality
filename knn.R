setwd("C:/Users/Chayanin/Desktop/Proj/AI")
install.packages("FastKNN")
install.packages("devtools")
install.packages("rfUtilities")
install.packages("kknn")
library("FastKNN")
library("devtools")
library("kknn")
library("rfUtilities")
library("ggplot2")
wine_data <- read.csv("winequality-red.csv", sep=",", header=T, fileEncoding="UTF-8-BOM")

check_train <- wine_data[1:1199,]
check_test <- wine_data[1200:1599,]
label_train <- check_train$quality
label_test <- check_test$quality
train <- subset(check_train, select = -c(quality))
test <- subset(check_test, select = -c(quality))

distance <- Distance_for_KNN_test(test, train)
ans <- knn_test_function(train, test, distance,label_train, k = 1)
ans <- as.integer(unlist(strsplit(ans,",")))

accuracy(ans, label_test)$PCC

findK <- data.frame("k"=1, "accuracy"=accuracy(ans, label_test)$PCC)
for (i in seq(2,nrow(check_train),1)) {
  ans <- knn_test_function(train, test, distance,label_train, k = i)
  ans <- as.integer(unlist(strsplit(ans,",")))
  findK <- rbind(findK, list(i, accuracy(ans, label_test)$PCC))
}
p <- plot_ly(data = findK, x = ~k, y = ~accuracy, type = 'scatter', mode = 'lines') %>%
               layout(title = "Finding the best K",
                      xaxis = list(title = "K"),
                      yaxis = list(title = "Accuracy"))
p

ans <- knn_test_function(train, test, distance,label_train, k = 113)





check_train$quality = as.factor(check_train$quality)
check_test$quality = as.factor(check_test$quality)
model <- train.kknn(quality ~ ., data = check_train, kmax = 1)
prediction <- predict(model, check_test[, -12])
accuracy(prediction, label_test)$PCC
CM <- table(check_test[, 12], prediction)


findK <- data.frame("k"=1, "accuracy"=accuracy(prediction, label_test)$PCC)
for (i in seq(2,1100,1)) {
  model <- train.kknn(quality ~ ., data = check_train, ks = i)
  prediction <- predict(model, check_test[, -12])
  findK <- rbind(findK, list(i, accuracy(prediction, label_test)$PCC))
}
