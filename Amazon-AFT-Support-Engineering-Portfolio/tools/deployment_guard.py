#!/usr/bin/env python3
"""Apply synthetic canary deployment health gates."""
import json, sys

def decision(m):
    reasons=[]
    if m['api_success_pct'] < 98: reasons.append('API success below 98%')
    if m['heartbeat_pct'] < 98: reasons.append('heartbeat below 98%')
    if m['error_pct'] > 2: reasons.append('error rate above 2%')
    return ('ROLLBACK' if reasons else 'PROCEED', reasons)

if __name__=='__main__':
    if len(sys.argv)>1:
        with open(sys.argv[1],encoding='utf-8') as f: metrics=json.load(f)
    else:
        metrics={'api_success_pct':96.4,'heartbeat_pct':97.2,'error_pct':3.6}
    state,reasons=decision(metrics)
    print(state)
    for reason in reasons: print('-', reason)
    raise SystemExit(2 if state=='ROLLBACK' else 0)
