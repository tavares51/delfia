import csv
from datetime import datetime

def ler_arquivo(caminho):
    """
    Função para ler o arquivo CSV.

    Args:
        caminho (str): O caminho do arquivo CSV.

    Returns:
        list: Lista de transações do arquivo.
    """
    transacoes_retorno = []
    try:
        with open(caminho, 'r', encoding='UTF-8') as csv_arquivo:
            transacoes = csv.DictReader(csv_arquivo)
            transacoes_retorno = list(transacoes)
        return transacoes_retorno
    except FileNotFoundError:
        raise FileNotFoundError(f'O arquivo {caminho} não foi encontrado.\n')

def salvar_transacoes(transacoes_altas, caminho_saida='transacoes_altas.csv'):
    """
    Função para salvar transações em um novo arquivo CSV.

    Args:
        transacoes_altas (list): Lista de transações a serem salvas.
        caminho_saida (str): Caminho do arquivo de saída. Padrão é 'transacoes_altas.csv'.
    """
    with open(caminho_saida, 'w', newline='', encoding='UTF-8') as transacoes_altas_output:
        colunas = ['Nome do Cliente', 'Valor da Transação', 'Data da Transação']
        writer = csv.DictWriter(transacoes_altas_output, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(transacoes_altas)

def processar_dados(caminho, valor_limite):
    """
    Função principal para processar os dados do arquivo CSV.

    Args:
        caminho (str): O caminho do arquivo CSV.
        valor_limite (float): Limite para identificar transações altas.
    """
    try:
        transacoes = ler_arquivo(caminho)
        transacoes_altas = [linha for linha in transacoes if float(linha['Valor da Transação']) > valor_limite]  # Filtrando transações altas, utilizando list comprehension
        salvar_transacoes(transacoes_altas)
        print('Transações salvas com sucesso.')

    except Exception as ex:
        # Registra o erro em um arquivo de log
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensagem_erro = f'[{timestamp}] Erro: {str(ex)}.'
        with open('errors.txt', 'a', encoding='UTF-8') as log_file:
            log_file.write(f'{mensagem_erro}\n')

# Exemplo de uso
processar_dados('transacoes.csv', 1000)
processar_dados('nao_existe_transacoes.csv', 1000)
