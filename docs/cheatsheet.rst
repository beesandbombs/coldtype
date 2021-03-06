Cheatsheet
==========

.. csv-table:: Single-Key Action Shortcuts in the App (Default Layer)
    :header: "Key", "Action", "Notes"
    :widths: 50, 100, 200

    "``=``", "zoom in", ""
    "``-``", "zoom out", ""
    "``→``", "one frame forward (in animation)", ""
    "``←``", "one frame backward (in animation)", ""
    "``a``", "``render_all``", "render/rasterize all renderables and frames in renderables"
    "``w``", "``render_workarea``", "for partial animation rendering"
    "``r``", "``restart_renderer``", "to reload code not in source file"
    "``l``", "``release``", "to call special ``release`` fn"
    "``m``", "``toggle_multiplex``", "turn multiplexing on/off"

All of those single-key shortcuts also work as single-letter actions in the command buffer (below) and the hanging process stdin.

.. csv-table:: Single-Key Editing Shortcuts in the App (Default Layer)
    :header: "Key", "Action", "Notes"
    :widths: 50, 100, 200

    "``q``", "Quit", ""
    "``0``", "Set zoom to 100%", ""
    "``c``", "(C)ommand", "enter the command buffer layer"
    "``d``", "e(D)iting", "enter the editing layer (if available)"

.. csv-table:: Abbreviated Commands
    :header: "Abbrv", "Expansion", "Arguments"
    :widths: 50, 80, 100

    "``pf``", "`preview-frame`", "list of <frame-index> (space-delimited)"
    "``ps``", "`preview-scale`", "<float>"
    "``ff``", "`filter-functions`", "<regex>"
    "``rp``", "`reset-filepath`", "<filepath>"

These abbreviations can be typed into the command buffer in the app (available by hitting ``c``), or into the stdin of the hanging process in the command line.

For example, once a coldtype program is running, you can hit ``c``, then enter `ps 2` to zoom the viewer to 200%-percent scale.