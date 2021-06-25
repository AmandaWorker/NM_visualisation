# NM_visualisation

percentage_overlap.py script takes the z-scores and labels from the NM output and calculates percentage overlap per patient/control group. It formats the regions with the % overlap so that they can be copied and pasted into the R markdown code.

annotations.Rmd R markdown with a few lines of code from fsbrain to read in a parcellation file from fsaverage and change the values to those calculated in percentage_overlap.py

Overlaying on an inflated brain in freeview 
e.g.
module load freesurfer
freeview -f /data/project/BrainChart/fsaverage/surf/rh.white:overlay=rh_pos_pcnt_patient_05.mgz:overlay_method=linearopaque:overlay_threshold=0,100,percentile
