# Governance Charter

Xyraiq is open-spec but **certified-results-controlled**.  
We keep the test vectors public; we keep the scoring weights + certification keys semi-closed.

## Roles

| Role | Responsibility |
| ---- | -------------- |
| *Stewards* | Merge PRs, version the spec, manage Releases |
| *Auditors* | Independently verify detectors & maths |
| *DAO Voters* (TBD) | Ratify major spec bumps (v1.0+) |

## Release policy

1. Patch (0.x.y) = typo / doc fix.  
2. Minor (0.y.0) = new detectors / weight tweaks.  
3. Major (1.0) = breaking JSON schema changes.

## Contributing

Pull requests welcome for:

* New detector plug-ins (`src/xyraiq/detectors/`)
* Language-localised prompt packs
* Bug fixes & test cases

All contributors sign a **CLA** (Apache-2.0 for code, CC-BY-SA for docs).

## Ethical stance

*No training data gets submitted back to vendors.*  
Scorecards contain **only** metrics, never raw transcript chunks.

## Oversight board (seed list)

| Name | Expertise |
| ---- | --------- |
| George N. (Founder) | AI governance, spec author |
| TBD (2 seats) | Academic robustness research |
| TBD (2 seats) | Industry LLM deployment |

Board seats are rotated every 18 months via simple-majority DAO vote.
