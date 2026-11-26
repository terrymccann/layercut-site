---
title: Command-line tool
intro: layercut-cli runs the same slicer as the app, for batch jobs and scripts. It reads the same materials file.
---

> The command-line tool isn't included in the beta installers yet. [Email us](mailto:hello@layercut.app) if you'd like to try it.

## Examples

```sh
# list your materials
layercut-cli profiles

# stacked, using a saved material, 90 mm tall
layercut-cli slice bust.stl -p "Birch 3mm K40" --height 90 -o out

# hollow pot: 8 mm walls, 2 solid floor layers
layercut-cli slice pot.stl -t 3 --hollow 8 --solid-bottom 2 -o out

# interlocking grid: 6 A slices by 5 B slices
layercut-cli slice vase.stl -t 3 --interlock 6x5 --edge-inset auto -o out

# radial: 8 spokes, 4 rings, as a hollow shell
layercut-cli slice vase.stl -t 3 --radial 8x4 --hollow 8 -o out

# panels for a thin-walled organizer
layercut-cli slice organizer.stl -t 3 --panels -o out

# a fit test sheet
layercut-cli fit-test -t 3.1 --kerf 0.15 --pin-diameter 3 -o fit-test
```

`-p` uses a saved material; flags such as `-t` (thickness) or `--kerf` override it. Run `layercut-cli slice --help` for every option. `--settings file.json` takes the same settings the app uses.

## Common options

| Option | What it does |
|---|---|
| `-t`, `--thickness` | Material thickness in mm |
| `--kerf` | Kerf in mm |
| `--height` | Finished height in mm |
| `--sheet 400x300` | Sheet size in mm |
| `--pins N`, `--pin-diameter` | Alignment pins per joint, and their size |
| `--interlock AxB` | Interlocking grid |
| `--radial SxR` | Radial spokes and rings; `--hub`, `--spoke-angle` |
| `--edge-inset MM` or `auto` | Edge inset for interlocking and radial |
| `--panels` | Panels; `--max-wall`, `--finger`, `--no-hinges`, `--keep-outer` |
| `-o` | Output folder |
