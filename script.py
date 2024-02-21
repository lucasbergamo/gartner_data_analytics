import certifi
import json
import requests
import csv

def get_company_profile(symbol, api_key):
    url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={api_key}"
    response = requests.get(url, verify=certifi.where())
    data = response.json()
    return data[0] if data else None

def main():
    api_key = "SUA CHAVE API"
    companies = ["BRK-A", "GOOG", "BABA", "AMZN", "MSFT", "SCHW", "IBKR", "AAPL", "META", "AXP", "F", "PDD", "XOM", "TSLA", "GM", "BIDU", "CSCO", "INTC", "JNJ", "GE"]

    all_companies_info = []

    for company in companies:
        company_info = get_company_profile(company, api_key)

        if company_info:
            # Adicionando um dicionário à lista para cada empresa
            company_info_dict = {
                "Symbol": company_info["symbol"],
                "Name": company_info['companyName'],
                "Industry": company_info['industry'],
                "Description": company_info['description'],
                "Price": company_info['price'],
                "Beta": company_info['beta'],
                "VolAVG": company_info['volAvg'],
                "MktCap": company_info['mktCap'],
                "LastDiv": company_info['lastDiv'],
                "Changes": company_info['changes'],
                "Currency": company_info['currency'],
                "CEO": company_info['ceo'],
                "Sector": company_info['sector'],
                "Country": company_info['country'],
                "State": company_info['state'],
                "City": company_info['city'],
                "Zip": company_info['zip']
            }

            all_companies_info.append(company_info_dict)

    # Salvando a lista de dicionários em um arquivo CSV
    csv_file_path = "all_companies_info.csv"
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=company_info_dict.keys(), delimiter= ',')
        csv_writer.writeheader()
        csv_writer.writerows(all_companies_info)

    print(f"Dados salvos em {csv_file_path}")

if __name__ == "__main__":
    main()
