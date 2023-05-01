#tipe data : angka satuan tidak ada koma (interger)
data_interger = 1

print("data :", data_interger, ", bertipe : ", type(data_interger))



#type data : angka dengan koma (float)

data_float = 1.5
print("data :", data_float, ", bertipe : ", type(data_float))

# type data : string
data_string = "ucup"
print("data :", data_string, ", bertipe : ", type(data_string))

#type data : biner true/false (boolan)

data_bool = False
print("data :", data_bool, ", bertipe : ", type(data_bool))


# type data khusus
# bilangan kompleks


data_complex = complex(5,6)
print("data :", data_complex, ", bertipe : ", type(data_complex))


from ctypes import c_double

data_c_dloube = c_double(10.5)
print("data :", data_c_dloube, ", bertipe : ", type(data_c_dloube))