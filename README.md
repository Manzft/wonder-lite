# Wonder Lite

A high-performance, optimized 2D demake of *Super Mario Bros. Wonder*, built from
scratch in **Godot 4.7.2** with hand-rotoscoped, pre-rendered sprites and original
artwork.

> **Status: pre-production.** The repository currently contains a bare Godot
> project. Milestone 1 (boot -> loading -> title) is the first playable slice.

## Progress

<!-- progress:start -->

```text
Alpha 0.1.0   [█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   3%  1/39 tasks
Main courses  [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   0%  0/68 courses
```

<!-- progress:end -->

Both bars are live: tick a task in the collapsible lists below (GitHub saves the
change) and run `python3 tools/progress.py` to refresh the percentages.

- **Alpha 0.1.0** tracks the first playable slice: boot, loading, title, user
  select and a finishable Level 1.
- **Main courses** tracks the regular courses of the original campaign, i.e.
  enough content to say the game can be played from start to finish. It excludes
  collectibles, playable characters, Badge Challenges, Break Time and KO Arena
  stages, and the hidden Special World. Course counts are approximate and may
  change once the demake's course list is finalized.

<details>
<summary><b>Alpha 0.1.0 - first playable slice</b></summary>

<!-- progress:alpha:start -->

### M0 - Skeleton

- [x] Repository, Apache-2.0 license and README
- [ ] `project.godot`: 1920x1080 viewport, nearest filter, input map, collision layers
- [ ] Autoload skeleton (`Game`, `SceneFlow`, `Audio`, `Settings`, `Events`)
- [ ] Folder structure and placeholder scenes

### M1 - Loading screen

- [ ] Loading visuals: flower animation, progress bar, rotating tips
- [ ] `SceneFlow`: threaded loading, real progress, minimum display time, fades

### M2 - Title screen

- [ ] Layout with placeholder concept art and logo
- [ ] Blinking "Press START" prompt and confirm input

### M3 - User select

- [ ] Six-slot layout with placeholder avatars
- [ ] Placeholder "create user" dialog
- [ ] Focus navigation (keyboard, gamepad, mouse)
- [ ] Selecting a slot loads Level 1

### M4 - Level greybox

- [ ] W1-1 layout built as `TileMapLayer` terrain
- [ ] Camera with dead zone, look-ahead and level bounds
- [ ] Player locomotion: walk, run, skid, jump, crouch
- [ ] Player animation state machine

### M5 - Level objects

- [ ] `?` blocks, Brick Blocks and bump/break feedback
- [ ] Coins and flower coins
- [ ] Pipes: enter, travel between ends, sideways exits
- [ ] Goomba: walk, turn, squash
- [ ] Sleeping Goomba: idle, wake, walk

### M6 - Power-ups

- [ ] Small / Super / damage states
- [ ] Elephant Fruit: transform and trunk attack
- [ ] Trunk water and refilling fountains

### M7 - Wonder effect

- [ ] Wow Buds: hit, spawn blocks and coins
- [ ] Wonder Flower trigger, pipe eyes and bobbing pipes
- [ ] Inchworm Pipe
- [ ] Wonder Seed pickup and effect end

### M8 - Gameplay loop

- [ ] HUD: coins, seeds, lives, timer
- [ ] Checkpoint flag and respawn point
- [ ] Death, respawn and pit detection
- [ ] Goal Pole and Course Clear screen
- [ ] Talking Flowers with proximity quotes
- [ ] Localization EN + ES
- [ ] Audio buses and SFX/music hooks

### M9 - Art pass

- [ ] Player sprite set (all states and forms)
- [ ] Enemy, block and prop sprites
- [ ] Tileset and background art
- [ ] UI art: title, loading, HUD, course clear


<!-- progress:alpha:end -->

</details>

<details>
<summary><b>Main courses - regular campaign levels</b></summary>

<!-- progress:courses:start -->

### Pipe-Rock Plateau

- [ ] Welcome to the Flower Kingdom!
- [ ] Piranha Plants on Parade
- [ ] Scram, Skedaddlers!
- [ ] Bulrush Coming Through!
- [ ] Here Come the Hoppos
- [ ] Rolla Koopa Derby
- [ ] Swamp Pipe Crawl
- [ ] Angry Spikes and Sinkin' Pipes
- [ ] Bulrush Express
- [ ] Sproings in the Twilight Forest
- [ ] Cosmic Hoppos
- [ ] Pipe-Rock Plateau Palace

### Fluff-Puff Peaks

- [ ] Outmaway Valley
- [ ] Pokipede Pass
- [ ] Condarts Away!
- [ ] Pole Block Passage
- [ ] Up 'n' Down with Puffy Lifts
- [ ] Jump! Jump! Jump!
- [ ] Countdown to Drop Down
- [ ] Cruising with Linking Lifts
- [ ] Fluff-Puff Peaks Flying Battleship
- [ ] Fluff-Puff Peaks Palace

### Shining Falls

- [ ] The Hoppycat Trial: Hop, Hop, and Awaaay
- [ ] The Anglefish Trial: Ready, Aim, Fly!
- [ ] The Midway Trial: Hop to It
- [ ] The Sharp Trial: Launch to Victory
- [ ] The Sugarstar Trial: Across the Night Sky
- [ ] The Final Trial: Zip Track Dash

### Sunbaked Desert

- [ ] Armads on the Roll
- [ ] The Desert Mystery
- [ ] Rolling-Ball Hall
- [ ] Ninji Jump Party
- [ ] Bloomps of the Desert Skies
- [ ] Valley Fulla Snootles
- [ ] Color-Switch Dungeon
- [ ] Secrets of Shova Mansion
- [ ] Flight of the Bloomps
- [ ] Sunbaked Desert Palace

### Fungi Mines

- [ ] Upshroom Downshroom
- [ ] Taily's Toxic Pond
- [ ] Light-Switch Mansion
- [ ] Beware of the Rifts
- [ ] An Uncharted Area: Wubba Ruins
- [ ] Another Uncharted Area: Swaying Ruins
- [ ] A Final Uncharted Area: Poison Ruins
- [ ] Fungi Mines Palace

### Deep Magma Bog

- [ ] Where the Rrrumbas Rule
- [ ] Raarghs in the Ruins
- [ ] Pull, Turn, Burn
- [ ] Hot-Hot Hot!
- [ ] Wavy Ride through the Magma Tube
- [ ] Dragon Boneyard
- [ ] Deep Magma Bog Flying Battleship
- [ ] Deep Magma Bog Palace

### Petal Isles

- [ ] Leaping Smackerel
- [ ] Robbird Cove
- [ ] Blewbird Roost
- [ ] Downpour Uproar
- [ ] Jewel-Block Cave
- [ ] Gnawsher Lair
- [ ] Maw-Maw Mouthful
- [ ] Muncher Fields
- [ ] Petal Isles Flying Battleship
- [ ] Missile Meg Mayhem
- [ ] High-Voltage Gauntlet
- [ ] Evade the Seeker Bullet Bills!
- [ ] KnuckleFest Bowser's Blazing Beats
- [ ] The Final Battle! Bowser's Rage Stage


<!-- progress:courses:end -->

</details>

---

## 1. What this project is

`Wonder Lite` recreates the *feel* and the *flow* of Super Mario Bros. Wonder in a
lightweight 2D engine, without reusing a single asset from the original game.

Every sprite, tile, background and sound is produced by this project:

- Sprites are **rotoscoped**: reference animations are recorded from emulated
  gameplay, traced/re-drawn frame by frame, and rendered as pre-rendered 2D art.
- Backgrounds are removed manually, per frame.
- Animations are authored at 1080p and packaged into texture atlases.

The result is a demake in the same spirit as a fan re-imagining: recognizable
gameplay language, entirely original assets.

> **AI-assisted, human-reviewed.** This project is developed with AI assistance.
> AI is used for scaffolding, boilerplate and implementation drafts, but **every
> line of code that lands in the repository is reviewed by a human**, and all
> physics, menus, animations and gameplay feel are tuned and polished by hand.
> Nothing generated by AI is shipped unreviewed.

This is a **non-commercial fan project**. It is not affiliated with, endorsed by,
or sponsored by Nintendo.

---

## 2. Short-term goals

1. **Loading screen** - shown on first boot and on every scene transition.
2. **Title screen** - concept art, logo, blinking "Press START" prompt.
3. **User select screen** - six placeholder profile slots, styled after the
   original, with no real profile system behind them.
4. **Selecting a placeholder** transitions straight into Level 1.
5. **A complete, finishable Level 1** - a faithful-but-not-pixel-exact recreation
   of the original *Welcome to the Flower Kingdom!*

Goal 5 is the real milestone: it forces the core engine work (player controller,
animation state machine, tilemap collision, blocks, enemies, power-ups, camera,
HUD, audio hooks, save-point flags and the Wonder effect) to exist at once.

### Non-goals (for this slice)

- World map / level progression
- Local co-op (the player controller is written to allow it later)
- Badges and `!` blocks
- Sub-areas, hidden blocks, 10-flower coins, Super Star
- Real save profiles or persistent progress
- Mobile builds (the render path is prepared for them, but none is produced yet)
- Networking, replays, editor tooling inside the game

---

## 3. Tech stack

| Item | Choice |
|---|---|
| Engine | Godot 4.7.2 stable |
| Renderer | GL Compatibility (desktop first, mobile-friendly) |
| Physics | Built-in 2D physics (`CharacterBody2D` + `TileMapLayer` collision) |
| Language | GDScript |
| Audio | Godot `AudioStreamPlayer` + bus layout (Master / Music / SFX) |
| Localization | Godot CSV translations (`en`, `es`) |

### Resolution and frame

- Internal viewport: **1920x1080**, aspect **16:9**.
- Tile size: **128 px** -> 15 tiles across, ~8.4 tiles vertically, matching the
  original game's framing.
- Stretch mode `canvas_items`, aspect `keep` (letterbox on non-16:9 displays).
- Texture filter: **nearest** everywhere; the art is authored at native scale, so
  there is no downscaling inside the base resolution.
- Mobile (later): render into a `SubViewport` at 0.5x (960x540) and upscale. The
  art does not change; only the render scale does.

---

## 4. Art direction and asset pipeline

### Style

Pre-rendered 2D: soft shapes, painted gradients and lighting, but with a
restrained palette and flat, readable silhouettes at gameplay scale. Think
"modern 2.5D art flattened into crisp 2D", not pixel art.

### Production loop

1. Record reference footage from emulated gameplay.
2. Pick and stabilize frames (`ffmpeg`).
3. Rotoscope / re-draw each frame over the reference.
4. Remove the background manually.
5. Normalize the frame: consistent canvas, pivot at **feet center**, baseline on
   the last visible row.
6. Export PNG frames + an animation manifest.
7. Pack atlases and generate `SpriteFrames` resources.

Steps 2, 5, 6 and 7 are scripted in `tools/`:

```
tools/
  extract_frames.sh      # ffmpeg: video -> PNG sequence at a fixed fps
  build_atlas.gd         # headless Godot: pack PNGs into atlases
  build_spriteframes.gd  # headless Godot: manifest -> .tres SpriteFrames
  check_sprites.gd       # validates naming, size, pivot and empty frames
```

### Asset conventions

- Path: `assets/art/<entity>/<state>/<state>_<##>.png`
- Animation manifest: `assets/art/<entity>/<state>/<state>.json`
  (fps, loop, pivot, frame order, hitboxes)
- One atlas per entity family, not one giant atlas, so texture memory stays
  predictable and mobile-friendly.
- All sprites are authored at 1080p; no per-platform duplicates.

### Animation authoring

- Animation frame rate: 12-24 fps depending on the action (the original uses
  hand-drawn cadence, not 60 unique drawings).
- Every animated entity is driven by an animation state machine
  (`Idle / Walk / Run / Jump / Fall / Skid / Crouch / ...`) that never hardcodes
  frame names; it asks the `SpriteFrames` resource.

---

## 5. Architecture

### Autoloads

| Autoload | Responsibility |
|---|---|
| `Game` | Global state: current user slot, coins, seeds, lives, timer reset |
| `SceneFlow` | Async scene loading with progress, minimum display time, fade in/out |
| `Audio` | Bus setup, music crossfade, SFX pool, volume settings |
| `Settings` | Language, volumes, render scale, keybinds; persisted in `user://` |
| `Events` | Small signal hub (coin collected, enemy stomped, seed collected, ...) |

### Scene flow

```
Boot (bootstrap, no visuals)
  -> Loading (flower animation + progress bar + rotating tip)
  -> Title ("Press START")
  -> UserSelect (6 placeholders)
  -> Loading
  -> Level 1
  -> CourseClear
  -> Title
```

`SceneFlow` instantiates the loading overlay as a CanvasLayer that survives the
swap, loads the next scene with `ResourceLoader.load_threaded_request`, blocks
for a configurable minimum time (so fast loads don't flicker) and exposes a real
percentage.

### Directory layout

```
res://
  assets/
    art/            # source PNGs + manifests (per entity/state)
    atlases/        # generated atlases (git-ignored)
    audio/          # music and SFX provided by the project owner
    fonts/
    ui/             # title art, logo, loading flower, menu frames
  scenes/
    boot/
    loading/
    title/
    user_select/
    level/          # level_01.tscn, tilemaps, parallax
    player/
    enemies/        # goomba/, goomba_sleeping/
    blocks/         # question_block, brick_block, pipe, wow_bud, ...
    items/          # coin, elephant_fruit, mushroom, wonder_flower, wonder_seed
    effects/        # wonder effect, particles, screen shake
    ui/             # HUD, course clear, pause
  scripts/
    autoload/
    components/     # reusable nodes (hurtbox, item bobbing, water spray, ...)
  tools/
  locale/           # en.csv, es.csv
  tests/            # headless smoke tests (optional, later)
```

### Player controller

- `CharacterBody2D`, fixed 60 Hz physics, tuned by hand for *game feel*.
- Tunable constants live in an exported `PlayerTuning` resource, expressed in
  tiles and tiles/second so the numbers stay readable.
- Input is read through an `InputDevice` abstraction (`keyboard` / `pad_0..3`),
  so co-op only needs a second instance and a camera target list.
- States: idle, walk, run, skid, crouch, jump, fall, land, hurt, transform,
  pipe enter/exit, goal.
- Pickup/transform, damage, and death are handled by a small state machine that
  freezes input for the animation duration.

### Level structure

- `level_01.tscn` is a composition root: `TileMapLayer`s for terrain, pipes and
  decorative props, plus entity scenes placed as children.
- Camera: `Camera2D` with a dead zone and a forward look-ahead, clamped to level
  bounds; vertical follow softened to avoid seasick motion.
- Collision layers: `terrain`, `player`, `enemy`, `item`, `block`, `hazard`,
  `trigger`.
- Checkpoint flag swaps the respawn point and restarts the timer from a fixed
  value without reloading the scene.

---

## 6. Level 1 - "Welcome to the Flower Kingdom!"

A faithful, approximately-measured recreation of the original first course
(Pipe-Rock Plateau, star difficulty, 2 Wonder Seeds). Layout, rhythm and order of
events follow the original; exact block positions are reconstructed by eye and
adjusted during playtesting.

### Beats included

1. Opening: Wonder Flower-shaped bush, first Talking Flower, first sleeping
   Goomba on flat ground.
2. Wow Bud that summons Brick Blocks up a tree, with coins and a flower coin.
3. Pipe with a Goomba on top; entering it releases a Wow Bud that spawns coins
   around the `?` Block containing the first **Elephant Fruit**.
4. Fountains that refill the elephant trunk.
5. Downhill section with walking and sleeping Goombas and dry Wow Buds.
6. **Checkpoint Flag**, followed by a sideways pipe with a Wow Bud inside.
7. Wow Bud that raises a row of pipes; the **Wonder Flower** sits in the middle.
8. Wonder effect: the pipes grow eyes and bob up and down; a sideways pipe
   becomes an **Inchworm Pipe** that squirms and slithers into a pit.
9. **Wonder Seed** on top of the last fountain; touching it ends the effect.
10. Final Wow Bud that raises pipes to reach the top of the **Goal Pole**.

### Entities required

| Type | Objects |
|---|---|
| Enemies | Goomba (walk, squash, turn), Sleeping Goomba (wake on proximity/hit) |
| Blocks | `?` block, Brick Block (break, bump), pipe (enterable), cloud/semisolid |
| Items | Coin, flower coin, Elephant Fruit, Super Mushroom, Wonder Flower, Wonder Seed |
| World | Wow Bud (hit -> spawn blocks/coins), fountain, slope terrain, tree |
| Characters | Talking Flower (proximity quotes), Goal Pole |
| Player | Small, Super, Elephant (trunk attack, trunk water, heavy stomp) |

### Wonder effect implementation

- A `WonderState` node owns the effect lifecycle: `inactive -> triggered ->
  active -> ending`, with a global `wonder_active` flag on `Events` used by
  entities that change behaviour.
- Pipes are separate scenes that support two visual modes (plain / eyes + bob)
  driven by a shared `Wonderable` interface.
- The Inchworm Pipe is a scripted `Path2D` follower with its own collision body;
  it is not a static pipe with a different animation.
- During the effect: palette shift, music layer change, and HUD seed counter.

---

## 7. Screens

### Loading

- Black background, animated flower (looping, low frame count), progress bar
  driven by real load progress, and a rotating gameplay tip.
- Full-screen, input-blocked, survives scene swaps, minimum 0.8 s display time.
- Also used for the first boot, so there is no "flash of empty screen".

### Title

- Key/concept artwork, project logo, subtle parallax or drifting particles.
- Blinking "PRESS START" prompt; gamepad `Start` and any keyboard confirm key.
- Optional attract mode is out of scope for now.

### User select

- Six slots in the original's layout; each with a placeholder avatar and an
  empty name. Creating a user is a no-op placeholder dialog.
- Clicking a slot sets `Game.current_slot` (in memory only) and continues.
- Keyboard/gamepad navigation with focus, not just mouse.

### Course Clear

- Seed and coin count-up, "Course Clear!" banner, then press to return to the
  title.

### HUD

- Coin counter, seed counter, lives, timer, and the active power-up.
- Anchored to a 1920x1080 safe area, scales with the viewport without offsetting
  the game camera.

---

## 8. Controls

| Action | Keyboard | Gamepad |
|---|---|---|
| Move | Arrows / WASD | Left stick / D-pad |
| Jump | `Z` / `Space` | `A` (south) |
| Run / Trunk | `X` / `Shift` | `X` (west) / `B` |
| Crouch | `S` / `Down` | `B` (east) / D-pad down |
| Pause | `Esc` / `Enter` | `Start` |
| Confirm | `Enter` / `Space` | `A` |

All bindings live in the `InputMap` and are remappable later from Settings.

---

## 9. Localization

- Godot CSV translation pipeline in `locale/`: `en.csv`, `es.csv`.
- All UI strings go through `tr()` from the first commit; no hardcoded labels.
- On-screen dialogue (Talking Flowers, tips) uses the same keys, so adding a
  language is a data change only.
- Level layout never contains translatable text; text lives in entity data.

---

## 10. Roadmap

| Milestone | Content | Done when |
|---|---|---|
| **M0** | Project skeleton: viewport, layers, autoloads, folder structure, git hygiene | Game boots to a stub scene |
| **M1** | Loading screen + `SceneFlow` (async, progress, min time, fades) | Any scene transition shows real progress |
| **M2** | Title screen with placeholder art, blinking prompt, input navigation | START leads to user select |
| **M3** | User select with 6 placeholders, focus navigation, settings persistence of language/volume | Choosing a slot loads Level 1 |
| **M4** | Greybox Level 1: tilemap terrain, camera, player locomotion (walk/run/jump/crouch), debug overlay | You can traverse the whole level with box art |
| **M5** | Blocks, coins, pipes and Goombas (walk + sleeping) | Level is playable start to Goal Pole |
| **M6** | Power-ups: Super Mushroom, Elephant Fruit, transform/damage states | Trunk attack and water work |
| **M7** | Wonder Flower: pipe eyes, bobbing pipes, Inchworm Pipe, seed | Effect can be triggered and completed |
| **M8** | HUD, checkpoint, timer, death/respawn, Course Clear | Level is finishable with a full loop |
| **M9** | Art pass: replace every placeholder with final sprites/audio | Ship-quality vertical slice |

Menus come first (M1-M3), then the level is built greybox-first and art is
dropped in last, so gameplay is never blocked by asset production.

---

## 11. Conventions

- **Language:** code, comments, commit messages and documentation in English.
- **Commits:** Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`,
  `refactor:`), one logical change per commit.
- **README:** kept up to date with every functional change; stale sections get
  fixed in the same commit that breaks them.
- **GDScript style:** typed variables and function signatures where practical,
  `snake_case` for files/variables, `PascalCase` for classes/scenes, signals in
  past tense (`coin_collected`).
- **Nodes:** prefer composition of small scenes over deep inheritance; every
  repeated behaviour becomes a component under `scripts/components/`.
- **No magic numbers in gameplay:** tuning values live in exported resources or
  a single constants file per system.
- **Progress bars:** the two bars at the top of this README are generated from
  the task lists by `python3 tools/progress.py`; run it after ticking a task so
  the percentages stay honest.

---

## 12. Licensing

- **Source code:** Apache License 2.0 (see `LICENSE`).
- **Original art, audio and design assets produced for this project:**
  CC BY-NC-SA 4.0 - share alike, non-commercial.
- **No assets from the original game are included.** Reference footage is used
  only as a tracing guide during production and is never shipped.
- *Super Mario Bros. Wonder*, Mario and related characters are trademarks of
  Nintendo. This project is a non-commercial fan work, unaffiliated with
  Nintendo.

---

## 13. Open items

- Final tip texts for the loading screen (EN + ES).
- Audio files (music loop, SFX set) - provided by the project owner.
- Exact W1-1 measurements: distances are currently reconstructed by eye and will
  be tuned in playtests.
- Whether the elephant trunk water is a limited resource or infinite (original:
  refilled by fountains).
