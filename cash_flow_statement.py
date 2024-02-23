import certifi
import json
import requests
import csv

def get_company_profile(symbol, api_key, ano):
    url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{symbol}?periodo={ano}&apikey={api_key}"
    response = requests.get(url, verify=certifi.where())
    data = response.json()
    print(data)
    return data[0] if data else None

def main():
    api_key = "KwazJYS5ECjmKmvNI0M4lxrks33XyI0p"
    companies = [
        'ZM', 'NVDA', 'DOCU', 'SHOP', 'CRM', 'UBER', 'BKNG', 'AAL', 'CSCO', 'BA',  # Tecnologia
        'MRNA', 'TDOC', 'PFE', 'REGN', 'ABT', 'JNJ', 'HCA', 'UHS', 'CAH', 'THC',  # Saúde
        'AMZN', 'WMT', 'TGT', 'COST', 'KR', 'GPS', 'FL', 'M', 'TJX', 'SPG',  # Comércio
        'NFLX', 'ATVI', 'EA', 'SPOT', 'ROKU', 'LYV', 'DIS', 'CINE', 'AMC', 'SIX',  # Entretenimento
        'Z', 'EQR', 'AVB', 'PLD', 'AMT', 'HST', 'MAC', 'VNO', 'CCI', 'SLG'  # Imobiliário
    ]
    ano = 2022

    all_companies_info = []

    for company in companies:
        company_info = get_company_profile(company, api_key, ano)

        if company_info:
            # Adicionando um dicionário à lista para cada empresa
            company_info_dict = {
                "Symbol": company_info["symbol"],
                "Year": ano,
                "NetIncome": company_info['netIncome'],
                "DepreciationAndAmortization": company_info['depreciationAndAmortization'],
                "DeferredIncomeTax": company_info['deferredIncomeTax'],
                "StockBasedCompensation": company_info['stockBasedCompensation'],
                "ChangeInWorkingCapital": company_info['changeInWorkingCapital'],
                "AccountsReceivables": company_info['accountsReceivables'],
                "Inventory": company_info['inventory'],
                "AccountsPayables": company_info['accountsPayables'],
                "OtherWorkingCapital": company_info['otherWorkingCapital'],
                "OtherNonCashItems": company_info['otherNonCashItems'],
                "NetCashProvidedByOperatingActivities": company_info['netCashProvidedByOperatingActivities'],
                "InvestmentsInPropertyPlantAndEquipment": company_info['investmentsInPropertyPlantAndEquipment'],
                "AcquisitionsNet": company_info['acquisitionsNet'],
                "PurchasesOfInvestments": company_info['purchasesOfInvestments'],
                "SalesMaturitiesOfInvestments": company_info['salesMaturitiesOfInvestments'],
                "OtherInvestingActivites": company_info['otherInvestingActivites'],
                "NetCashUsedForInvestingActivites": company_info['netCashUsedForInvestingActivites'],
                "DebtRepayment": company_info['debtRepayment'],
                "CommonStockRepurchased": company_info['commonStockRepurchased'],
                "DividendsPaid": company_info['dividendsPaid'],
                "OtherFinancingActivites": company_info['otherFinancingActivites'],
                "NetCashUsedProvidedByFinancingActivities": company_info['netCashUsedProvidedByFinancingActivities'],
                "EffectOfForexChangesOnCash": company_info['effectOfForexChangesOnCash'],
                "NetChangeInCash": company_info['netChangeInCash'],
                "CashAtEndOfPeriod": company_info['cashAtEndOfPeriod'],
                "CashAtBeginningOfPeriod": company_info['cashAtBeginningOfPeriod'],
                "OperatingCashFlow": company_info['operatingCashFlow'],
                "CapitalExpenditure": company_info['capitalExpenditure'],
                "FreeCashFlow": company_info['freeCashFlow']
            }

            all_companies_info.append(company_info_dict)

    # Salvando a lista de dicionários em um arquivo CSV
    csv_file_path = "cash_flow_statement_info.csv"
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=company_info_dict.keys(), delimiter=',')
        csv_writer.writeheader()
        csv_writer.writerows(all_companies_info)

    print(f"Dados salvos em {csv_file_path}")

if __name__ == "__main__":
    main()
