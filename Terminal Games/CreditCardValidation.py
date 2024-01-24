from wsgiref import validate


def validation(C_num):
    def digits_od(n):
        return [int(d) for d in str(n)]
    digits = digits_od(C_num)
    odd_digi = digits[-1::-2]
    even_digi = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digi)
    for d in even_digi:
        checksum += sum(digits_od(d*2))
    return checksum % 10

if validation(input("Enter Num \n"))==0:
    print("valid")
else:
    print("invalid")