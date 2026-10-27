import matplotlib.pyplot as plt
import numpy as np

# Ambar Fierro NC 0060

cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 7000, 9000, 12000, 18000]

# Primera gráfica (corregida la coma innecesaria)
plt.plot(cant_productos)
plt.show()

# Personalizar gráfica (corregida la coma faltante en linewidth=2)
plt.plot(
    cant_productos,
    precio,
    color="green",
    marker="o",
    linestyle="dashed",
    linewidth=2,
    markersize=12,
)
plt.title("ventas de walmart 0060")
plt.xlabel("cant prod")
plt.ylabel("precio")
plt.show()