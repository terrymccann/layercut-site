---
title: Install and first cut
intro: Install LayerCut, open a model, and export your first cut files in about five minutes.
---

## Install on a Mac

1. [Download LayerCut for Mac](/#download). It's one universal app for Apple silicon and Intel Macs running macOS 11 or later.
2. Open the downloaded `.dmg` and drag **LayerCut** onto **Applications**.
3. Open LayerCut from Applications or Launchpad. The first time, macOS asks whether you want to open an app downloaded from the internet. Click **Open**.

## Install on Windows

1. [Download LayerCut for Windows](/#download). It runs on 64-bit Windows 10 and 11.
2. Run `LayerCut_x.y.z_x64-setup.exe`. It installs for your user account, so it doesn't ask for an administrator password, and adds LayerCut to the Start menu.
3. If the PC doesn't have Microsoft Edge WebView2 yet, the installer downloads it. Most Windows 10 and 11 PCs already have it.

> If Windows shows **Windows protected your PC** for a brand-new release, click **More info** and check the publisher is LayerCut, then click **Run anyway**. Windows shows this for new downloads until enough people have installed them.

## Updates

LayerCut checks for a new version when it starts. When one is available it tells you what changed and asks before installing it. You can also choose **Help → Check for Updates…** at any time.

## Your first cut

### 1. Open a model

Drag an STL or OBJ file onto the window, click **Open model…**, or choose **File → Open Model** (<kbd>⌘O</kbd>, <kbd>Ctrl+O</kbd> on Windows). LayerCut assumes the model is in millimeters. Its name and size appear in the top bar.

The model is sliced straight away with the current settings, and the result appears in the 3D view.

### 2. Choose your material

At the top of the settings, pick the material you'll cut. The line underneath shows its key values: thickness, kerf, pin size and laser settings. If you haven't set up your own material yet, start with the example and read [Materials](/docs/materials/) and [The fit test](/docs/fit-test/) before cutting anything that matters.

### 3. Size the model

Under **Model**, set the finished size with **Scale** (a percentage) or switch **Size by** to **Height** and type the finished height in millimeters. If the model is lying on its side, change **Up axis**.

### 4. Choose how it's built

Under **Construction**, choose **Stacked**, **Interlock** or **Panels**. Each mode has its own settings, described in the [build mode pages](/docs/stacked/).

### 5. Check the result

The top bar shows how many pieces and sheets you'll need and how much of the material is used. If there's a warning badge, click it and read the notes; they say what to change. Switch to **Sheets** (<kbd>⌘2</kbd>) to see the cut sheets themselves.

### 6. Export

Click **Export…** (<kbd>⌘E</kbd>), choose the formats you want, then choose a folder. LayerCut writes one file per sheet plus an assembly guide, and offers to show them in Finder or Explorer. Open the files in LightBurn, or any program that reads SVG, and cut.

> Cut one sheet first, check that the pieces fit, then cut the rest.
