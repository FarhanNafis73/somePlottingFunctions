import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x_values = np.linspace(-10,10,500)
y_sinx = np.sin(x_values)
y_ex = np.exp(x_values)
y_cosx = np.cos(x_values)
y_x2 = x_values ** 2

sns.set_theme(style="whitegrid", font_scale=1.5)

fig, ax = plt.subplots(2, 2, figsize=(15,8), dpi = 100) # 2,2: First number is number of rows, second number is number of columns

# First row, first column
ax[0,0].plot(x_values, y_sinx, color = 'blue', linestyle = '--', linewidth = 3, label = 'sin(x)')
ax[0,0].set_xlabel('x', fontsize = 16)
ax[0,0].set_ylabel('sin(x)', fontsize = 16)
ax[0,0].tick_params(axis='both', labelsize = 14, which = 'major') # Select major or minor grid ticks
ax[0,0].legend(fontsize = 14)

# First row, second column
ax[0,1].plot(x_values, y_ex, color = 'red', linestyle = '-', linewidth = 3, label = 'exp(x)')
ax[0,1].set_xlabel('x', fontsize = 16)
ax[0,1].set_ylabel('exp(x)', fontsize = 16)
ax[0,1].tick_params(axis='both', labelsize = 14, which = 'major') 
ax[0,1].legend(fontsize = 14)

# Second row, first column
ax[1,0].plot(x_values, y_cosx, color = 'green', linestyle = '--', linewidth = 3, label = 'cos(x)')
ax[1,0].set_xlabel('x', fontsize = 16)
ax[1,0].set_ylabel('cos(x)', fontsize = 16)
ax[1,0].tick_params(axis='both', labelsize = 14) 
ax[1,0].legend(fontsize = 14)

# Second row, second column
ax[1,1].plot(x_values, y_x2, color = '#6E3BF5', linestyle = '--', linewidth = 3, label = 'x^2')
ax[1,1].set_xlabel('x', fontsize = 16)
ax[1,1].set_ylabel('X^2', fontsize = 16)
ax[1,1].tick_params(axis='both', labelsize = 14, which = 'major') 
ax[1,1].legend(fontsize = 14)

# plt.tight_layout()
# Exporting graph
# plt.savefig('saveGraphAs.pdf', dpi = 1200, bbox_inches='tight')
# Can export as png, jpg, svg, or tiff
plt.show()