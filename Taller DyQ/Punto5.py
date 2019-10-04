

def suma(num):
    acum = 0
    for i in range(len(num)):
        acum += int(num[i])
    return acum


def main():
    x = int(input('Numero X: '))
    num_actual = 1
    num_bits_acum = 0
    while True:
        bits = suma(bin(num_actual)[2:])
        num_bits_acum += bits
        if num_bits_acum >= x:
            break
        num_actual += 1
    print(num_actual)

main()
