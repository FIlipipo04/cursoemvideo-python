# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 076 — Lista de preços com tupla
#
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
# preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em
# forma tabular.
# === FIM DO ENUNCIADO ===

lista = (
    'Processador Ryzen 5 5600', 830.00,
    'Placa-mãe MSI B550M', 816.00,
    'Memória RAM DDR4 32GB (2x16GB)', 900.00,
    'Placa de vídeo Radeon RX 7600 8GB', 1900.00,
    'SSD NVMe 1TB', 650.00,
    'Fonte 650W 80 Plus Bronze', 390.00,
    'Gabinete Mid Tower', 350.00,
    'Cooler adicional para processador', 120.00,
    'Kit de 3 fans RGB', 120.00,
    'Monitor 27 polegadas QHD 100Hz', 900.00,
    'Teclado mecânico', 180.00,
    'Mouse gamer', 100.00,
    'Headset gamer', 180.00,
    'Nobreak 1200VA', 450.00,
    'Mousepad', 80.00
)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<35}', end='')
    else:
        print(f'R${lista[pos]: >8.2f}')
