with open('Subject.txt', encoding='utf-8') as f:
    subjects = {}
    for subject in f.readlines():
        sum_sub = 0
        subject = subject.split(":   ")
        for el in subject[1].split("  "):
            try:
                sum_sub += int(el[:el.find("(")])
            except ValueError:
                continue
        subjects[subject[0]] = sum_sub
print(f'Полученный словарь:\n{subjects}')
