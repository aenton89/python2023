import sys

def make_ruler(n):
    try:
        n = int(n)

        unit = "|...."
        ruler = ""
        ruler_numbers = "0".ljust(5)
    
        for i in range(1, n + 1):
            ruler += unit
            sI=str(i)
            if(len(sI) > 1):
                ruler_numbers += sI.ljust(7-len(sI))
            elif(sI == '9'):
                ruler_numbers += sI.ljust(4)
            else:
                ruler_numbers += sI.ljust(5)
        
        ruler += "| \n"
        ruler += ruler_numbers

    except ValueError:
        print("Error: bledne dane")
        sys.exit(1)

    return ruler



def make_grid(rows, cols):
    try:
        rows = int(rows)
        cols = int(cols)

        rectangle = ""
    
        for i in range(2*rows):
            if i % 2 == 0:
                line = "+---" * cols + "+\n"
            else:
                line = "|   " * cols + "|\n"
            rectangle += line
    
        rectangle += "+---" * cols + "+\n"

    except ValueError:
        print("Error: bledne dane")
        sys.exit(1)

    return rectangle