---
title: Warnings and notes
intro: When something won't cut or fit the way you'd expect, LayerCut tells you, names the pieces involved, and suggests a fix.
---

Click the badge in the top bar to read the messages. **Warnings** (amber) are things to fix or check before cutting. **Notes** are information, such as how many joints of each kind a panels build has.

## Any build

| Message | What to do |
|---|---|
| The mesh is not watertight | The model has holes in its surface, and some outlines may be incomplete. Repair the mesh in your modeling program or a 3D printing slicer. |
| Outlines could not be closed cleanly | Same cause as above: check the mesh for holes. |
| Pieces are larger than the sheet and were left out | Reduce the scale, or set a larger sheet size. |
| Dropped islands smaller than … mm² | Tiny pieces were left out. Lower **Drop islands under** to keep them. |
| Piece … is too small for a label | It's cut without a number. Note where it goes, or turn labels off. |

## Stacked

| Message | What to do |
|---|---|
| Model height is not a multiple of the thickness | Information: LayerCut centers the model in the stack and tells you the finished height. |
| Layers have no material at this thickness | A sliver of the model falls between layers. Change **Slice at** or the scale slightly. |
| Not enough room for alignment pins between layers … | Those layers don't overlap enough for a pin. Line them up by the scored guide lines. |
| Walls are too thin for the pins | Raise the hollow **Wall thickness**, use a smaller pin, or lower the pin **Edge margin**. |
| Nothing could be hollowed | The model is thinner than two walls everywhere. Use a thinner wall, or turn Hollow off. |

## Interlocking

| Message | What to do |
|---|---|
| Crossings can't slide together because the shape overhangs | No slot was cut there. Try different slice counts, or for radial, more or fewer rings or a larger hub. |
| Slots leave less than … mm of material and may snap | Use fewer slices, move a slice, or lower **Min. material** if you accept the risk. |
| Slots sit close to an edge and leave a thin strip | Increase **Edge inset** or use **Auto**, drag those slices inward, or use fewer slices. |
| Slots split … into separate pieces | The pieces are labeled .1, .2 and so on, and only stay in place once assembled. |
| Slices are only … mm apart | Use fewer slices or thinner material. |
| Some slices or rings overlap each other | Move them apart, or use fewer. |
| Spokes are only … mm apart at the hub | Use a larger **Hub radius** or fewer spokes. |
| Slices miss the model and were skipped | A slice you moved is outside the model. Reset it. |
| No slices cross each other | Nothing holds the model together. Use more slices, or move them so they cross. |

## Panels

| Message | What to do |
|---|---|
| No flat walls were found | Panels suit thin-walled boxes and organizers. Try Stacked or Interlocking for solid shapes. |
| Some walls are thicker than the limit and were left out | Raise **Thickest model wall** to the value LayerCut suggests. |
| …% of the model's surface isn't flat walls | Curves, fillets, angled or thick parts were left out. Check the 3D view to see what's missing. |
| Rounded corners curve too tightly for a living hinge | Their radius is under three times the material thickness. Make the radius bigger in the model, or use thinner material. |
| Curved walls couldn't be unrolled into a strip | Those walls were left out. Check the model's curved walls are smooth and evenly thick. |
| Dividers meet a curved wall at too sharp an angle | Glue those dividers in place. |
| Shelves cross a curved wall partway up | They aren't joined to the wall. Glue them. |
| Joints at a very shallow angle were skipped | Glue those panels. |
| Crossings can't be half-lapped because neither panel ends there | Glue them, or change the model so one of the panels ends at the crossing. |
| Joints split … into separate pieces | Check those panels in the Sheets view. |
| Small loose bits were dropped | Tiny offcuts between joints were removed. Check the joints there look right. |
