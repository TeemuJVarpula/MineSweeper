# MineSweeper
Minesweeper game with python
"
Pelaaja klikkaa hiiren vasemmalla näppäimellä paljastamattomia ruutuja: jos ruudussa on miina, se räjähtää ja peli päättyy. Jos ruudussa ei ole miinaa, ruudussa näkyy, monessako ruudun kahdeksasta naapuriruudusta on miina.

Mikäli klikatun ruudun yhdessäkään naapuriruudussa ei ole miinaa, peli paljastaa ensin kaikki siihen yhteydessä olevat ruudut, joiden naapurissa ei myöskään ole miinaa, sekä lisäksi tämän paljastetun alueen reunalla olevat ruudut, joiden naapurissa on miina. Tämä ei helpota mutta nopeuttaa peliä etenkin suurella laudalla, jossa on vähän miinoja, koska "nollaruutuja" ei tarvitse klikkailla yksitellen.

Oikealla näppäimellä pelaaja voi merkitä lipulla paljastamattoman ruudun, jossa päättelee olevan miinan. Kun kaikki miinattomat ruudut on paljastettu, pelaaja on onnistunut ja hänen tuloksensa on käytetty aika.

In Minesweeper, hidden mines are scattered throughout a board, which is divided into cells. Cells have multiple possible states:

Unopened tiles (cover the board at the start of the game, can also be made by removing flags)
Numbered tiles (can show 1-8)
Blank tiles (no mines are on the diagonal/adjacent to the tile)
Flagged tiles (appear after right-clicking an unopened tile)
(?) Question marked tiles (appear after right-clicking a flagged tile; only exists in certain implementations)

An unopened cell is blank and clickable, while an opened cell is exposed. Flagged cells are unopened cells marked by the player to indicate a potential mine location; some implementations make flagged cells unopenable to reduce the risk of uncovering a suspected mine.

A player selects a cell to open it. If a player opens a cell containing a mine, the game ends in a loss. Otherwise, the opened cell displays either a number, indicating the number of mines diagonally and/or adjacent to it, or a blank tile (sometimes shown as a 0), and all adjacent cells will automatically be opened. This may cause a chain reaction; any blank tiles opened by other blank tiles open the surrounding tiles too. Players can also flag a cell, visualised by a flag being put on the tile, to denote that they believe a mine to be in that place. Flagged cells are still considered unopened, and may be unflagged. In some versions of the game, when the number of adjacent mines is equal to the number of adjacent flagged cells, all adjacent non-flagged unopened cells can be opened by both left and right-clicking (regardless of if any tiles are mines or not), a process known as chording."
