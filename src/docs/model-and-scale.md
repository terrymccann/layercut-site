---
title: Model, size and slicing
intro: Open your model the right way up, at the right size, and decide where each layer is sliced.
---

## Supported files

LayerCut opens **STL** (binary and text) and **OBJ** files. Drag a file onto the window, or use **Open model…**.

Models are read in **millimeters**. If a model comes in far too small or too large, it was probably saved in inches or meters; fix it with **Scale**.

The mesh should be **watertight**, with no holes in its surface. If it isn't, the top bar shows how many open edges it has, and some outlines may be incomplete. Most modeling programs can repair a mesh; in a slicer such as PrusaSlicer or Bambu Studio, the repair option does this.

## Up axis

**Up axis** (X, Y or Z) says which way is up. Stacked layers are horizontal, so the up axis decides which way the model is sliced. Panels and interlocking slices are worked out from the model's walls and footprint in the same frame.

Most CAD programs export Z-up, and some game and animation tools export Y-up. If the preview shows your model lying on its side, change the up axis.

## Size

**Size by** works in two ways:

- **Scale**: a percentage of the model's size.
- **Height**: type the finished height in millimeters, and LayerCut scales the model to match.

Everything follows the size: slice counts stay the same, while moved slices and edge insets scale with the model.

## Slicing (stacked)

**Slice at** chooses where in each layer's thickness the outline is taken:

- **Middle** (default): the closest match to the model's shape overall.
- **Bottom**: the outline is taken at each layer's lower face.
- **Top**: the outline is taken at each layer's upper face.

On a shape that narrows towards the top, such as a dome, Bottom gives slightly fuller layers and Top slightly smaller ones. Try both and compare them in the 3D view.

When the model's height isn't an exact number of layers, LayerCut centers the model in the stack so the top layer isn't wasted, and tells you the finished stack height.

**Drop islands under** leaves out tiny pieces, smaller than the area you set (4 mm² by default). These are usually crumbs from noisy scans or the very tips of a shape. LayerCut notes how many it dropped.
