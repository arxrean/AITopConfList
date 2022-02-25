import os
import pandas as pd

if __name__ == '__main__':
	csv = pd.read_csv('./save/google.csv')
	csv.drop_duplicates(subset=['title'])
	queries = csv['url'].str.split('?').str[1].str.split('&').str[1]
	keyword = queries.str.split('+').str[0].str.replace('q=', '')
	source0 = queries.str.split('+').str[1].str.replace('source:%22', '')
	source1 = queries.str.split('+').str[2:-1].str.join(' ')
	source2 = queries.str.split('+').str[-1].str.replace('%22', '')
	source = source0 + ' ' + source1 + ' ' + source2
	csv['keyword'] = keyword
	csv['source'] = source
	csv = csv.drop(columns=['url'])
	csv.to_csv('./save/google2.csv', index=False)