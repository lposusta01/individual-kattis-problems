"""
Balloon problem
Elizabeth Posusta - Sep 2026
"""

def main() -> None:
  # input
  
  i: int = 0
  k: list[int] = []
  q: list[int] = []
  
  while input() != "":
    try:
      inp = input().split(" ")
      k.append(int(inp[0]))
      q.append(int(inp[1]))
      print(f"\n={k, q}=")
    except:
      break
    i += 1

  q.sort()
    
  print(f"{q[0]}")
  # processing
  
  
  # output

if __name__ == "__main__":
  main()
