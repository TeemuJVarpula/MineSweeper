# MineSweeper
Minesweeper game with python
"
Unopened tiles (cover the board at the start of the game, can also be made by removing flags)
Numbered tiles (can show 1-8)
Blank tiles (no mines are on the diagonal/adjacent to the tile)
Flagged tiles (appear after right-clicking an unopened tile)
(?) Question marked tiles (appear after right-clicking a flagged tile; only exists in certain implementations)

An unopened cell is blank and clickable, while an opened cell is exposed. Flagged cells are unopened cells marked by the player to indicate a potential mine location; some implementations make flagged cells unopenable to reduce the risk of uncovering a suspected mine.

A player selects a cell to open it. If a player opens a cell containing a mine, the game ends in a loss. Otherwise, the opened cell displays either a number, indicating the number of mines diagonally and/or adjacent to it, or a blank tile (sometimes shown as a 0), and all adjacent cells will automatically be opened. This may cause a chain reaction; any blank tiles opened by other blank tiles open the surrounding tiles too. Players can also flag a cell, visualised by a flag being put on the tile, to denote that they believe a mine to be in that place. Flagged cells are still considered unopened, and may be unflagged. In some versions of the game, when the number of adjacent mines is equal to the number of adjacent flagged cells, all adjacent non-flagged unopened cells can be opened by both left and right-clicking (regardless of if any tiles are mines or not), a process known as chording."

Beginner is usually on an 8x8 or 9x9 board containing 10 mines, 
Intermediate is usually on a 16x16 board with 40 mines and 
expert is usually on a 30x16 board with 99 mines

Game construction:
    Field
        choose difficulty
        generate mines to field
        

    game loop
        show screen
        get button
            if left "open specific field"
                if bomb -> game over
                if near bomb -> show amount near mines
                if empty -> reveal empty and next near bombs
            if right "mark as bomb" or "unmark bomb"
        check result
            if bombs still unfound
                bombs unmarked/hidden -> continue
            if too many bombs marked, some empty still hidden and unmarked --> continue
            if all bombs found and marked ( or all other fields "open" ) --> game ends with victory

        draw screen

        
        

         

        