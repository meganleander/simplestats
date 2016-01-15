def mean(vals):
    assert type(vals) is list, 'wrong imput format'
    total = sum(vals)
    length = len(vals)
    return total/length

print(mean([2,4]))

print(mean("hello"))
