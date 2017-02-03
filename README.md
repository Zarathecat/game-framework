This utility provides a framework for a variety of pygame games.
It includes:

    * A player object that can be moved in 4 directions with the keyboard
    * A screen
    * Collision-detection between the player and the screen edges,
      with the inability to walk beyond them
    * A grid with configurable width, height and cellsize,
    * Some configurable walls, collision detection between these
      and the player, and the inability to walk through them
    * 3 sample maps, with different walls, which include doors through
      which the player can move to change to a different map and move
      to the relevant place on the screen
    * Basic character objects with collision detection and text
      rendered upon collision. The player can currently walk through
      them. They are tied to the maps.
    * A handful of colours for dev purposes
    * Various misc config

It's designed primarily for RPGs, but might suit some platformers, too.
It is currently a test/wip, and not ready for any serious use.
