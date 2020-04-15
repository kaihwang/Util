import pandas as pd
import glob as glob
import numpy as np
import os

def pivot_behav(TMS):
	#i=0
	
	rows = ['Subj', 'Cond', 'Motor', 'Match', 'Accu', 'FA', 'RH', 'LH', 'RT', 'OnsetTime', 'fn']
	if TMS:
		subjects = [7002, 7003, 7004, 7006, 7008, 7009, 7012, 7014, 7016, 7017, 7018, 7019, 7021,7022,7024,7025,7026,7027,6601, 6602, 6603, 6605, 6617]
		sessions = ['Ips', 'S1', 'Loc', 'loc']
	else:
		subjects = [6601, 6602, 6603, 6605, 6617, 7002, 7003, 7004, 7006, 7008, 7009, 7012, 7014, 7016, 7017, 7018, 7019]
		sessions = ['Loc', 'loc']


	df = pd.DataFrame() 

	for s in subjects:
		
		
		for ses in sessions:
			tdf = pd.DataFrame(columns=rows)
			fn = '/home/kahwang/bkh/TTD/ScanLogs/*%s*%s*txt' %(s, ses)
			fs = sorted(glob.glob(fn))
			for f in fs:
				print(f)
				tdf=tdf.append(pd.read_csv(f, sep='\t', header=None, names=rows))

			# if ses in ['Loc', 'loc']:
			# 	tdf['Session'] = 'Loc'
			# else:
			tdf['Session'] = ses
			
			tdf.reset_index(inplace = True)
			run = 1
			for i, row in tdf.iterrows():
				if i ==0:
					tdf.loc[i, 'Run'] = run
				elif i > 0:
					if tdf.loc[i-1, 'OnsetTime'] < tdf.loc[i, 'OnsetTime']:
						tdf.loc[i, 'Run'] = run	
					elif tdf.loc[i-1, 'OnsetTime'] > tdf.loc[i, 'OnsetTime']:		
						run = run+1
						tdf.loc[i, 'Run'] = run

			df = df.append(tdf)	


	df.loc[df['Cond'] == 'FH', 'Category' ] = 'Face'
	df.loc[df['Cond'] == 'F2', 'Category' ] = 'Face'
	df.loc[df['Cond'] == 'HF', 'Category' ] = 'Buildings'
	df.loc[df['Cond'] == 'H2', 'Category' ] = 'Buildings'
	df.loc[df['Cond'] == 'Hp', 'Category' ] = 'Localizer'
	df.loc[df['Cond'] == 'Fp', 'Category' ] = 'Localizer'
	df.loc[df['Cond'] == 'FH', 'Load' ] = '1-Back'
	df.loc[df['Cond'] == 'F2', 'Load' ] = '2-Back'
	df.loc[df['Cond'] == 'HF', 'Load' ] = '1-Back'
	df.loc[df['Cond'] == 'H2', 'Load' ] = '2-Back'		
	df.loc[df['Cond'] == 'Hp', 'Load' ] = 'Localizer'
	df.loc[df['Cond'] == 'Fp', 'Load' ] = 'Localizer'
	df.loc[df['RT'] == -1, 'RT' ] = np.nan
	df.loc[df['RT'] == 0, 'RT'] = np.nan
	#df = df[df['Cond']!='Hp']
	#df = df[df['Cond']!='Fp']

	df = df.drop(columns=['Motor', 'Match', 'RH', 'LH', 'fn'])

	return df

if __name__ == "__main__":

	behav_df = pivot_behav(TMS=True)
	behav_df.to_csv('/home/kahwang/RDSS/tmp/behav_df.csv')

