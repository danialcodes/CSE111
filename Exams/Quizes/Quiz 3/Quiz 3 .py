class ECustomer:
  count = 0
  def __init__(self,name):
    ECustomer.count+=1
    self.name = name
    self.products = ''
    self.total_cost = 0
  def setProductDetails(self,*item):
    for i in range(len(item)):
      if i%2 == 0:
        self.products+=item[i]+', '
      else:
        self.total_cost+=item[i]
    self.products = self.products[:-2]
  def printDetail(self):
    print('Name: {}\nProducts: {}\nTotal cost: {}'
    .format(self.name,self.products,self.total_cost))

# Write your codes here.
print("Total E-Customer:", ECustomer.count)
c1 = ECustomer("James")
c1.setProductDetails("TV",35000,"Air Cooler", 9000)
c2 = ECustomer("Mike")
c2.setProductDetails("Mobile",20000,"Headphone",1200,"Fridge", 45000)
c3 = ECustomer("Sarah")
c3.setProductDetails("Headphone", 1200)
print("=========================")
c1.printDetail()
print("=========================")
c2.printDetail()
print("=========================")
c3.printDetail()
print("=========================")
print("Total E-Customer:", ECustomer.count)