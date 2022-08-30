import numpy as np

def calculate(list):
  print(len)
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")  
  result={}
  a = np.array(list).reshape(3,3)
  list=[]
  col_mean=(np.mean(a, axis=0)).tolist()
  list.append(col_mean)
  row_mean=(np.mean(a, axis=1)).tolist()
  list.append(row_mean)
  array_mean=(np.mean(a)).tolist()
  list.append(array_mean)
  result['mean']=list
  # calculate the variance col wise, row wise and entire array
  list = []
  col_var = (np.var(a, axis=0)).tolist()
  list.append(col_var)
  row_var = (np.var(a, axis=1)).tolist()
  list.append(row_var)
  array_var = (np.var(a)).tolist()
  list.append(array_var)
  result['variance'] = list

# calculate the standard deviation
  list=[]
  col_std = np.std(a, axis=0).tolist()
  list.append(col_std)
  row_std = np.std(a, axis=1).tolist()
  list.append(row_std)
  array_std = np.std(a).tolist()
  list.append(array_std)
  result['standard deviation'] = list

# calculate the max
  list=[]
  col_max = np.max(a, axis=0).tolist()
  list.append(col_max)
  row_max = np.max(a, axis=1).tolist()
  list.append(row_max)
  array_max = np.max(a).tolist()
  list.append(array_max)
  result['max'] = list

# calculate the min
  list=[]
  col_min = np.min(a, axis=0).tolist()
  list.append(col_min)
  row_min = np.min(a, axis=1).tolist()
  list.append(row_min)
  array_min = np.min(a).tolist()
  list.append(array_min)
  result['min'] = list

# calculate the sum
  list = []
  col_sum = np.sum(a, axis=0).tolist()
  list.append(col_sum)
  row_sum = np.sum(a, axis=1).tolist()
  list.append(row_sum)
  array_sum = np.sum(a).tolist()
  list.append(array_sum)
  result['sum'] = list
  return result