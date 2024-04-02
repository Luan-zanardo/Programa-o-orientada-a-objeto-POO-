from ReservaCinema import Sala, IngressoNormal, IngressoVIP, Ingresso3D

sala1 = Sala(100)
ingresso_normal = IngressoNormal()
ingresso_vip = IngressoVIP()
ingresso_3d = Ingresso3D()

quantidade_ingressos = 5

if sala1.reservar(quantidade_ingressos):
    total_normal = ingresso_normal.calcular_preco(quantidade_ingressos)
    total_vip = ingresso_vip.calcular_preco(quantidade_ingressos)
    total_3d = ingresso_3d.calcular_preco(quantidade_ingressos)

    print(f"Total a pagar para ingressos normais: ${total_normal}")
    print(f"Total a pagar para ingressos VIP: ${total_vip}")
    print(f"Total a pagar para ingressos 3D: ${total_3d}")