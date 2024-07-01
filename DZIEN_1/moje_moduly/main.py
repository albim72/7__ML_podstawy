print("program testowy -> Python 3")

liczba = [4,6,26,8,9,-324,2,0,356,1000,-987,45,13,5,8,-12]

print(liczba)
print(type(liczba))

parzyste = list(filter(lambda x:x%2==0,liczba))
print(parzyste)

cube =  list(map(lambda x:x**3,liczba))
print(cube)

def witaj(imie):
    return f'Miło Cię widzieć {imie}!'


from funkcje.bfunkcje import konkurs,punkty_plus_bonus

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Anna"))
print(osoba(konkurs,"Jan",67,11))
print(osoba(punkty_plus_bonus,67,10))
