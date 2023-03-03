def check(student_name, word):
    student_name = student_name.lower().replace('ё', 'е').replace(' ', '')
    word = word.lower().replace('ё', 'е')

    def full_check(student_name, word):
        if student_name == word:
            return True
        return False

    def part_check(student_name, word):
        if student_name[0:3] == word[0:3]:
            return True
        return False

    if full_check(student_name, word):
        return 2  # Полное совпадение
    elif part_check(student_name, word):
        return 1  # Частичное совпадение
    return False
