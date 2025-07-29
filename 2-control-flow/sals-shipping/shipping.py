# Sal's Shipping
# Sonny Li

weight = float(input('Please input your weight: ')) # made my own change by adding input for weight

# use both conditions mentioned in the table, that way it can be more granular rather than using one and it makes it easier for the code to meet the requirements
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 +20
else:
  cost_ground = weight * 4.75 + 20

print('Total cost of shipping this package will be: ' + str(cost_ground))
cost_ground_premium = 125.00
print('Total cost of ground shipping premium will be: ' + str(cost_ground_premium))
# This code calculates the cost of ground shipping based on the weight of the package.

# will now create the same code for drone shipping
if weight <= 2:
  cost_drone = weight * 4.5 
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9 
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12 
else:
  cost_drone = weight * 14.25 
print('Total cost of drone shipping will be: ' + str(cost_drone))

# going to see if we can run some test cases which will compare the code and whichever is cheaper will be the one that is printed
if cost_ground < cost_drone:
  print('Ground shipping is cheaper than drone shipping, the cost is: ' + str(cost_ground))
elif cost_drone < cost_ground:
  print('Drone shipping is cheaper than ground shipping, the cost is: ' + str(cost_drone))
else:
  print('Both ground and drone shipping cost the same, the cost is: ' + str(cost_ground))
