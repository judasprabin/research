# AU Visa Source Registry

Automated agent that discovers, catalogues, and tracks authoritative Australian
visa-related sources across official government domains. Maintains a master
source registry in Notion with change detection and dead-link checking.

## Quickstart

```bash
cd ~/Workspace/research/au-visa-sources
uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
cp .env.example .env  # fill in NOTION_TOKEN
```

## Usage

```bash
python main.py              # full run: crawl + upsert to Notion
python main.py --dry-run    # crawl + print without writing
python main.py --check-only # re-check existing URLs for changes/dead links
```

## In-scope sources

- immi.homeaffairs.gov.au — visa listings, processing times, fees
- homeaffairs.gov.au — policy, media releases
- legislation.gov.au — Migration Act, Regulations, instruments
- aat.gov.au / art.gov.au — tribunal decisions
- mara.gov.au — agent regulations
- studyaustralia.gov.au / jobsandskills.gov.au — occupation lists
- State/territory nomination pages (NSW, VIC, QLD, WA, SA)
- treasury.gov.au / budget.gov.au — budget measures
- abs.gov.au — migration statistics

Excludes: forums, blogs, marketing sites, Reddit, news aggregators.

## Schema

Each source record captures:
- Title, URL (canonical), Source authority
- Category (visa subclass page / legislation / policy / processing times / etc.)
- Related visa subclasses
- Published/updated date
- 2–3 sentence summary
- Reliability tier (1=legislation, 2=guidance, 3=supporting)
- Status (new/updated/unchanged/dead)
- Change log and content hash

## Cron

```crontab
0 6 * * * cd ~/Workspace/research/au-visa-sources && .venv/bin/python main.py >> logs/cron.log 2>&1
```