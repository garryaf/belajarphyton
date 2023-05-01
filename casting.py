#belajar casting

#merubah dari suatu tipe ke tipe data lain
#type type data = int, float, str, bool
print("--interget--")
data_int = 9;
print ('data = ', data_int, ", type =", type(data_int))


data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print ('data = ', data_float, ", type =", type(data_float))
print ('data = ', data_str, ", type =", type(data_str))
print ('data = ', data_bool, ", type =", type(data_bool))

print("--float--")
data_float = 9.9;
print ('data = ', data_float, ", type =", type(data_float))


data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print ('data = ', data_float, ", type =", type(data_float))
print ('data = ', data_str, ", type =", type(data_str))
print ('data = ', data_bool, ", type =", type(data_bool))

print("--boolean--")
data_bool = True;
print ('data = ', data_bool, ", type =", type(data_bool))


data_int = int(data_bool)
data_str = str(data_bool)
data_float = bool(data_bool)
print ('data = ', data_int, ", type =", type(data_int))
print ('data = ', data_str, ", type =", type(data_str))
print ('data = ', data_float, ", type =", type(data_float))