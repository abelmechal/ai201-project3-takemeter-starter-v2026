# TakeMeter planning notes

## Milestone 1 — Dataset choice

**Source:** The instructor-approved AG News dataset, using its training split.

**Scope:** Short English-language news articles classified by source topic.
The project uses 200 articles: 50 from each of the four provided classes.

## Milestone 2 — Source-label taxonomy

| Project label | AG News source label | Target |
| --- | --- | ---: |
| `world` | World | 50 |
| `sports` | Sports | 50 |
| `business` | Business | 50 |
| `sci_tech` | Sci/Tech | 50 |
| **Total** |  | **200** |

The labels are source-provided and instructor-approved. The dataset-building
script uses seed `20261021` to select the balanced sample reproducibly.

### Hardest boundary

`business` versus `sci_tech`: use `business` when the article is primarily
about financial or commercial activity; use `sci_tech` when it is primarily
about a scientific or technical development, even if a company is named.
