import re

demon_name = input()
demons = {}
regex = r'([^, ]+)+'
hp_regex = r'([^0-9+*/.,-])'
damage_regex = r'(-?\d+[.]?\d*)'
symbols_regex = r'[*/]{1}'

matches = re.findall(regex, demon_name)
for name in matches:
    hp = 0
    damage = 0
    symbols = []
    hp_matches = re.findall(hp_regex, name)
    for hp_points in hp_matches:
        hp += int(ord(hp_points))
    damage_matches = re.findall(damage_regex, name)
    for dmg in damage_matches:
        damage += float(dmg)
    symbol_matches = re.findall(symbols_regex, name)
    for s in symbol_matches:
        symbols.append(s)
    for s in symbols:
        if s == "*":
            damage *= 2
        elif s == "/":
            damage /= 2

    demons[name] = {"HP": int(hp), "Damage": float(damage)}

sorted_demons = sorted(demons.items())
for k, v in sorted_demons:
    print(f"{k} - {v['HP']} health, {v['Damage']:.2f} damage")
