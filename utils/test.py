from matplotlib import pyplot as plt
import numpy as np

y_values_engytime = [
    12000.067597149204,
12001.033925446984,
12007.935435461013,
11999.30334434349 ,
12196.353878287857,
12037.311240168567,
12279.204224235538,
]
engytime_baseline = 12002.044046987385
y_engytime = (np.array(y_values_engytime) - engytime_baseline) / engytime_baseline * 100

y_values_aggregation = [
    11427.231933091778,
11425.591214043028,
11419.46373804495 ,
11408.408253053716,
11411.096104043163,
11608.116595423591,
13061.290737340973,
]
aggregation_baseline = 11427.231
y_aggregation = (np.array(y_values_aggregation) - aggregation_baseline) / aggregation_baseline * 100

y_values_DS850 = [
    413.1335775404105 ,
413.1335775404105 ,
413.15592329472827,
413.1335775404105 ,
413.21340826258097,
414.77051868129206,
415.7366571213864 ,
]
DS850_baseline = 413.1335775404105
y_DS850 = (np.array(y_values_DS850) - DS850_baseline) / DS850_baseline * 100

y_values_diamond9 = [
    1015.2392000415291,
1015.2392000415291,
1015.256791229979 ,
1015.2392000415291,
1015.349929301801 ,
1015.425312198503 ,
1026.6195234935903,
]
diamond9_baseline = 1015.2392000415291
y_diamond9 = (np.array(y_values_diamond9) - diamond9_baseline) / diamond9_baseline * 100

x_values = list(range(4,11))

plt.plot(x_values, y_engytime, label='engytime')
plt.plot(x_values, y_aggregation, label='aggregation')
plt.plot(x_values, y_DS850, label='DS850')
plt.plot(x_values, y_diamond9, label='diamond9')
plt.legend()
plt.title('BPAA1_LSP1 on all datasets: WCSS error vs. Inaccurate portion size')
plt.xlabel('Inaccurate portion size')
plt.ylabel('WCSS error (%)')
plt.show()