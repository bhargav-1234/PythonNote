import datetime
import re
import math
import json
x = datetime.datetime.now()
print(x)
print("hello")
def my():
  print("Hi bhargav")
my()
txt = "Hi Bhargav how are you"
x = re.search("how",txt)
print(x)
print(math.acos(0))
x =  {
  1:{
  "name":"Bhargav",
  "age":24,
  "colour":"white"
  },
  2:{
  "name":"Arun",
  "age":30,
  "colour":"white"
  }
}
print(json.dumps(x, indent=4))
list = ["lemon", "grape", "Dragon friut", "water melon"]
print(list)