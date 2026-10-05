# Instagram Scraper Skills for AI Agents

Five focused agent skills for collecting public Instagram data with
[DataVoyantLab Actors on Apify](https://apify.com/datavoyantlab).

Use them from Codex, Claude Code, Cursor, OpenClaw, and other agents supported by
the open Agent Skills ecosystem. Each skill uses the Apify REST API, checks the
Actor's current pay-per-event pricing, and applies a maximum run charge.

## Skills

| Skill | Use it for | Apify Actor |
| --- | --- | --- |
| [instagram-stories-scraper](skills/instagram-stories-scraper/SKILL.md) | Current public Stories, media URLs, timestamps, mentions, links, music, locations, and partnership metadata | [Advanced Instagram Stories Scraper](https://apify.com/datavoyantlab/advanced-instagram-stories-scraper) |
| [instagram-followers-scraper](skills/instagram-followers-scraper/SKILL.md) | Public follower lists and profile fields | [Instagram Followers Scraper](https://apify.com/datavoyantlab/instagram-followers-scraper) |
| [instagram-following-scraper](skills/instagram-following-scraper/SKILL.md) | Accounts followed by a public Instagram profile | [Instagram Following Scraper](https://apify.com/datavoyantlab/instagram-following-scraper) |
| [instagram-highlights-scraper](skills/instagram-highlights-scraper/SKILL.md) | Public Instagram Highlight URLs and their story media | [Instagram Highlights Scraper](https://apify.com/datavoyantlab/instagram-highlights-scraper-api-by-url) |
| [instagram-campaign-monitor](skills/instagram-campaign-monitor/SKILL.md) | Recent campaign hashtag posts, brand filtering, and webhook monitoring | [Instagram Campaign Hashtag Monitor](https://apify.com/datavoyantlab/instagram-campaign-hashtag-monitor) |

## Install

List the available skills:

```bash
npx skills add DataVoyantLab/instagram-agent-skills --list
```

Install all five:

```bash
npx skills add DataVoyantLab/instagram-agent-skills --all
```

Install only Advanced Instagram Stories:

```bash
npx skills add DataVoyantLab/instagram-agent-skills \
  --skill instagram-stories-scraper
```

## Apify setup

These skills call paid external services on Apify. Use a paid Apify account or
an approved DataVoyantLab Free-user entitlement.

Create a token in
[Apify integrations](https://console.apify.com/account/integrations), then expose
it to your agent:

```bash
export APIFY_TOKEN="your_token"
```

Do not paste the token into prompts, source files, or committed configuration.

Approved Free users have limited access. To request access, email
`datavoyant@gmail.com` with the Apify user ID that will run the Actor.

## Examples

- “Download the current public stories for natgeo and return every media URL.”
- “Get the followers of this public Instagram profile with a maximum spend of $2.”
- “Find the accounts followed by these three Instagram usernames.”
- “Extract the story items from these Instagram Highlight URLs.”
- “Monitor #mycampaign from the last 24 hours and send matching posts to this webhook.”

The skills preserve the complete dataset response and return the run or dataset
identifier so the result can be reused in another workflow.

## Spend controls

- Current pricing is read from the public Actor API before execution.
- Every run uses Apify's `maxTotalChargeUsd` parameter.
- Followers and Following default to a $5 maximum when the user does not state a
  budget.
- A run is not started when its price cannot be verified.

Learn more at
[datavoyantlab.com/agent-skills/instagram](https://datavoyantlab.com/agent-skills/instagram).

## License

MIT-0
