import pandas as pd

def my_func():
  d = {}
  d["col_a"] = ["a", "b", "c"]
  d["col_b"] = [1, 2, 3]
  d["col_c"] = [True, False, None]
  df = pd.DataFrame.from_dict(d)
  return df

if __name__ == "__main__":

  print(my_func())
