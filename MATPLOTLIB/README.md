```python
import matplotlib.pyplot as plt
x = [2010,2020,2030,2040,2050,2060,2070,2080]
y = [234, 120, 350,432, 587, 650,789, 792]
```
## line graph
```python
plt.plot(x,y) 
## (x-axis, y-axis)
```
## scatter plot
```
plt.scatter(x,y, s = np.array(y), c = color_list_of_data_represented, alpha = 0.8)
# s -> size of bubbles
# c -> color of bubbles
# alpha -> opacity(0 => transparent, 1 => not at all transparent,opaque) 
```
#£ histogram plot
```python
# historam(list_name, specify number of bins data to be seperated#default value 10#)
plt.hist(x)
plt.hist(x,5)
```
## Show plot
```python
plt.show()
```
## Plot Customizations
```python
# log all values on x-axis
plt.xscale('log')

# clean plot
plt.clf()

## label AXIS, to be used before show()
plt.xlabel('Year')
plt.ylabel('GDP')

## Adding title to plot
plt.title('Country GDP over years')

# shifting axis
plt.yticks([150,250,350,450,550,650,750,850,950])
plt.yticks([150,250,350,450,550,650,750,850,950],
	['150B','250B','350B','450B','550B','650B','750B','850B','950B'])

## Gridlines on plot
plt.grid(True)

## Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
```
