

def BinaryCheck(value):
    try:
        if int(value, 2):
            return True
    except ValueError:
            return False
def xor(a,b):
    result = ""
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result = result + "0"
        else:
            result = result + "1"
    return result
def modulo2div(divident, divisor):
    div = len(divisor)
    temp = divident[0: div]
    while div < len(divident):
        if temp[0] == "1":
            temp = xor(divisor, temp) + divident[div]
        else:
            temp = xor("0" * div, temp) + divident[div]
        div += 1
    if temp[0] == "1":
        temp = xor(divisor, temp)
    else:
        temp = xor("0" * div, temp)
    checksum = temp
    return checksum

