from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import ViaCepModel  
from .serializers import CepSerializer
import requests

class ViaCepViewSet(ModelViewSet):
    queryset = ViaCepModel.objects.all()
    serializer_class = CepSerializer

    def create(self, request):  
        cep = request.data.get("cep", "00000000")
        
        site = f"https://viacep.com.br/ws/{cep}/json/"  

        requisicao = requests.get(site)
        print(requisicao)
        json_data = requisicao.json()  

        cep_result = json_data.get('cep', '')
        logradouro = json_data.get('logradouro', '')
        complemento = json_data.get('complemento', '')
        bairro = json_data.get('bairro', '')
        localidade = json_data.get('localidade', '')
        uf = json_data.get('uf', '')
    
        dados_recebidos = {
            "cep": f"{cep_result}",
            "logradouro": f"{logradouro}",
            "complemento": f"{complemento}",
            "bairro": f"{bairro}",
            "localidade": f"{localidade}",
            "uf": f"{uf}"
        }
    
        meu_serializer = CepSerializer(data=dados_recebidos)  

        if meu_serializer.is_valid():
            cep_pesquisado = ViaCepModel.objects.filter(cep=cep_result)
            cep_pesquisado_existe = cep_pesquisado.exists()

            if cep_pesquisado_existe:
                return Response({"aviso": "Seu CEP já está no banco de dados"})  
            
            meu_serializer.save()
            return Response(meu_serializer.data)
        else:
            return Response({"Aviso": "Houve um problema com os dados recebidos"})