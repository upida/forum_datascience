from scipy.stats import beta

# 100 daging 50 hari
a, b = 100, 50
days_in_month = 30

upper = beta.ppf(0.975, a, b)
lower = beta.ppf(0.025, a, b)

lower_bound = lower * days_in_month
upper_bound = upper * days_in_month

print(lower_bound, upper_bound)
# 17.68504645143243 22.18865282697018