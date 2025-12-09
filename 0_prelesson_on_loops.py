# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# for loops  
# Theres a third number you can add ion for loop like slicing ex. (1, 11. 2) counts by two
# can itterate over string using for loop {goes iover all #/letter}
# continute = skip over itteration 
#break = stops loop
# ex:
for x in range(1, 21):
    if x == 13: # skips 13
        continue
    else:
        print(x)

#break stops group: 
for x in range(1, 21):
    if x == 13: # stops loop at 13
        break
    else:
        print(x)