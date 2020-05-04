import math


def int_to_bit(num):
    arr = []
    for i in range(16):
        arr.append(num >> i & 1)
    arr.reverse()
    return arr


def bin_to_int(list_bits):
    x = 0
    for i in range(len(list_bits)):
        x += list_bits[i] * 2 ** (len(list_bits) - i - 1)
    return x


def check_if_even(num):
    number_of_repeat = int(math.sqrt(len(int_to_bit(num))))
    list_of_bites = int_to_bit(num)
    for i in range(number_of_repeat):
        size_of_returns_list = int(len(list_of_bites) / 2)
        list_of_bites = divide_and_check([], list_of_bites, size_of_returns_list, True)
    return list_of_bites[0]


def divide_and_check(returns_list, list_bit, size_of_returns_list, is_stop):
    left_part = []
    right_part = []
    for i in range(int(len(list_bit) / 2)):
        left_part.append(list_bit[i])
        right_part.append(list_bit[int(len(list_bit) / 2) + i])
    if int(len(left_part)) != 1:
        divide_and_check(returns_list, left_part, size_of_returns_list, False)
    if int(len(right_part)) != 1:
        divide_and_check(returns_list, right_part, size_of_returns_list, False)
    if int(len(right_part)) == 1 and int(len(left_part)) == 1:
        returns_list.append(check(left_part[0], right_part[0]))
    if int(len(returns_list)) == size_of_returns_list and is_stop:
        return returns_list


def check(x, y):
    return 0 if x == y else 1


def inverse(list_of_bits):
    new_list = []
    for i in list_of_bits:
        new_list.append(1 if i == 0 else 0)
    return new_list


def get_inverse_code(list_of_original_bits):
    if check_if_even(number):
        return list_of_original_bits + inverse(list_of_original_bits)
    else:
        return list_of_original_bits + list_of_original_bits


def get_original_message_form_inverse_code(list_of_bits):
    original_list = []
    for i in range(int(len(list_of_bits) / 2)):
        original_list.append(list_of_bits[i])
    return original_list


def is_message_broken(list_of_bits):
    original_list = []
    inverse_list = []
    state = False
    for i in range(int(len(list_of_bits) / 2)):
        original_list.append(list_of_bits[i])
        inverse_list.append(list_of_bits[int(len(list_of_bits) / 2) + i])
    if check_if_even(number):
        for i in range(int(len(original_list))):
            if original_list[i] == inverse(inverse_list):
                state = True
            else:
                state = False
    else:
        for i in range(int(len(original_list))):
            if original_list[i] == inverse_list:
                state = True
            else:
                state = False
    return state


number = 732
print("number == " + str(number))
list_of_bit = int_to_bit(number)
print("list_of_data before adding inverse code == " + str(list_of_bit))
print("even bit == " + str(check_if_even(number)))
print("list_of_data after adding inverse code == " + str(get_inverse_code(int_to_bit(number))))
print("list_of_data after dividing message == " + str(get_original_message_form_inverse_code(get_inverse_code(int_to_bit(number)))))
print("is message broken == " + str(is_message_broken(get_inverse_code(int_to_bit(number)))))
