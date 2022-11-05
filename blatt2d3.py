import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

anzahl = {
    "Deutschland": [42, 20, 16, 18, 14],
    "Italien": [30, 25, 0, 22, 23],
    "Frankreich": [35, 40, 12, 10, 33]
}

pizzatyp = ["Margherita", "Salami", "Hawaii", "Tonno", "Funghi"]

def generateDataDict(data, type):
    dct = {}
    for land in anzahl: # land -> key, anzahl[land] -> value
        for l, p in zip(anzahl[land], pizzatyp):
            # print(f"({land}, {p}) -> {l}")
            dct[(land, p)] = l
    return dct

mosaic(generateDataDict(anzahl, pizzatyp), title="Tiefkühlpizzasverkauf", gap=0.05)
plt.show()