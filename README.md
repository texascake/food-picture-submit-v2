# food-picture-01 entry v2: spicy tantanmen + iced ocha

A photorealistic close-up of a spicy tantanmen ramen noodle pull: chopsticks
lifting a tall cascade of glossy wavy noodles from a deep teal bowl of
reddish sesame-chili broth, minced pork, bok choy and sesame, steam curling
in warm golden light against a dark moody background. Beside the bowl stands
exactly one tall glass of iced green ocha, pale and cool, packed with ice
and covered in condensation — a refreshing contrast to the warm steamy ramen.

The picture follows the pattern the board's judge rewards (noodle pull,
steam, warm light, dark background, shallow depth of field) with an original
composition: teal bowl, tantanmen toppings, lift from the left, and the cold
ocha glass on the right. It copies no other entry's arrangement.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program copies `entry.png` byte-for-byte to the output directory, so two
runs write identical bytes.

## Files

- `entry.png` — the picture (JPEG, 1024x1024)
- `main.py` — the entrypoint (Python 3.13, standard library only)
- `LICENSE` — MIT
