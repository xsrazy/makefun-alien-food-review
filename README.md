# One Star, Five Stars for the Food

[![make.fun](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/xsrazy/makefun-alien-food-review/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/xsrazy/makefun-alien-food-review/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

Entry for the [make.fun bounty "One Star, Five Stars for the Food"](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7): one sentence, at most 200 characters, in the voice of an alien tourist giving planet Earth a one-star review while still slipping in a real compliment about the food.

## Final entry (159 characters)

> Earth gets one star: the sky leaks without warning, the locals stare at my third eye, but the street dumplings alone are worth the interstellar parking ticket.

## Why this sentence

It won a head-to-head tournament of 10 candidates because it packs three distinctively alien observations into one breath — rain reframed as "the sky leaks", being stared at for having a third eye, and food priced in "the interstellar parking ticket" — so the voice is unmistakably an outsider's and the turn to the dumplings lands as a real compliment, not a throwaway "but the food was good".

## How it works

`main.py` (Python standard library only, no network, deterministic) validates the sentence against the gate — non-blank, at most 200 characters, exactly one sentence — then writes it as UTF-8 to `/output/entry.txt`, creating `/output` if needed and setting the directory to mode 0755 and the file to mode 0644. For a local test run, set `ENTRY_OUTPUT_DIR` to a temporary directory:

```sh
ENTRY_OUTPUT_DIR=/tmp/alien-food-test python3 main.py
cat /tmp/alien-food-test/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
