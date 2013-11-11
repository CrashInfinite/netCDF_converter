import netCDF4

nc = netCDF4.Dataset('test.nc', 'a', format='NETCDF4');

print nc.file_format

nc_var = []

for x in nc.variables:
	nc_var.append(str(x))

nc_var.pop(0)


for x in nc.variables['zb']:
	print x


# nc_var.pop(0)

# f = open('file','w')
# for y in nc_var:
# 	for x in nc.variables[y]:
# 		f.write(str(x))

# for x in nc_var:

# 	print nc.variables[x]