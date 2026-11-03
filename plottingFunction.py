import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generates 500 evenly spaced points between -5 and 5
x_values = np.linspace(-5, 5, 500)
y_values = x_values ** 2

sns.set_theme(style="whitegrid", font_scale=1.5) 

plt.figure(figsize=(12, 7), dpi=100)
sns.lineplot(x = x_values, y = y_values, label = 'calculated y values', color="red", linewidth=2, linestyle='--')
plt.title('Y = X ** 2 Graph', fontsize=16, weight='bold')

# X axis
plt.xlabel('X values', fontsize=16)
# Limit values between zero and five
plt.xlim(0,5)
# plt.xticks(fontsize=16, color='black', weight = 'bold')

# Y axis
plt.ylabel('Y values', fontsize=16)
plt.ylim(0,)
# plt.yticks(fontsize=16, color='black', weight = 'bold')

plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Exporting graph
# plt.savefig('saveGraphAs.pdf', dpi = 1200, bbox_inches='tight') 
# Can export as png, jpg, svg, or tiff
plt.show()