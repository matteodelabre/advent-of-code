import re

fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
data = re.compile(r'([a-z]{3}):(\S+)')

def maybe_int(val):
    try:
        return int(val)
    except ValueError:
        return 0

def validate_byr(val):
    return maybe_int(val) >= 1920 and maybe_int(val) <= 2002

def validate_iyr(val):
    return maybe_int(val) >= 2010 and maybe_int(val) <= 2020

def validate_eyr(val):
    return maybe_int(val) >= 2020 and maybe_int(val) <= 2030

hgt_format = re.compile(r'(\d+)(cm|in)')

def validate_hgt(val):
    results = hgt_format.fullmatch(val)

    if not results:
        return False

    value, unit = results.groups()

    if unit == 'cm':
        return maybe_int(value) >= 150 and maybe_int(value) <= 193
    elif unit == 'in':
        return maybe_int(value) >= 59 and maybe_int(value) <= 76

    return False

hcl_format = re.compile(r'#[0-9a-f]{6}')

def validate_hcl(val):
    return hcl_format.fullmatch(val) is not None

def validate_ecl(val):
    return val in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

pid_format = re.compile(r'[0-9]{9}')

def validate_pid(val):
    return pid_format.fullmatch(val) is not None

validators = {
    'byr': validate_byr,
    'iyr': validate_iyr,
    'eyr': validate_eyr,
    'hgt': validate_hgt,
    'hcl': validate_hcl,
    'ecl': validate_ecl,
    'pid': validate_pid,
}

current_fields = set()
current_valid = True
count_valid = 0

try:
    while True:
        line = input().strip()

        if not line:
            if fields <= current_fields and current_valid:
                count_valid += 1

            current_fields = set()
            current_valid = True
        else:
            for field, value in data.findall(line):
                current_fields.add(field)

                if field in validators and not validators[field](value):
                    current_valid = False
except EOFError:
    pass

if fields <= current_fields and current_valid:
    count_valid += 1

print(count_valid)
