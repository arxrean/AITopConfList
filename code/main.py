import os
import glob
import pandas as pd

def group_crawled_csvs():
	csvs = glob.glob('./collection/save/*.csv')
	papers = []
	for csvp in csvs:
		csv = pd.read_csv(csvp)
		if len(csv) == 0:
			raise
		papers.append(csv)
	csv = pd.concat(papers, axis=0).reset_index(drop=True)
	csv.to_csv('../list.csv', index=False)


if __name__ == '__main__':
	group_crawled_csvs()