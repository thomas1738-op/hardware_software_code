def celsius_to_fahr(temp):
    temp=9/5*temp + 32
    return("the freezing point of water in fahrenheit is:{}".format(temp))

def kelvins_to_celsius(temp_kelvins):
    temp=temp_kelvins - 273.15
    return("the absolute freezing point of water in celsius is:{}".format(temp))

def main():
    temp=0
    freezing_point=celsius_to_fahr(temp)
    print(freezing_point)

    absolute_zero=kelvins_to_celsius(temp)
    print(absolute_zero)

if __name__=="__main__":
    main()
