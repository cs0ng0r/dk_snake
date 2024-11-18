# Gyurcsány Ferenc Snake Game

Ez a projekt egy egyszerű Snake játék, amelyben Gyurcsány Ferenc feje a kígyó, és az ételek DK logók. A játék Pygame könyvtárral készült, és egyedi képeket és hátteret használ.

## Funkciók

- **Egyedi megjelenés**: A kígyó feje és az étel saját képekkel jelenik meg.
- **Dinamikus sebesség**: A játék sebessége növekszik a pontszám emelkedésével.
- **Rugalmas méretek**: A rács mérete arányos a képernyő felbontásával.
- **Játék vége képernyő**: A játék vége után az eredmény megjelenik.

---

## Telepítés

### Követelmények

- Python 3.8 vagy újabb
- Pygame könyvtár

### Lépések

1. Klónozd a repót:
   ```bash
   git clone https://github.com/cs0ng0r/gyurcsany-snake-game.git
   cd gyurcsany-snake-game
   ```

2. Telepítsd a szükséges könyvtárat:
   ```bash
   pip install pygame
   ```

3. Helyezd el a következő fájlokat a projekt könyvtárában:
   - **`head.png`**: A kígyó fejéhez használt kép.
   - **`dk.png`**: Az ételhez használt kép.
   - **`gradient.jpeg`**: A háttérkép.

4. Futtasd a játékot:
   ```bash
   python snake_game.py
   ```

---

## Használat

### Irányítás

- **Fel**: Nyíl felfelé
- **Le**: Nyíl lefelé
- **Balra**: Nyíl balra
- **Jobbra**: Nyíl jobbra

A cél minél több DK logót összegyűjteni anélkül, hogy a kígyó ütközne a falakba vagy önmagába.

---

## Fájlok

- **`snake_game.py`**: A játék fő kódja.
- **`head.png`**: A kígyó fejének grafikája.
- **`dk.png`**: Az étel grafikája.
- **`gradient.jpeg`**: A játék háttérképe.

---

## Játék Képernyőkép

> (Helyezz ide egy képernyőképet a játékról, amely a játékot akció közben mutatja.)

---

## Hozzájárulás

Ha szeretnél hozzájárulni a projekthez, nyugodtan nyiss egy issue-t vagy küldj pull requestet. 

---

## Licenc

Ez a projekt [MIT Licenc](LICENSE) alatt érhető el.
