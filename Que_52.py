#52.Write a function that computes the area of a rectangle.
# Then, write a second function that calls this function three times to compute the surface area of a rectangular solid.
def secondfun():
  a = 0
  for i in range(3):
    a = a + area(i+1,i+3)
  return a

def area(h,w):
  area=h*w
  return area

height=2
width=3
print(area(height,width))
print(secondfun())
