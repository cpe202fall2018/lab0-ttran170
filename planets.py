
def weight_on_planets():
   # write your code here
    inp = float(input("What do you weigh on earth? "))
    mw = inp * 0.38
    jw = inp * 2.34
    print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(mw,jw))
   
   
   
if __name__ == '__main__':
   weight_on_planets()
