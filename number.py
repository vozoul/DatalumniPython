# test n°1 Datalumni Python
def isValid(number):
    digits = [int(d) for d in str(number)]
    # exclusion du nombre de digits de 2 minimum modification des condition de test (1 mini à 10 mini)
    # if len(digits) < 2:
    #     return False
    if 1 in digits or 7 in digits:
        return False
    if sum(digits) > 10:
        return False
    if (digits[0] + digits[1]) % 2 == 0:
        return False
    if digits[-2] != 4:
        return False
    if digits[-1] != len(digits):
        return False
    return True

def main():
    # remplacement de 1 à 10 dans le range puisque le nombre de 'digits' est suppérieur à 2
    for number in range(10, 1000):
        if isValid(number):
            mystery_number = number
            break

    print(f"Le nombre mystère est : {mystery_number}")

main()
