from src.maths_ops import add,substract

def test_add():
  assert add(2,3)==5
  
  assert add(-1,1)==0
  
  
def test_sub():  
  assert substract(5,3)==2
  
  assert substract(4,3)==1
  assert substract(8,3)==5
  assert substract(5,5)==0
  
  
  