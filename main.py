"""
num_1: int = int(input("enter a number 1: "))
num_2: int = int(input("enter a number 2: "))

if num_1 == num_2:
    print("both are same")
else:
    print("both are diff")

  

i = 1
while i < 10:
    print(i,'hello')
    i=i +1


for i in range(0,5, 2) :
    print(i, "rave") 


ab = 10
bc = 12
 
def number_add(a, b):
    sum = a+b
    return sum

new_sum = number_add(ab, bc)

print(new_sum)
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

if __name__ == "__main__":
    app.run(debug =True)