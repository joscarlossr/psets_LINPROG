def sum_digits(digits):
    return np.sum([int(d) for d in digits])


def is_valid_card(card_number):
    if not (isinstance(card_number, int)
       or (isinstance(card_number, str) and card_number.isnumeric())):
       return

    # Começando pelo penúltimo dígito e indo em direção ao primeiro,
    # multiplique cada dígito sim, dígito não, por 2
    reverse_alt_digits_seclast = str(card_number)[-2::-2]
    reverse_alt_digits_last = str(card_number)[::-2]

    times_2_alt_nums = [int(d)*2 for d in reverse_alt_digits_seclast]

    # Depois some os dígitos desses resultados
    # (atenção: somar os dígitos dos resultados nao os resultados)
    sum_num_digits = np.sum([(d if d <= 9 else (d-10)+1)
                            for d in times_2_alt_nums])

    # Adicione a soma dos dígitos dos resultados obtidos no passo anterior,
    #  à soma dos dígitos que não foram multiplicados por 2.
    sum_num_digits_from_last = sum_digits(reverse_alt_digits_last)

    result = sum_num_digits + sum_num_digits_from_last

    return result % 10 == 0


def get_card_type(card_number):
    if is_valid_card(card_number):
        if int(str(card_number)[:2]) in (34, 37) and len(str(card_number)) == 15:
            return f'AMEX\n'

        if int(str(card_number)[:2]) in (51, 52, 53, 54, 55)\
           and len(str(card_number)) == 16:
            return f'MASTERCARD\n'

        if str(card_number)[0] == str(4) and len(str(card_number)) in (13, 16):
            return f'VISA\n'

    return f'INVÁLIDO\n'


number = input("Número: ")
print(get_card_type(number), end='\n')
