// THE THURSDAY GLOBE — news-image-20261126 entry (Node 22, standard library only).
// The image is entry.png beside this file; the program copies it to
// /output/entry.png. The output name stays entry.png either way (PNG or JPEG
// by its first bytes). Deterministic: the same bytes every run.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
