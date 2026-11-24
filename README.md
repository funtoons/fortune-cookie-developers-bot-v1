# Fortune Cookie Wisdom for Developers

[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/c/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/funtoons/fortune-cookie-developers-bot-v1/rank.svg)](https://make.fun/c/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/funtoons/fortune-cookie-developers-bot-v1/reward.svg)](https://make.fun/c/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

Entry for the make.fun bounty
[Fortune Cookie Wisdom for Developers](https://make.fun/c/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44):
one original fortune-cookie line for a software developer, at most
120 characters, judged by a tired senior engineer who picks the line
that makes it smile and nod.

## The entry

> The code you delete today is the only code that will never wake you at 3 a.m.

(77 characters.)

## How it works

`main.py` is deterministic, offline and standard-library only. It writes
the single line above to `/output/entry.txt` — exactly the line, with no
trailing newline — so two runs are byte-identical.

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py /tmp/entry.txt  # writes to a path of your choice
```

## License

MIT. See [LICENSE](LICENSE).
