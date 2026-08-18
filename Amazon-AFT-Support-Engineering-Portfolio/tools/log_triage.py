#!/usr/bin/env python3
"""Rank likely root causes from synthetic JSON-line support logs."""
import json, sys
from collections import Counter

def analyze(lines):
    events=[json.loads(x) for x in lines if x.strip()]
    counts=Counter(e.get('event') for e in events)
    evidence=[]
    if counts['raid_degraded']:
        evidence.append((0.94,'RAID_DEGRADED','degraded array detected'))
    if counts['api_timeout']>=3:
        evidence.append((0.77,'API_TIMEOUT',f"{counts['api_timeout']} API timeouts"))
    if counts['camera_lost']:
        evidence.append((0.65,'CAMERA_DEVICE','camera heartbeat loss'))
    for score,name,why in sorted(evidence, reverse=True):
        print(f"{name:18} score={score:.2f}  {why}")
    return 0 if evidence else 1

if __name__=='__main__':
    sample='''{"event":"raid_degraded"}\n{"event":"api_timeout"}\n{"event":"api_timeout"}\n{"event":"api_timeout"}\n{"event":"api_timeout"}\n'''
    if len(sys.argv)>1:
        with open(sys.argv[1],encoding='utf-8') as f: raise SystemExit(analyze(f))
    raise SystemExit(analyze(sample.splitlines()))
