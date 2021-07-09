import os
import glob
import pandas as pd

def group_crawled_csvs():
	csvs = glob.glob('./collection/*.csv')
	csv = pd.concat([pd.read_csv(_) for _ in csvs], axis=0).reset_index(drop=True)
	csv.to_csv('../list.csv', index=False)


if __name__ == '__main__':
	group_crawled_csvs()