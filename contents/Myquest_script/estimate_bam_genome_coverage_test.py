# _*_ coding=utf-8 _*_

import subprocess

# Insert your directories here
sra_accession_number = ["SRR11951439", "SRR11951443"]

for sra_id in sra_accession_number:
    samtools_cmd = "samtools coverage " + sra_id + "_sort.bam | awk 'NR>1 {suma+=$5; sumb+=$3 } END { print suma/sumb}'"
    output = subprocess.run(samtools_cmd, shell=True, capture_output=True).stdout # The output of subproces stout is byte style, you need to convert it to str
    output = str(output)
    with open("/home/qgn1237/qgn1237/4_single_cell_SV_chimera/1_smooth_seq_95_sc_K562_SMRT/coverage_list", "a+") as f:
        f.write(sra_id + "\t" + output)
