import math

def main():
    print("\nQuadratic Equation Solver")
    print("Quadratic Equation format : ax^2 + bx + c = 0")
    print("You can select what you want to solve for!\n")
    
    print("1. Find the Roots of the Equation")
    print("2. Form the Equation from the Roots")
    
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Invalid input. PLease enter a valid Number")
        return
    
    if choice == 1:
        # Input values
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        
        #Display the equation
        print(f"Your Equation : {a}x^2 + {b}x + {c} = 0\n")
        
        #Calculate the discriminant
        discriminant = b**2 - 4 * a * c
        
        if discriminant < 0:
            print("No real roots exist because the discriminant is negative.")
        elif discriminant == 0:
            #result if D is 0
            result = -b / 2 * a
            print("Since D = 0, The equation has only one real root")
            print(f"Root: {result}")
        else:
            e = math.sqrt(discriminant) # Calculate the square root of the discrimant
            f = round((-b + e) / (2 * a), 1) # First root
            g = round((-b - e) / (2 * a), 1) # Second root

            # Display the roots 
            print(f"Root 1: {f}")
            print(f"Root 2: {g}")
            print("\n")
        
        #Graph plotting
        spaces = [' ', ' ']

        if discriminant > 0:
            print("Your graph should look like this")
        elif discriminant == 0:
            print("Unable to load graph, Meet Mr Samuel Ikoro to fix this problem")
        else:
            print(f"Can't illustrate graph because The discriminant is negative( D = {discriminant})")
        while discriminant > 0:
            if a < 0 and f > 0 and g < 0:
                print("               |____              ")
                print("               |    |             ")
                print("              ||     |            ")
                print("             | |      |           ")
                print("            |  |       |          ")
                print("           |   |        |         ")
                print("          |    |         |        ")
                print("_________|_____|__________|______")
                print(f"    {g}|      |0     {f}  |      ")
                print("       |       |            |    ")
                print("      |        |             |   ")
                print("     |         |              |  ")
                print("     |         |              | ")
                print("               |               ")
                print("               |               ")
                print("               |               ")
                break
            elif a < 0 and f < 0 and g > 0:
                print("               |____              ")
                print("               |    |             ")
                print("              ||     |            ")
                print("             | |      |           ")
                print("            |  |       |          ")
                print("           |   |        |         ")
                print("          |    |         |        ")
                print("_________|_____|__________|______")
                print(f"    {f}|      |0     {g}  |      ")
                print("       |       |            |    ")
                print("      |        |             |   ")
                print("     |         |              |  ")
                print("     |         |              | ")
                print("               |               ")
                print("               |               ")
                print("               |               ")
                break
            elif a > 0 and f < 0 and g > 0:
                print("                   |                  ")
                print("      |            |            |      ")
                print("       |           |            |      ")
                print("        |          |           |       ")
                print("         |         |          |        ")
                print("          |        |         |         ")
                print("__________ |_______|________|_______")
                print(f"       {f} |      |0      |  {g}        ")
                print("             |     |      |            ")
                print("              |    |     |             ")
                print("               |   |    |            ")
                print("                |  |   |               ")
                print("                 |_|__|                ")
                print("                   |                  ")
                break
            elif a > 0 and f > 0 and g < 0:
                print("                   |                  ")
                print("      |            |            |      ")
                print("       |           |            |      ")
                print("        |          |           |       ")
                print("         |         |          |        ")
                print("          |        |         |         ")
                print("__________ |_______|________|_______")
                print(f"       {g} |      |0      |  {f}        ")
                print("             |     |      |            ")
                print("              |    |     |             ")
                print("               |   |    |            ")
                print("                |  |   |               ")
                print("                 |_|__|                ")
                print("                   |                  ")
                break
            elif a > 0 and f < 0 and g < f:
                print("                           |  |        ")
                print("                           | |        ")
                print("                           ||        ")
                print(" |                         |     ")
                print("  |                       ||      ")
                print("   |                     | |     ")
                print("    |                   |  |      ")
                print("     |                 |   |      ")
                print("_____ |_______________|____|_______")
                print(f"   {g}|             |{f} |      ")
                print("        |           |      |      ")
                print("         |         |       |      ")
                print("          |       |        |    ")
                print("           |     |         |      ")
                print("            |___|          |      ")
                print("                           |       ")
                break
            elif a > 0 and f < g and g < 0:
                print("                           |  |        ")
                print("                           | |        ")
                print("                           ||        ")
                print(" |                         |     ")
                print("  |                       ||      ")
                print("   |                     | |     ")
                print("    |                   |  |      ")
                print("     |                 |   |      ")
                print("_____ |_______________|____|_______")
                print(f"   {f}|             |{g} |      ")
                print("        |           |      |      ")
                print("         |         |       |      ")
                print("          |       |        |    ")
                print("           |     |         |      ")
                print("            |___|          |      ")
                print("                           |       ")
                break
            elif a > 0 and f > g and g > 0:
                print("     |  |                              ")
                print("      | |                       |      ")
                print("       ||                      |      ")
                print("        |                     |       ")
                print("        ||                   |        ")
                print("        | |                 |         ")
                print("________|_ |_______________|_______")
                print(f"     0 |{g}|             |{f}        ")
                print("        |     |          |            ")
                print("        |      |        |             ")
                print("        |       |      |            ")
                print("        |        |    |               ")
                print("        |         |__|                ")
                print("                                      ")
                break
            elif a > 0 and f > 0 and g > f:
                print("     |  |                              ")
                print("      | |                       |      ")
                print("       ||                      |      ")
                print("        |                     |       ")
                print("        ||                   |        ")
                print("        | |                 |         ")
                print("________|_ |_______________|_______")
                print(f"     0 |{f}|            |{g}        ")
                print("        |     |          |            ")
                print("        |      |        |             ")
                print("        |       |      |            ")
                print("        |        |    |               ")
                print("        |         |__|                ")
                print("                                      ")
                break
        while discriminant > 0:
            print("\n")
            print("At turning point, dy/dx = 0")
            x_max = round(((f + g) / 2), 2)
            y_max = a*(x_max**2) + (b*x_max) + c
            y_intercept = c
            print(f"Extremum or Turning point: ({x_max}, {y_max})") 
            print(f"y-Intercept : (0, {c})")
            break
            
    elif choice == 2:
        #Input values and using the Try and Except conditions to prevent the program from crashing
        try:
            root1 = float(input("Enter Root 1 : "))
            root2 = float(input("Enter Root 2 : "))
        except ValueError:
            print("Must be a valid integer or floating point number!")
            return
        print("")
        
        #Main logic
        sum_of_roots = round((root1 + root2), 2)
        product_of_roots = round((root1 * root2), 2)
        
        #Displaying the Equation
        if sum_of_roots < 0 and product_of_roots < 0:
            print(f"Equation:     x^2 {sum_of_roots}x {product_of_roots} = 0")
        elif sum_of_roots < 0 and product_of_roots > 0:
            print(f"Equation:     x^2 {sum_of_roots}x + {product_of_roots} = 0")
        elif sum_of_roots > 0 and product_of_roots > 0:
            print(f"Equation:     x^2 + {sum_of_roots}x + {product_of_roots} = 0")
        elif sum_of_roots > 0 and product_of_roots < 0:
            print(f"Equation:     x^2 + {sum_of_roots}x {product_of_roots} = 0")
        elif sum_of_roots == 0 and product_of_roots < 0:
            print(f"Equation:     x^2 {product_of_roots} = 0")
        elif sum_of_roots == 0 and product_of_roots > 0:
            print(f"Equation:     x^2 + {product_of_roots} = 0")
print("\n\nMade by SAMUEL IKORO\n\n")
 
if __name__ == "__main__":
    main()