#David Abushlaih 

#This function takes in the input from the list as the paramter L, then it has a variable which will be used to signify the previous value when comparing 2 values in the list. I deleted the first value of the list because at this point a is equal to the first value and it will cause the program to run incorrectly when comparing a = L[0] with the first value in the for loop. I loop throgh the values in the list and then if the num in the loop is greater than the value of the previous number in this case a, then we set a to the number and continue on with the loop. If at any point the number is not greater than the previous value, False is outputted.
def isIncreasing(L):
  a = L[0]
  del L[0]
  for num in L:
    if num > a:
      a = num
    else:
      return (False)
  return True


#This function takes in input from a list of positive integer digits and it converts the separate digits into a number such that [1,2,3] would convert to 123. In order to accomplish this I made a variable a, which is equal to an empty string. Afterwards, I used a for loop to loop through the values of the list L. I then set a = a + the string of the number in the list. This is so we can concatenate strings because int doesnt work with string in this way. I then converted a to an int and returned a
def NumConvert(L):
  a = ""
  for value in L:
    a = a + str(value)
  a = int(a)
  return a








# My program takes in a string representing a binary number. For clarity I set a variable binary = to that input. The next step that I do is create 2 variables one called count = 1, the first value of the binary number, and one called decimal which is going to be the result. Now I create a list and loop through all the characters in the binary string and append them onto the list. The thing is, the values in the list are read in reverse using the binary conversion method I'm using so I reverse the list using [::-1]. I then loop through the list and use an if statement to check if the value of the item in the list is equal to '1', no need to use an else to check for 0 because you dont need to add anything if it equals 0. I add the variable count if the value is equal to 1 to the decimal variable. Lastly, I multiply count by 2 to account for the conversions in binary which go in stages from 2^0 = 1 to 2^1 = 2 to 2^2 = 4 and so on. I return the decimal number converted from binary to decimal.

def BinConvert(string):
  binary = string
  count = 1
  decimal = 0

  list_1 = []
  for value in binary:
    list_1.append(value)
  list_1 = list_1[::-1]

  for i in list_1:
    if i == "1":
      decimal  = decimal + count
    count = count * 2
  return decimal













def main():
  #Begin Question 1
  print("-------------------------Question 1---------------------------------")
  print("My program takes in input in the form of a list of integers and returns True if the numbers in the list continue to Increase and False otherwise\n")
  list_1 = [-100,-90,-56,-57,57,80]
  print(list_1, "\n")

  print("This is an example of a list that has integers that increase but then decrease at one point, therefore it is False\n")

  print(isIncreasing(list_1), "\n")
 
  list_2 = [-100,-40,0,34,100,8000]
  print(list_2, "\n")
  print("This is an example of a list that has integers that just keep increasing, therefore True is returned\n")
 
  print(isIncreasing(list_2))
  print("---------------------------------------------------------------------")

  #End Question 1



  #Begin Question 2
  print("-------------------------Question 2---------------------------------")
  print("My program takes in a list of positive integer digits that is then converted into a number that concatenates all the digits together and converts it back as an integer number for example: [1,2,3] is converted to 123\n")
  digits = [1,2,3,4,5,6,4,6,7]
  print("This is a list of digits:", digits, "\n")
 
  digits_2 = [4,7,2,1,9]
  print(digits, "is converted to", NumConvert(digits), "\n")

  print("This is another list of digits:", digits_2, "\n")

  print(digits_2, "is converted to", NumConvert(digits_2))
  print("---------------------------------------------------------------------")
  #End Question 2


  #Begin Question 3
  print("-------------------------Question 3---------------------------------")
  print("My program takes in a string representing binary and I convert it to a decimal number using a for loop to convert the string to a list, then reversing that list, and then looping through that list and adding a value to the variable decimal depending on if the value in the list is = '1' Then I multiplied count by 2 in order to account for the conversion\n")
  a = "1011"
  print("The value of", a, "converted to binary is", BinConvert(a), "\n")
  b = "10111"
  print("The value of", b, "converted to binary is", BinConvert(b), "\n")
  c = "00000111"
  print("The value of", c, "converted to binary is", BinConvert(c), "\n")
  d = "101101"
  print("The value of", d, "converted to binary is", BinConvert(d))
  print("---------------------------------------------------------------------")
  #End question 3
  
main()