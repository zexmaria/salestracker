from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Venda
from .serializers import VendaSerializer

class RelatorioVendasAPIView(APIView):
    def get(self, request):
        # Filtragem por cliente, vendedor ou data
        vendas = Venda.objects.all()
        cliente_id = request.GET.get('cliente')
        vendedor_id = request.GET.get('vendedor')
        data_inicial = request.GET.get('data_inicial')
        data_final = request.GET.get('data_final')

        if cliente_id:
            vendas = vendas.filter(cliente_id=cliente_id)
        if vendedor_id:
            vendas = vendas.filter(vendedor_id=vendedor_id)
        if data_inicial and data_final:
            vendas = vendas.filter(data__range=[data_inicial, data_final])

        # Serializar os dados
        serializer = VendaSerializer(vendas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)