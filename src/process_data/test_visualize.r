library(tidyverse)
cfb_data = read.csv("cleaned_data.csv")
ggplot(data = cfb_data) +
    geom_line(mapping = aes(x = as.Date(date, format = "%m/%d/%Y"), y = Ohio.State), color = "blue") +
    scale_x_date(date_labels = "%b %Y", limits = as.Date(c("1980-09-01", "2020-12-31")))




