import requests

def converter_moeda(valor_brl, moeda_destino):
    moeda_destino = moeda_destino.lower()
    url = f"https://economia.awesomeapi.com.br/json/last/BRL-{moeda_destino.upper()}"
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        print("Erro ao acessar a API.")
        return None

    dados = resposta.json()
    chave = f'BRL{moeda_destino.upper()}'
    
    if chave not in dados:
        print("Moeda não encontrada.")
        return None

    cotacao = float(dados[chave]['bid'])
    return valor_brl * cotacao

def main():
    print("Conversor de Moedas (BRL → USD, EUR, etc)")
    valor = float(input("Digite o valor em BRL: "))
    moeda = input("Digite a moeda de destino (ex: USD, EUR, ARS): ").upper()

    resultado = converter_moeda(valor, moeda)

    if resultado:
        print(f"\n{valor:.2f} BRL = {resultado:.2f} {moeda}")

if __name__ == "__main__":
    main()

