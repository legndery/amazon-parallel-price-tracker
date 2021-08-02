# Amazon Price Tracker
- User specified prouducts to track
- Extract Info about Products
- Generate Report Based on Info
- Alert on price change (Windows)
- SQlite, CSV support for the reports

## Setup Instructions

Make sure to download correct chromedriver - https://chromedriver.chromium.org/downloads

### Setup Python Virtual Environment
```buildoutcfg
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
### Put your links in inputs/links.txt
```
echo 'https://www.amazon.in/dp/B07YFF3JCN/' >> inputs/links.txt
```
## Running Script
```buildoutcfg
python start_tracker.py
```

## Screenshot:
- Charting support using matplotlib

![Alt text](/screens/B073GF2CL6.png?raw=true "Price change")