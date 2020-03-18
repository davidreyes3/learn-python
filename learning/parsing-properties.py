separator = "="
comment = "#"
keys = {}

with open('test.properties') as f:
    for line in f:
        if separator in line and comment not in line:
            name, value = line.split(separator, 1)
            keys[name.strip()] = value.strip()

print(keys)
