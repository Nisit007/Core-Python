n = {'nishit': 'patel',  <----'key':'value'
     'ford': 'car',
     'bmw': 1956}
print(n)

      # GET method
x = n.get('nishit')
print(x)
  # OUTPUT = patel

      # CHANGE value
n['nishit'] = 'ravi'
print(n)
  # OUTPUT = {'nishit': 'ravi', 'ford': 'car', 'bmw': 1956}
      
      # ADD dict
n['ravi'] = 'boss'
print(n)
  # OUTPUT = {'nishit': 'patel', 'ford': 'car', 'bmw': 1956, 'ravi': 'boss'}

      # REMOVE method
n.pop('nishit')
print(n)
  # OUTPUT = {'ford': 'car', 'bmw': 1956}
  
      # DEL method
del n['ford']
print(n)
  # OUTPUT = {'nishit': 'patel', 'bmw': 1956}
  
      # CLEAR method
n.clear()
print(n)
  # OUTPUT = {}

      # KEY method
m = n.keys()
print(m)
  # OUTPUT = dict_keys(['nishit', 'ford', 'bmw'])

      # UPDATE method
n.update({'color' : 'red'})
print(n)
  # OUTPUT = {'nishit': 'patel', 'ford': 'car', 'bmw': 1956, 'color': 'red'}
  
      # SET default
m = n.setdefault('nishit' , 'patidar')
print(m)
  # OUTPUT = patel
