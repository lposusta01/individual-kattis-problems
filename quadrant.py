"""
Determine quadrant of coordinate pair
Elizabeth Posusta - Sep 2026
"""

def main() -> None:
  # input
  x: int = int(input())
  y: int = int(input())
  # processing
  
  
  # output
  if x > 0:
    if y > 0:
      print(1)
    else:
      print(4)
  else:
    if y > 0:
      print(2)
    else:
      print(3)

if __name__ == "__main__":
  main()
    
