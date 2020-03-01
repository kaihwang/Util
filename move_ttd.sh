


for subject in 6601 6602 6603 6605 6617 7002 7003 7004 7006 7008 7009 7012 7014 7016 7017 7018 7019; do


	mkdir /data/backed_up/kahwang/TTD/preprocessed/sub-${subject}/derivatives/
	
	for session in Loc loc Ips S1; do
		mkdir /data/backed_up/kahwang/TTD/preprocessed/sub-${subject}/derivatives/ses-${session}
		cp /data/backed_up/kahwang/TTD/Results/sub-${subject}/ses-${session}/Localizer_FIR_errts.nii.gz /data/backed_up/kahwang/TTD/preprocessed/sub-${subject}/derivatives/ses-${session}/Localizer_FIR_errts.nii.gz
		cp /data/backed_up/kahwang/TTD/Results/sub-${subject}/ses-${session}/Localizer_FIR_MNI_errts.nii.gz /data/backed_up/kahwang/TTD/preprocessed/sub-${subject}/derivatives/ses-${session}/Localizer_FIR_MNI_errts.nii.gz

	done


done