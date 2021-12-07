# Ideas:
# The median minimizes the sum of absolute differences. Exactly what we need here.
# The mean minimizes the sum of squared differences. Almost what we need here, since we have n^2*n/2 as our distances.
# Article: https://www.johnmyleswhite.com/notebook/2013/03/22/modes-medians-and-means-an-unifying-perspective/
# More thorough explanation: https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/

# From 4HbQ on Reddit
from numpy import *
x = fromfile("input.txt", int, sep=',')

print(int(sum(abs(x - median(x)))))

fuel = lambda d: d*(d+1)/2

print(int(min(sum(fuel(abs(x - floor(mean(x))))),
              sum(fuel(abs(x - ceil(mean(x))))))))
