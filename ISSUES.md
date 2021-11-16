```
share-worker-1  |   File "/code/share/transformers/gov_nih.py", line 281, in get_pi
share-worker-1  |     pi_list = ctx['PIS']['PI'] if isinstance(ctx['PIS']['PI'], list) else [ctx['PIS']['PI']]
share-worker-1  | KeyError: 'PI'
```


```
share/harvesters/gov_clinicaltrials.py
```