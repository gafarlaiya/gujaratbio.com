import json,sys
lang=sys.argv[1]; N=int(sys.argv[2]); src=sys.argv[3] if len(sys.argv)>3 else '1'
keys=json.load(open(f'i18n/src{src}.json')); d=json.load(open(f'i18n/{lang}.json'))
out=[];cnt=0
for l in open(f'i18n/src{src}.txt').read().split('\n'):
    if l.startswith('###'): out.append(l); continue
    if not l: continue
    n,t=l.split('\t',1)
    if keys[int(n)] in d: continue
    out.append(l); cnt+=1
    if cnt>=N: break
res=[l for i,l in enumerate(out) if not (l.startswith('###') and (i+1==len(out) or out[i+1].startswith('###')))]
print('\n'.join(res)); print('# remaining', sum(1 for k in keys if k not in d), file=sys.stderr)
