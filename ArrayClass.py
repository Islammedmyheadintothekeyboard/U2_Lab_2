# YOUR CODE AND HEADING HERE
import ctypes

class DynamicArray:
  def __init__(self, c=0):
    self.__capacity = 1
    self.__A = self.__make_array(c)
    self.__n = 0
  
  def __str__(self):
    if self.__n == 0:
        return "[]"

    out = '['
    for i, element in enumerate(self.__A):
        try:
            out += str(element) + ', '
            temp = self.__A[i+1]
        except:
            break
    return out[:-2] + ']'



  def __make_array(self, c):
    return (c * ctypes.py_object)()

  def get_cap(self):
    return self.__capacity

  def __resize(self):
    for loop in range(0, self.__capacity, 1):
      self.__A += [None]
    self.__capacity *= 2

  def append(self, item):
    if self.__n == self.__capacity:
      self.__resize()
    self.__A[self.__n] = item



  def __getitem__(self, k):
    """return element at index"""
    if k <= 0 or k >= self.__n:
        raise IndexError("invalid index")
    
    return self.__A[k]

  def __len__(self):
    return self.__n