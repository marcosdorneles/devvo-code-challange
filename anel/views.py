from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from anel.forms import AnelForm

from .serializers import AnelSerializer
from .models import Anel

# Create your views here.


def index(request):
    aneis = Anel.objects.all()
    opcoes_forjador = Anel.OPCOES_FORJADOR
    return render(request, 'anel/index.html', {'aneis': aneis, 'opcoes_forjador': opcoes_forjador})


def detail(request, pk):
    anel = get_object_or_404(Anel, pk=pk)

    if request.method == 'POST':
        form = AnelForm(request.POST, instance=anel)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AnelForm(instance=anel)

    return render(request, 'anel/anel_detail.html', {'anel': anel, 'form': form})


@api_view(['GET'])
def listar_aneis(request):
    aneis = Anel.objects.all()
    serializer = AnelSerializer(aneis, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def criar_anel(request):
    data = request.data.copy()
    if not data.get('imagem') and data.get('imagem_predefinida'):
        data['imagem'] = data['imagem_predefinida']
    serializer = AnelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def anel_detail(request, pk):
    try:
        anel = Anel.objects.get(pk=pk)
    except Anel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnelSerializer(anel)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AnelSerializer(anel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        anel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
