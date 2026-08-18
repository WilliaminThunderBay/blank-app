#!/usr/bin/env python3
"""Parse a small mdadm-style RAID status sample."""
import re,sys
sample='''md0 : active raid1 sdb1[1]\n      976630336 blocks super 1.2 [2/1] [_U]\n'''
text=open(sys.argv[1],encoding='utf-8').read() if len(sys.argv)>1 else sample
match=re.search(r'\[(\d+)/(\d+)\].*?\[([U_]+)\]',text,re.S)
if not match:
    print('UNKNOWN'); raise SystemExit(1)
total,active,bitmap=int(match.group(1)),int(match.group(2)),match.group(3)
state='HEALTHY' if active==total and '_' not in bitmap else 'DEGRADED'
print(state, f'{active}/{total}', bitmap)
raise SystemExit(0 if state=='HEALTHY' else 2)
