# Research discovery maintenance

The root IndexNow ownership file enables URL submission without a Bing account.
Keep that file published. The key is an IndexNow ownership token, not a Google,
GitHub, or Bing account credential. `_tools` is excluded from Jekyll output.

After deploying meaningful changes to research pages:

```sh
python _tools/submit_indexnow.py
python _tools/submit_indexnow.py --submit --output /tmp/indexnow-receipt.json
```

The first command checks the live key and the seven configured URLs without
submitting. The second submits to the IndexNow shared endpoint. HTTP 200 means
receipt; HTTP 202 means receipt with ownership validation pending. Neither means
that pages are indexed or cited by an AI system. Avoid repeatedly submitting
unchanged pages. Update `indexnow.json` when publication URLs change.

Bing Webmaster Tools provides an optional account dashboard; IndexNow submission
does not create or verify a site in that dashboard. Google Search Console is
separate and continues to use `/sitemap.xml`.

Research questions on each publication page are paraphrases of the paper, with
source sections or figures where applicable. Keep version distinctions and
limitations when revising them. Do not add unsupported performance claims.
