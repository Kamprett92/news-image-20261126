[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Kamprett92/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Kamprett92/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

# THE THURSDAY GLOBE

A one-day world news image for **Thursday 26 November 2026**, drawn with code (Python PIL) as a newspaper front page: a navy masthead, one big lead panel, and a grid of eight short stories.

## The lead

**US slaps sweeping tariffs on 14 partners** — China, the EU, Japan and India hit in a crackdown on factory overcapacity. Markets rattled: the Nasdaq falls ~4% in an AI sell-off, shown in the chart beside the headline.

## The other stories

- **Cairo** — tanker fire kills at least 31 on the ring road.
- **Yemen** — Houthis hit Saudi ports and the Ras Tanura oil refinery.
- **Iran** — the US tells its citizens to leave as war fears grow.
- **Ukraine** — strikes Russia's Savasleyka airbase, damaging five aircraft (3 MiG-31, 2 Su-34).
- **North Korea** — Kim calls for wider deployment of tactical nuclear weapons.
- **Europe** — EU leaders clash in Brussels over a €45bn loan for Ukraine.
- **Indonesia** — mine flood kills 13 in Bogor, 13 more trapped.
- **Space** — first Pakistani astronaut boards China's Tiangong station.

## How it is built

`draw.py` draws `entry.png` (1024×1024, under 1 MiB) with PIL — masthead, lead panel with a Nasdaq chart, and the story grid. `main.ts` (Node 22, standard library only) copies `entry.png` to `/output` (or `$MAKEFUN_OUTPUT_DIR`); both runs write byte-identical output.

## Verification

`entry.png` is a valid PNG, 1024×1024, 108,472 bytes — inside the 1 MiB and 1024×1024 caps. Running `main.ts` twice produces the same sha256 both times, and the output matches `entry.png` byte for byte.
