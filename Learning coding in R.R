library(datasets)
data(mtcars)
head(mtcars,5)
?mtcars

library(ggplot2)
ggplot(aes(x=disp,y=mpg),data=mtcars)+geom_point()