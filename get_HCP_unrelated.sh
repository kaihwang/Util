

for subject in $(cat /home/kahwang/hcp_unrelated); do

	if [ ! -d /data/not_backed_up/shared/HCP/${subject} ]; then
		echo $subject

		mkdir /data/not_backed_up/shared/HCP/${subject}
		mkdir /data/not_backed_up/shared/HCP/${subject}/MNINonLinear
		mkdir /data/not_backed_up/shared/HCP/${subject}/release-notes
		mkdir /data/not_backed_up/shared/HCP/${subject}/T1w

		aws s3 sync s3://hcp-openaccess/HCP_1200/${subject}/MNINonLinear/ /data/not_backed_up/shared/HCP/${subject}/MNINonLinear/
		aws s3 sync s3://hcp-openaccess/HCP_1200/${subject}/release-notes/ /data/not_backed_up/shared/HCP/${subject}/release-notes/
		aws s3 sync s3://hcp-openaccess/HCP_1200/${subject}/T1w/ /data/not_backed_up/shared/HCP/${subject}/T1w/


	fi

done