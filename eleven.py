import math
import statistics
import twelve
import twelve as t
import urllib.request

# math module
print(math.pi)
print(math.log(10))
print(math.pow(2, 4))
print(math.sqrt(100))

# statistics module
print(statistics.mean([2, 5, 6, 9]))
print(statistics.median([1, 2, 3, 8, 9]))

# using twelve
print(twelve.hello_world())
print(twelve.good_by_world())

# using custom name
print(t.hello_world())

# using another module
html = urllib.request.urlopen('https://wftutorials.blog/about/')
print(html.read())
