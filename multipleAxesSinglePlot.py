import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = np.linspace(1, 11, 100)

# This plot shows three y values within one graph (sharing same x axis).

df = pd.DataFrame(
    {
        "X": x,
        "Y1": x * 2,  # First y val
        "Y2": x ** 2, # Second y val 
        "Y3": x ** 3, # Third y val 
    }
)

sns.set_theme(style="whitegrid", font_scale=1.2) 
# Initialize the first plot (Left Y-Axis)
fig, ax1 = plt.subplots(figsize=(12, 7), dpi = 100)

# To set specific font size use fontsize = ; and for bold, use weight = 'bold'
sns.lineplot(data=df, x="X", y="Y1", ax=ax1, color="blue", label="Y1 Data")
ax1.set_ylabel("Y1 Axis", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")
# Individual line legends are not necessary, that's why the following line is implemented.
ax1.get_legend().set_visible(False)

# Create the second plot (Right Y-Axis)
ax2 = ax1.twinx()
sns.lineplot(data=df, x="X", y="Y2", ax=ax2, color="green", label="Y2 Data")
ax2.set_ylabel("Y2 Axis", color="green")
ax2.tick_params(axis="y", labelcolor="green")
ax2.get_legend().set_visible(False)

# Create the third plot (Offset from the Right Y-Axis)
ax3 = ax1.twinx()
sns.lineplot(data=df, x="X", y="Y3", ax=ax3, color="red", label="Y3 Data")
ax3.set_ylabel("Y3 Axis", color="red")
ax3.tick_params(axis="y", labelcolor="red")
ax3.get_legend().set_visible(False) 

# Shifting the third axis spine outward so it doesn't overlap ax2
ax3.spines["right"].set_position(("outward", 65))

# Legends and layout
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax1.legend(lines1 + lines2 + lines3, labels1 + labels2 + labels3, fontsize=14, loc="upper left")

# plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.6)

# Exporting graph
# plt.savefig('saveGraphAs.pdf', dpi = 1200, bbox_inches='tight') 
# Can export as png, jpg, svg, or tiff
plt.show()