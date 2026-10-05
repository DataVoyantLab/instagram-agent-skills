---
name: instagram-campaign-monitor
description: Monitor recent public Instagram posts from campaign or branded hashtags through Apify, with optional brand-term filtering and webhook delivery. Use for recurring campaign tracking, UGC discovery, brand mentions, or scheduled hashtag reports; do not use for broad historical hashtag scraping.
metadata:
  openclaw:
    requires:
      env:
        - APIFY_TOKEN
      bins:
        - curl
        - jq
    primaryEnv: APIFY_TOKEN
    emoji: "📣"
    homepage: https://datavoyantlab.com/agent-skills/instagram
---

# Instagram Campaign Monitor

Use DataVoyantLab's Instagram Campaign Hashtag Monitor on Apify to find recent
public posts from branded or campaign hashtags, optionally filter them with
brand terms, and deliver results to a dataset or webhook.

This skill uses a paid external service on Apify. It requires a paid Apify
account or an approved DataVoyantLab Free-user entitlement.

## Actor contract

- Actor ID: `aXaAdkVNc5MZ60qbH`
- Store page: <https://apify.com/datavoyantlab/instagram-campaign-hashtag-monitor>
- Required: `campaign_hashtags`
- Optional: `brand_terms`, `webhook_url`, `notify_on_zero`
- `max_scan_pages`: integer from 1 to 10, default 10
- `last_hours`: integer from 1 to 168, default 24
- Billing events: Actor start plus each hashtag page scanned

Use branded or campaign-specific hashtags. Do not silently turn a broad topical
hashtag into an unbounded historical scrape.

## Prepare the request

1. Require `APIFY_TOKEN` and never display or persist it.
2. Strip a leading `#` from hashtags, trim whitespace, remove duplicates, and
   reject empty values.
3. Preserve brand terms as user-provided text after trimming and deduplication.
4. Validate `max_scan_pages` and `last_hours` against the Actor limits.
5. Accept a webhook only when the user supplied it. Require HTTPS and never
   invent a destination.
6. Construct JSON with `jq` and include:

```json
{
  "skill": true,
  "skillName": "instagram-campaign-monitor",
  "skillVersion": "1.0.0"
}
```

## Verify pricing and set the cap

Fetch `https://api.apify.com/v2/acts/aXaAdkVNc5MZ60qbH`. Select the latest
active entry in `.data.pricingInfos` and read the Actor-start price plus
`scan-page.eventPriceUsd`.

Calculate:

```text
maximum charge = actor start + (max_scan_pages × scan-page) + $0.01
```

Round up to the next cent. If active pricing or either event is missing, do not
start the run.

## Run asynchronously

Start:

```text
POST https://api.apify.com/v2/acts/aXaAdkVNc5MZ60qbH/runs
  ?waitForFinish=60
  &maxTotalChargeUsd=<calculated cap>
Authorization: Bearer $APIFY_TOKEN
Content-Type: application/json
```

Poll `GET /v2/actor-runs/<run ID>?waitForFinish=60` until terminal status. On
`SUCCEEDED`, retrieve
`GET /v2/actor-runs/<run ID>/dataset/items?clean=true&format=json`.

Launch directly after validation and price calculation. Do not request another
confirmation.

## Return

Return:

- every dataset item;
- the run ID and dataset ID;
- hashtags and time window used;
- pages scanned when available;
- the maximum authorized charge;
- whether a webhook was configured, without echoing sensitive query strings.

Zero matching posts is a valid result. Distinguish it from a failed Actor run.
For a failed terminal status, return the public status and run ID without
exposing private implementation details.

If Apify rejects an unapproved Free account, tell the user to email
`datavoyant@gmail.com` with their Apify user ID to request access.
