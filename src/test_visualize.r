library(tidyverse)
library(reshape)
cfb_data = read.csv("cleaned_data.csv")
#cfb_data = subset(cfb_data, select=c(date, Alabama, Ohio.State, Clemson, Auburn))
ggplot(data = cfb_data) +
    geom_line(mapping = aes(x = as.Date(date, format = "%m/%d/%Y"), y = Clemson)) +
    scale_x_date(date_labels = "%b %Y", limits = as.Date(c("1980-09-01", "2020-12-31"))) +
    xlab("Date") +
    ylab("Elo") 





