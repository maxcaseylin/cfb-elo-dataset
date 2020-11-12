#open csv, then transpose
import pandas

need_transpose = pandas.read_csv("src/old_processed_data/cleaned_data.csv", encoding="latin-1")
transpose = need_transpose.transpose();
transpose = transpose.iloc[1:]
transpose = transpose.rename(columns={})
transpose.to_csv("src/old_processed_data/cleaned_data.csv")