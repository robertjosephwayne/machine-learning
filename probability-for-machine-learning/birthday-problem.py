# Problem:
# How many people are required
# so that any two people in the group have the same birthday
# with at least a 50-50 chance?

max_group_size = 30
days_per_year = 365

# Calculate probability for different group sizes
p = 1.0
for i in range(1, max_group_size):
    available_days = days_per_year - i
    p *= available_days / days_per_year
    print('n=%d, %d/%d, p=%.3f 1-p=%.3f' % (i+1, available_days, days_per_year, p*100, (1-p)*100))

