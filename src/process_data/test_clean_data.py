import clean_data

wi = clean_data.Team("Wisconsin", 1500)
ind = clean_data.Team("Indiana", 1500)

clean_data.calc_elo(wi, ind, 0)

print("Wisconsin: "+ str(int(wi.elo)) + "\n")
print("Indiana: " + str(int(ind.elo)) + "\n")