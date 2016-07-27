#!/usr/bin/python -i

hydrophobic=['PHE','TYR','ILE','LEU','VAL','TRP']
polar=['ARG','LYS','GLU','ASP','HIS','SER','THR','ASN','GLN']
charged=['ARG','LYS','GLU','ASP','HIS']
hydrophobic_core=[1096,1098,1170,1171,1174,1179,1239,1245,1271,1240]
label_dict={True:'activating', False:'non-activating', 'maybe':'unknown', 'wt':'wild type'}

def get_subdomains(protein,domainfile='calcs/kinase_subdomains'):
    with open(domainfile,'r') as fp: domain_lines=fp.readlines(); fp.close()
    for line in domain_lines:
        line.strip('\n')
        dom_info=line.split(' ')
        if dom_info[0].upper()==protein.upper():
            domains={'kd_start':int(dom_info[1]), 'kd_end':int(dom_info[2]),
                     'kinase domain':range(int(dom_info[1]), int(dom_info[2])),
                     'ploop_start':int(dom_info[3]), 'ploop_end':int(dom_info[4]),
                     'nucleotide binding loop':range(int(dom_info[3]), int(dom_info[4])),
                     'alphac_start':int(dom_info[5]), 'alphac_end':int(dom_info[6]),
                     u"$\\alpha$C helix":range(int(dom_info[5]), int(dom_info[6])),
                     'catloop_start':int(dom_info[7]), 'catloop_end':int(dom_info[8]),
                     'catalytic loop':range(int(dom_info[7]), int(dom_info[8])),
                     'activation_start':int(dom_info[9]), 'activation_end':int(dom_info[10]),
                     'activation loop':range(int(dom_info[9]), int(dom_info[10]))}
    domains[u"$\\alpha$C helix, activation loop"]=list(set(set(domains['activation loop'])|
                                                           set(domains[u"$\\alpha$C helix"])))
    domains[u"$\\alpha$C helix, nucleotide binding loop"]=list(set(set(domains['nucleotide binding loop'])|
                                                                   set(domains[u"$\\alpha$C helix"])))
    domains[u"$\\alpha$C helix, catalytic loop"]=list(set(set(domains['catalytic loop'])|
                                                          set(domains[u"$\\alpha$C helix"])))
    domains['nucleotide binding loop, activation loop']=list(set(set(domains['activation loop'])|
                                                                 set(domains['nucleotide binding loop'])))
    domains['nucleotide binding loop, catalytic loop']=list(set(set(domains['nucleotide binding loop'])|
                                                                set(domains['catalytic loop'])))
    domains['activation loop, catalytic loop']=list(set(set(domains['catalytic loop'])|
                                                        set(domains['activation loop'])))
    domains[u"$\\alpha$C helix, catalytic loop, activation loop"]=list(set(set(domains['activation loop'])|
                                                                           set(domains[u"$\\alpha$C helix"])|
                                                                           set(domains['catalytic loop'])))
    domains[u"$\\alpha$C helix, catalytic loop, nucleotide binding loop"]=list(set(set(
        domains['nucleotide binding loop'])|set(domains[u"$\\alpha$C helix"])|set(domains['catalytic loop'])))
    domains[u"$\\alpha$C helix, nucleotide binding loop, activation loop"]=list(set(set(
        domains['activation loop'])|set(domains[u"$\\alpha$C helix"])|set(domains['nucleotide binding loop'])))
    domains[u"nucleotide binding loop, $\\alpha$C helix, catalytic loop, activation loop"]=list(set(set(
        domains['activation loop'])|set(domains[u"$\\alpha$C helix"])|set(
            domains['catalytic loop'])|set(domains['nucleotide binding loop'])))
    domains[u"kinase domain - ($\\alpha$C helix, activation loop)"]=list(set(
        domains['kinase domain']) - set(domains[u"$\\alpha$C helix, activation loop"]))
    return domains