# FILE NAME - convert_C_to_F_02.py

# NAME: Daniel Williams
# DATE: 3/27/2026
# BRIEF DESCRIPTION:  If Else and Conversion formulas



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def main():
  C_to_F_02_converter()
    
def C_to_F_02_converter():
  print('===== Temperature Converter =====')
  print()
  print('1. Convert from Celsius to Fahrenheit')
  print('2. Convert from Fahrenheit to Celsius')
  print()
  choice = int(input('Please choose from the above menu: '))

  if choice == 1:
    Celsius = float(input("Enter a temperature to convert: "))
    print()
    temperature = Celsius * 9/5 + 32
    print(f'{Celsius} degrees Celsius is {temperature} degrees Fahrenheit.')

  else:
    Fahrenheit = float(input("Enter a temperature to convert: "))
    print()
    temperature = (Fahrenheit - 32 ) * 5/9
    print(f'{Fahrenheit} degrees Fahrenheit is {temperature} degrees Celsius.')
main()

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab? I learned to adjust the indentation of text in the print statement. Also had to play with indentation of each block to get this to work so I understand proper indentation now.







'''
