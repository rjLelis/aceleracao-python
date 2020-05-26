from datetime import datetime, timedelta

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


def classify_by_phone_number(records):
    encargo_permanente = 0.36
    taxa_diurna = 0.09
    taxa_noturna = 0.00

    tarifacoes = {}
    for record in records:
        start = datetime.fromtimestamp(record['start'])
        end = datetime.fromtimestamp(record['end'])
        diff = end - start
        minutos = diff.total_seconds() // 60

        if start.hour >= 6 and end.hour <= 22:
            taxa_total = minutos * taxa_diurna
        else:
            taxa_total = minutos * taxa_noturna
        taxa_total += encargo_permanente

        source = record['source']
        if source in tarifacoes:
            tarifacoes[source] += taxa_total
        else:
            tarifacoes[source] = taxa_total

    new_records = []
    for source, total in tarifacoes.items():
        new_records.append({
            'source': source,
            'total': round(total, 2)
        })

    new_records = sorted(new_records, key=lambda k: k['total'], reverse=True)

    return new_records

if __name__ == "__main__":
    results = classify_by_phone_number(records)
    print(results)
