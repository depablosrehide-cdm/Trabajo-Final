library(tidyverse)

df1 <- read.csv("formula 1.csv")

summary(df)

df <- df1 %>% drop_na(Time) %>% mutate(
    DriverName = as.factor(DriverName),
    Car = as.factor(Car),
    Race = as.factor(Race),
    Code = as.factor(Code),
    TimeOfDay = ymd(TimeOfDay)
)
    

summary(df)


