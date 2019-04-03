# Explain what the following code does: ( ( n & ( n-1)) == 0). 

# In order for the above expression to equal 0, that means when 1 is subtracted from n, all of its bits must flip.
# And the only for all of its bits to flip is if n has a single 1 bit followed be a trail of 0s. Ex: 10000.
# This would mean that n is also a power of 2