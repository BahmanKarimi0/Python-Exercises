import json
import csv
import os


def source(txt_file):
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    reader = json.loads(line.strip())
                    yield reader
                except json.decoder.JSONDecodeError:
                    print('Invalid data')
    except GeneratorExit:
        print('source coroutine closed')
        raise


def validator():
    while True:
        item = yield
        try:
            while (isinstance(item, dict) and 'id' in item and isinstance(item['id'], str)
                   and 'type' in item and isinstance(item['type'], str)
                   and 'amount' in item and isinstance(item['amount'], (int, float))):
                item = yield item
        except GeneratorExit:
            print('validator coroutine closed')
            raise


def analyzer(target_type):
    stats = {}
    while True:
        item = yield
        try:
            while item == 'stats':
                item = yield stats
            while isinstance(item, dict) and item['type'] == target_type:
                stats[item['id']] = stats.get(item['id'], {'total': 0, 'count': 0})
                stats[item['id']]['total'] += float(item['amount'])
                stats[item['id']]['count'] += 1
                item = yield item
        except GeneratorExit:
            print('analyzer coroutine closed')
            raise


def recorder(csv_file):
    row_count = 0
    header = False
    item_header = False
    while True:
        try:
            item = yield
            if item == 'stats':
                stats = a.send('stats')
                try:
                    with open(csv_file, 'a', encoding='utf-8', newline='') as f:
                        writer = csv.writer(f)
                        if not header:
                            writer.writerow(['id', 'total', 'count'])
                            header = True
                        for id_, data in stats.items():
                            writer.writerow([id_, data['total'], data['count']])

                except (FileNotFoundError, PermissionError, IOError):
                    print('File error')
            else:
                try:
                    with open(csv_file, 'a', encoding='utf-8', newline='') as f:
                        writer = csv.writer(f)
                        if not item_header:
                            writer.writerow(['id', 'amount'])
                            item_header = True
                        writer.writerow([item['id'], item['amount']])
                        row_count += 1
                except (FileNotFoundError, PermissionError, IOError):
                    print('File error')
            yield row_count
        except GeneratorExit:
            print('recorder coroutine closed')
            raise


s = source("transactions.txt")
v = validator()
a = analyzer("sale")
r = recorder("sales.csv")

next(r)
next(a)
next(v)
for item in s:
    valid_item = v.send(item)
    if valid_item is not None:
        analyzed_item = a.send(valid_item)
        if analyzed_item is not None:
            r.send(analyzed_item)
            next(r)
print(r.send("stats"))
