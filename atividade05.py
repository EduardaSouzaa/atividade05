# Digite uma metragem e veja isso em cm e mm:

metros = float(input("digite o valor em metros \n"))
cm = metros * 100
mm = metros * 1000
print(f"""Convertendo o valor {metros} M
      MM = {mm} mm
      CM = {cm} cm
      """)
