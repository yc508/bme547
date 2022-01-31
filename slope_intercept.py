def inputrecieve():
    x1 = input("Enter x of your first coordinator: ")
    y1 = input("Enter y of your first coordinator: ")
    x2 = input("Enter x of your second coordinator: ")
    y2 = input("Enter y of your second coordinator: ")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    tuple1 = (x1, y1)
    tuple2 = (x2, y2)
    return(tuple1, tuple2)


def linearequation(tuple1, tuple2, x):
    m = (tuple2[1]-tuple1[1])/(tuple2[0]-tuple1[0])
    b = tuple1[1] - (m * tuple1[0])
    y = m * x + b
    return y
    #print("Your y value is {}". format(y))



if __name__ == "__main__":
    tuple1, tuple2 = inputrecieve()
    x = int(input("Enter your x value: "))
    y = linearequation(tuple1, tuple2, x)
    print(y)
    
