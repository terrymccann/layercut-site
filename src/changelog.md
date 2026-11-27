---
title: Changelog
description: What's new in LayerCut: panels cut to fit your sheet, sizing by width, depth or height, models drawn in inches, automatic update checks, and fixes to cut sheets.
intro: What changed in each version of LayerCut, newest first.
updated: 2026-11-26
---

## Version 0.2.0 beta

November 2026

### New

- **Cut panels to fit your sheet.** When a panel is too big for your sheet, LayerCut asks whether to cut it to fit or to change the sheet size. If you choose to cut, the panel is divided into parts that fit and join with dovetail keys, so they line up and hold together without glue. Cuts are placed between slots, never through one, and stay clear of living hinges. The parts are labeled P1a, P1b and so on, and the notes say which panels were cut. You can turn this on or off at any time with **Cut pieces to fit** under Sheet. Panels mode only.
- **Size a model by width, depth or height.** Under Model, choose what to size by and type the finished measurement in millimeters. The other dimensions follow in proportion. Sizing by a percentage works as before.
- **Models drawn in inches.** STL and OBJ files don't record their units. If a model opens 25.4 times too small, set **File drawn in** to inches. LayerCut remembers the choice for your next model.
- **Double-click a piece to highlight it.** In the 3D view, double-click any piece to highlight it and see its name. Double-click it again, or empty space, to show everything. Orbiting, panning and zooming are unchanged.
- **Update checks.** LayerCut looks for a new version when it starts and tells you if there is one. You choose when to install it. You can also check at any time with **Check for Updates…**, in the LayerCut menu on Mac and the Help menu on Windows.
- **About LayerCut on Windows.** The Help menu now has an About item that shows the version you are running.

### Improved

- **The top bar shows the size you will cut.** Next to the file name you now see the model's width, depth and height in millimeters at the current scale, plus the percentage when it isn't 100%. Before, it showed the size in the file and didn't change when you scaled.
- **Every model opens at 100%.** A scale left over from the last model no longer carries over to the next one. Slices you moved by hand are cleared too.
- **Switching how you size a model no longer changes its size.** Choosing Width, Depth or Height starts from the size the model already has.
- **Windows wording.** Tooltips show Ctrl shortcuts, and the button after an export says **Show in Explorer**.
- **Clearer message when a piece is too big.** The warning now tells you what you can do about it.

### Fixed

- **Stray cut lines across a panel.** With some models and kerf settings, a straight cut line could appear from one side of a panel to the other, on screen and in the exported files. This is fixed.
- **Narrow strips cut into loose bits.** A wall too narrow to joint, such as a chamfer or a stacking lip, used to come out as a row of small loose pieces and notch the panel beside it. It is now left out, with a note saying what was dropped.
- **Tiny specks in the cut layer.** Cut sheets could contain marks a few thousandths of a millimeter across beside a panel's outline. They were invisible on screen, but a laser would still fire on them. They are no longer produced.
