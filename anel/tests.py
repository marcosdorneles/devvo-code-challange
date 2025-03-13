from django.forms import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Anel


class AnelModelTest(TestCase):
    def setUp(self):
        # Criando alguns anéis com URLs de imagem completas para testar
        Anel.objects.create(
            nome="Anel de Sauron",
            poder="Domínio",
            portador="Sauron",
            forjadoPor=Anel.SAURON,
            imagem="https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg"
        )
        Anel.objects.create(
            nome="Anel dos Elfos",
            poder="Magia",
            portador="Elfo",
            forjadoPor=Anel.ELFOS,
            imagem="https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg"
        )
        Anel.objects.create(
            nome="Anel dos Homens",
            poder="Realeza",
            portador="Homem",
            forjadoPor=Anel.HOMENS,
            imagem="https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg"
        )

    def test_anel_str(self):
        anel = Anel.objects.get(nome="Anel de Sauron")
        self.assertEqual(str(anel), "Anel de Sauron")

    def test_validar_max_aneis_elves(self):
        """Verifica se a validação de um máximo de 3 anéis para Elfos está funcionando"""
        # Criando mais anéis para os Elfos
        Anel.objects.create(
            nome="Anel dos Elfos 2",
            poder="Sabedoria",
            portador="Elfo",
            forjadoPor=Anel.ELFOS,
            imagem="https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg"
        )
        Anel.objects.create(
            nome="Anel dos Elfos 3",
            poder="Poder",
            portador="Elfo",
            forjadoPor=Anel.ELFOS,
            imagem="https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg"
        )
        with self.assertRaises(ValidationError):
            anel = Anel.objects.create(
                nome="Anel dos Elfos 4",
                poder="Luz",
                portador="Elfo",
                forjadoPor=Anel.ELFOS,
                imagem="https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg"
            )

    def test_anel_create_view(self):
        """Testa se a view de criação de anéis funciona corretamente"""
        url = reverse('criar_anel')
        data = {
            'nome': 'Anel dos Anões',
            'poder': 'Ferro',
            'portador': 'Anão',
            'forjadoPor': Anel.ANOES,
            'imagem': 'https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Deve ter criado um novo anel
        self.assertEqual(Anel.objects.count(), 4)

    def test_anel_index_view(self):
        """Testa se a página de listagem de anéis está sendo carregada corretamente"""
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Anéis Cadastrados')

    def test_anel_detail_view(self):
        """Testa a página de detalhes de um anel"""
        anel = Anel.objects.get(nome="Anel de Sauron")
        url = reverse('detail', kwargs={'pk': anel.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, anel.nome)


def test_invalid_forjador(self):
    """Testa a validação de anéis de um mesmo forjador com mais de 3 Elfos, 7 Anões ou 9 Homens"""

    Anel.objects.create(
        nome="Anel dos Elfos 1",
        poder="Poder 1",
        portador="Elfo",
        forjadoPor=Anel.ELFOS,
        imagem="https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg"
    )
    Anel.objects.create(
        nome="Anel dos Elfos 2",
        poder="Poder 2",
        portador="Elfo",
        forjadoPor=Anel.ELFOS,
        imagem="https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg"
    )
    Anel.objects.create(
        nome="Anel dos Elfos 3",
        poder="Poder 3",
        portador="Elfo",
        forjadoPor=Anel.ELFOS,
        imagem="https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg"
    )

    anel_excesso = Anel(
        nome="Anel dos Elfos 4",
        poder="Poder",
        portador="Elfo",
        forjadoPor=Anel.ELFOS,
        imagem="https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg"
    )

    with self.assertRaises(ValidationError):
        anel_excesso.clean()

    def test_create_anel_with_predefined_image(self):
        """Testa a criação de um anel com uma imagem pré-definida"""
        url = reverse('criar_anel')
        data = {
            'nome': 'Anel Pré-definido',
            'poder': 'Força',
            'portador': 'Homem',
            'forjadoPor': Anel.HOMENS,
            'imagem': 'https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        anel = Anel.objects.get(nome='Anel Pré-definido')
        self.assertEqual(
            anel.imagem, 'https://cinepop.com.br/wp-content/uploads/2022/01/lord-cinepop.jpg')

    def test_create_anel_without_image(self):
        """Testa a criação de um anel sem imagem, o que deve gerar um erro de validação"""
        url = reverse('criar_anel')
        data = {
            'nome': 'Anel Sem Imagem',
            'poder': 'Nenhum',
            'portador': 'Desconhecido',
            'forjadoPor': Anel.SAURON,
            'imagem': '',  # Nenhuma imagem fornecida
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertContains(
            response, "Por favor, forneça uma URL de imagem válida.")
