class StringCalculator:
  def __init__(self):
    self.negatives = []
    self.delimeters = [',']
    self.total_summ = 0

  def Add(self, nums) -> int:
    self.__init__()
   
    cutted_nums = self.FindOutDelimeter(nums)
    self.FindNumbers(cutted_nums)

    if len(self.negatives) > 0:
      raise Exception("Negatives not allowed, please check the numbers:{0}".format(self.negatives))

    return self.total_summ

  def FindOutDelimeter(self, nums):
    if(len(nums) > 2 and nums[0:2:] == "//"):#first chars are delimeter instructions?
      nums = nums[2:]#cutting off the first param from array
      i = 0
      while i < len(nums):#iterate all delimeters
        if nums[i] != '\n':
          self.delimeters.append(nums[i])
        else:
          break
        i += 1

      nums = nums[i:]#cut off the delimeters from array

    return nums                   

  def FindNumbers(self, cutted_nums:str)->int:
    item = ""
    for i in cutted_nums:#iterate numbers
      if i in self.delimeters:#is a delimeter
        self.SumNumber(item) #sum concatenated number
        item = ""
      elif i.isdigit() or i == '-':#is negative or number
        item += i #concat character to number item
    self.SumNumber(item)

  def SumNumber(self, strNumber:str):
    if(strNumber != ""):
      number = int(strNumber)
      if (number < 0):#add to negative list
        self.negatives.append(number)
      elif(number < 1000):#only sum if less then a thousand
        self.total_summ += number

def CalculatorTester(inputStr:str, expected:int, mustThrow:bool):
  sc = StringCalculator()
  replaced = inputStr.replace("\n","")#console must be legible
  if mustThrow: #test if result must throw exception
    try:
      res = sc.Add(inputStr)
      print("FAILED--{0}--".format(replaced))  
    except Exception as inst:
      print("Passed--{0} -> Threw:{1}".format(replaced, inst))
  else:
    res = sc.Add(inputStr)
    if (expected != res):# assert result with expectation
      print("FAILED--{0}--".format(replaced))
    else:
      print("Passed--{0}".format(replaced))



#####
CalculatorTester("//,\n1,2", 3, False)
CalculatorTester("//;\n1;2", 3, False)
CalculatorTester("//$\n1$2", 3, False)
CalculatorTester("//$\n1$2$3", 6, False)
CalculatorTester("//@\n2@3@8", 13, False)
CalculatorTester("//%\n1%2%3%4%5", 15, False)

CalculatorTester("//,\n2,1001", 2, False)
CalculatorTester("//;\n2;1001", 2, False)

CalculatorTester("1,2", 3, False)
CalculatorTester("1,2,5", 8, False)
CalculatorTester("1,2,3,4,5", 15, False)
CalculatorTester("1\n,2,\n3", 6, False)
CalculatorTester("1\n,2,\n3", 6, False)
CalculatorTester("1\n,-2,\n3,\n-4", 6, True)

CalculatorTester("11,2", 13, False)
CalculatorTester("100,2", 102, False)
CalculatorTester("//$,@\n1$2@", 3, False)
CalculatorTester("//$,@\n1$2@,3,4$5,1001,10003", 15, False)

CalculatorTester("//$,@\n1$2@,3,4$5,1001,-10003", 15, True)
CalculatorTester("//,\n-1,2", 3, True)
CalculatorTester("//***\n1***2***3", 6, False)

