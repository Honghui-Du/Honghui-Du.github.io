"""Validate deployed research URLs; submit only with --submit.

Usage: python _tools/submit_indexnow.py [--submit] [--output receipt.json]
IndexNow receipts acknowledge receipt, not indexing or AI citations.
"""
import argparse
import datetime
import json
from pathlib import Path
import urllib.request
import urllib.parse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--submit', action='store_true')
parser.add_argument('--output', type=Path)
args = parser.parse_args()
payload = json.loads(Path(__file__).with_name('indexnow.json').read_text())
with urllib.request.urlopen(payload['keyLocation'], timeout=30) as response:
    if response.read().decode().strip() != payload['key']:
        raise SystemExit('Deployed ownership file does not match; no submission sent.')
for url in payload['urlList']:
    if urllib.parse.urlsplit(url).netloc != payload['host']:
        raise SystemExit('URL outside configured host; no submission sent.')
    with urllib.request.urlopen(url, timeout=30) as response:
        if response.status != 200 or response.url != url:
            raise SystemExit(f'URL is unavailable or redirects: {url}')
receipt = {'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'urls': payload['urlList'], 'submitted': False}
if args.submit:
    request = urllib.request.Request('https://api.indexnow.org/indexnow',
        data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json; charset=utf-8'})
    with urllib.request.urlopen(request, timeout=60) as response:
        receipt.update(submitted=True, status=response.status,
                       response=response.read().decode(),
                       meaning='Received; key validation pending' if response.status == 202 else 'Received; not an indexing guarantee')
if args.output:
    args.output.write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
