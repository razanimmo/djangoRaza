my_var =[2,2,4,5,6,7,3]
# n=1
# while n<10:
#  print(f"n is {n} but still not 10")
#  n=n + 1

my_var2="and 3"
my_var.pop(4)
employe_data=[{"ceo":"umer","cto":"zaeem","flutterDev":"raza","companyName":"Neksoft","numberOfmployes":56},
              {"ceo":"umer","cto":"zaeem","flutterDev":"raza","companyName":"Neksoft2.0","numberOfmployes":6},
              {"ceo":"umer","cto":"zaeem","flutterDev":"raza","companyName":"codify","numberOfmployes":56}]
employe_data[0]['waiter']="M.ali"
example_dict={"outer":{"inner":100}}


try:
    print("10"+10)
except:
    print("error")
finally:
    print("hello this is a code after error")


def checker_num(list):
    for it in list:
        if it==11:
         return True
    return False

ir=checker_num(my_var)
print(ir)
# print(employe_data[0].items())


# if employe_data[0]['waiter']=="umer":
#     print("umer is waiter")
# elif employe_data[0]['waiter']=="ahmed":
#    print("ahmed is waiter")
# else:
#  print(f"{employe_data[0]['waiter']} is waiter")
# print(employe_data[0]['ceo'])