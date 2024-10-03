def safe_divide(numerator , denomenator):
     division = numerator/denomenator
     return(division)
try:
    numerator = int (input("Enter the numerator : "))
    denomenator = int (input("Enter the denomenator : "))
    if denomenator != 0:
      result =safe_divide(numerator , denomenator) 
      print (f"the result is {result}")
    else:
      raise ZeroDivisionError("Invalid denomenator. Please enter the the right denomenator")
except ValueError:
  print("please enter an integer number")
except ZeroDivisionError as e:
    print(e) 
