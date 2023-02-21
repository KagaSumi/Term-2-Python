from string import ascii_uppercase


def check_plate(plate: str) -> bool:
    temp = plate.split("-")
    if len(temp) != 3:
        return False
    valid_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for number in temp[0]:
        if number not in valid_num:
            return False
    for letter in temp[1]:
        if letter not in ascii_uppercase:
            return False
    for number in temp[2]:
        if number not in valid_num:
            return False
    return True


def find_next_plate(current_plate: str, more: int = 1):
    """ Systematically breaks the entire plate into 3 parts and checks if each of them has reached the upper limit of the plate valid numbers
    if they have then we increment the higher order value and continue until we either reach the target plate or break from a error"""
    plate_pieces = current_plate.split("-")
    upper_bound = ['99', 'ZZ', 'Z', '9']
    counter = 0
    if not isinstance(more, int):
        raise OverflowError
    if check_plate(current_plate):
        while counter < more:
            if plate_pieces[0] == '99' and plate_pieces[1] == 'ZZ' and plate_pieces[2] == '99':
                raise OverflowError

            if plate_pieces[2] not in upper_bound:
                additional = 0
                if plate_pieces[2][1] in upper_bound:
                    additional += 1
                plate_pieces[2] = str(int(plate_pieces[2])+1 + additional)
            else:
                plate_pieces[2] = '11'
                if plate_pieces[1] not in upper_bound:
                    if plate_pieces[1][1] not in upper_bound:
                        plate_pieces[1] = plate_pieces[1][0] + \
                            chr(ord(plate_pieces[1][1]) + 1)
                    else:
                        plate_pieces[1] = chr(
                            ord(plate_pieces[1][0]) + 1) + 'A'
                else:
                    plate_pieces[1] = 'AA'
                    if plate_pieces[0] not in upper_bound:
                        additional = 0
                        if plate_pieces[0][1] in upper_bound:
                            additional += 1
                        plate_pieces[0] = str(
                            int(plate_pieces[0])+1 + additional)
                    else:
                        raise OverflowError
            counter += 1
    return f'{plate_pieces[0]}-{plate_pieces[1]}-{plate_pieces[2]}'


def main():
    current_plate = "11-AA-11"
    print(find_next_plate(current_plate, 81))


if __name__ == "__main__":
    main()
