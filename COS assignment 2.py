zprint("welcome to coc101 ")
print ("BHU|24|04|09|0019")
print("joel mschow")


def a():
    displacement = int(input("enter velocity:"))
    time = int(input("enter time: "))
    # velocity = displacement/time

    //
    output = str(displacement/time)
    print(output +"m/s^1")

def b():
    work  =int(input("enter work:"))
    time= int(input("enter  change in time:"))
    # power = work*change  in  time
    output = str(work / time
    print(output + "w")

def d():
    force= int(input("enter  force :"))
    length= int(input("enter length:"))
    #surface tenion = force/length
    output = str(force/length)

def d():
    mass= int(input("enter mass" ))
    volume= int(input("enter volume"))
    #surface tention = mass/volume
    output = str(mass/volume)
    print(output + "pa")

def e():
    a =int(input("enter a :"))
    b = int(input("enter b :"))
    # power = a^b
    output = str(a**b)
    print(output)

def main():
     user_choice = input("enter choice (a for accelaration) , (b for power) , (c for surface tension),(d for pressure),e(raise to power):")
        if  user_choice =="a":a()
        elif  user_choice == "d":d()
        elif  user_choice =="c":c()
        elif  user_choice == "d":d()
        elif  user_choice == "e":e()
if __name__ == '__main__':
     main()
