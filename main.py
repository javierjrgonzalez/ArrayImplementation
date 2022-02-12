class MyArray:
  def __init__(self):
    self.lenght=0
    self.data={}

  def __str__(self):
    return str(self.__dict__)

  def push(self,item):
    self.data[self.lenght] = item
    self.lenght+=1

  def pop(self):
    lastitem = self.data[self.lenght-1]
    del self.data[self.lenght-1]
    self.lenght-=1
    return lastitem

  def delete(self,index):
    deleteditem = self.data[index]
    for i in range(index,self.lenght-1):
      self.data[i] = self.data[i+1]

    del self.data[self.lenght-1]
    self.lenght-=1
    return deleteditem

arr = MyArray()
arr.push(3)
print('Array after pushing 3',arr)
arr.push('hi')
print('\n''Array after pushing hi',arr)
arr.push(34)
print('\n''Array after pushing 34',arr)
arr.push(20)
print('\n''Array after pushing 20',arr)
arr.push('hey')
print('\n''Array after pushing hey',arr)
arr.push('welcome')
print('\n''Array after pushing welcome',arr)
arr.delete(3)
print('\n''Array after deleting item in index 3',arr)
arr.pop()
print('\n''Array after popping last item',arr)


