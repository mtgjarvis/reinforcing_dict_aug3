ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

results = {}

def add_vote(name, points):
    if name not in results:
        results[name] = points
    else:
        results[name] += points


for ballot in ballots:
    for key, value in ballot.items():
        if key == 'gold':
            add_vote(value, 3)
        elif key == 'silver':
            add_vote(value, 2)
        else:
            add_vote(value, 1)

print(results)
maximum = max(results, key=results.get)
print(f'{maximum} won with {results[maximum]} votes')