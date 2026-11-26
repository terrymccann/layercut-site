---
title: Troubleshooting
intro: Fixes for the problems people run into most often.
---

## Installing

**Mac says LayerCut “can't be opened”.** Download it again from [layercut.app](/#download); a download can be damaged. LayerCut is signed and notarized by Apple, so macOS only asks you to confirm opening an app from the internet.

**Windows shows “Windows protected your PC”.** Click **More info**, check the publisher is LayerCut, then click **Run anyway**. Windows shows this for new releases until enough people have installed them.

**Windows says WebView2 is missing.** The installer downloads it automatically when the PC is online. On an offline PC, install the [WebView2 Evergreen Runtime](https://developer.microsoft.com/microsoft-edge/webview2/) from another computer first.

## Opening models

**The model is tiny or huge.** It was probably saved in inches or centimeters. Set **Scale**: 2540% converts a model saved in inches, and 1000% one saved in centimeters. Or use **Size by → Height**.

**The model is lying on its side.** Change **Up axis**.

**“The mesh is not watertight.”** The model has holes in its surface. Repair it in your modeling program or a 3D printing slicer, then export it again.

**Panels finds no walls.** Panels mode needs thin, flat walls. Solid models work better as Stacked or Interlocking.

## Fit

**Slots are too tight or too loose.** Cut the [fit test](/docs/fit-test/) and update **Slot clearance** in the material. Check the measured thickness too: sheets vary.

**Pieces come out the wrong size.** Your kerf is off. Measure the fit test's 20 mm square and update **Kerf**.

**Pin holes are too tight.** Raise **Hole clearance** in the material, or check the pin diameter matches your dowels.

## Cutting

**The SVG imports at the wrong size.** LayerCut's SVGs are in millimeters. In your laser software, check that it reads the SVG's own size instead of applying a fixed DPI. LightBurn .lbrn2 files avoid this entirely.

**Engraving happens after cutting and pieces move.** In LightBurn, LayerCut puts engraving on C01 so it runs first. If you've reordered layers, move C01 back above C02.

**A piece is missing from the sheets.** It's bigger than the sheet. The warning says which one: reduce the scale or set a larger sheet.

## Still stuck?

Email [hello@layercut.app](mailto:hello@layercut.app) with the model, if you can share it, and a screenshot of the settings.
