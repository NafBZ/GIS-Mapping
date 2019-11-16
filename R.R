library(dplyr)
library(cluster)
library(ggplot2)
library(NbClust)
library(factoextra)

setwd("C:/Users/user/Desktop/Sem 8/FYP Model/")

data <- read.csv("Terengganu Data.csv")

View(data)

data <- data %>% rename(DISTANCE_FROM_SEA = DISTANCE.FROM.SEA..KM.)
data <- data %>% rename(ALTITUDE = ALTITUDE.ELEVATION..M.)
data <- data %>% rename(ANNUAL_RAINFALL = ANNUAL.RAINFALL..MM.)

tdata <- data[3:6]

typeof(tdata$POPULATION)
typeof(tdata$DISTANCE_FROM_SEA)
typeof(tdata$ALTITUDE)
typeof(tdata$ANNUAL_RAINFALL)


head(tdata)

#apply Principal Component Analysis
pca <- prcomp(tdata, center = TRUE, scale = TRUE)

summary(pca)
pca
attributes(pca)
pca$x

fviz_eig(pca)

pca_data <- data.frame(pca$x[,1:2])

head(pca_data)
View(pca_data)

#determining optimal no. of clusters
set.seed(123)

#elbow method using within sum of squared distance
v <- vector()

for (i in 1:10)
  v[i] <- sum(kmeans(pca_data, i)$withinss)
plot(1:10, v, type = "b", main = paste('Clusters'), 
     xlab = "No. of Clusters", ylab = "WSS")

fviz_nbclust(pca_data, kmeans, method = "wss") +
  geom_vline(xintercept = 6, linetype = 2) +
  labs(subtitle = "WithinSS")

#gap-stat method
fviz_nbclust(pca_data, kmeans, nstart = 10, method = "gap_stat", nboot = 50) +
  labs(subtitle = "Gap-Stat")

#silhouette method
fviz_nbclust(pca_data, kmeans, method = "silhouette") +
  labs(subtitle = "Silhouette")


#apply k-means clustering model
kmodel <- kmeans(pca_data, 6)

attributes(kmodel)
kmodel
head(kmodel)
kmodel$cluster
kmodel$size
kmodel$withinss

result <- data.frame(data, kmodel$cluster)
head(result)
View(result)
result <- result %>% rename(Cluster = kmodel.cluster)


#visualization
names(result)
b <- ggplot(result, aes(x=factor(Cluster))) +
  geom_bar(stat="count", width=0.7, fill="steelblue") +
  labs(x = "Cluster", y = "No. of Towns", title = "K-Means Result")
b

clusplot(pca_data, kmodel$cluster, main = "2D Reperesentation of Clusters",
         color = TRUE, shade = TRUE, labels = 2, lines = 0)

fviz_cluster(kmodel, pca_data, ellipse.type = "norm")

fviz_cluster(kmodel, pca_data, palette = "Set2", ggtheme = theme_minimal())


#write data-frame into a new csv file
write.csv(result, file = "result.csv", row.names=FALSE)

#analysis of clusters

#r <- scale(tdata)
#r <- data.frame(r, Cluster = result$Cluster)
#r
r <- data.frame(tdata, Cluster = result$Cluster)
r %>% filter(Cluster == 1)
r %>% filter(Cluster == 2)


analysis <- data.frame(CLuster = numeric(), Population = double(), Distance_from_sea = double(), 
                       Altitude = double(), Annual_rainfall = double())

for (i in 1:6)
  analysis[i,] <- c(i,
                    mean(result$POPULATION[result$Cluster == i]),
                    mean(result$DISTANCE_FROM_SEA[result$Cluster == i]),
                    mean(result$ALTITUDE[result$Cluster == i]),
                    mean(result$ANNUAL_RAINFALL[result$Cluster == i]))

analysis






