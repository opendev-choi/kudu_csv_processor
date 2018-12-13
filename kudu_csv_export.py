import csv
import datetime
import argparse

import kudu


def args_parse() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()

    # arguments setting
    parser.add_argument("-i", "--ip", help="target kudu ip address", required=True)
    parser.add_argument("-t", "--table", help="target kudu table name", required=True)
    parser.add_argument("-f", "--file", help="export file name", required=True)
    parser.add_argument("-p", "--port", help="target kudu port", required=False, default=7051, type=int)

    return parser.parse_args()


if __name__ == '__main__':
    print(f'| start at {datetime.datetime.now():%Y-%m-%d %H:%M:%S}')
    start_time: datetime.datetime = datetime.datetime.now()

    args: argparse.Namespace = args_parse()

    client: kudu.Client = kudu.connect(args.ip, args.port)
    ss: kudu.Session = client.new_session()
    tb_reader = client.table(args.table).scanner()

    tb_reader.open()

    with open(args.file, 'w') as csv_file:
        print(f'| CSV file name : {args.file}')
        cnt: int = 0

        csv_writer: csv.writer = csv.writer(csv_file, delimiter=',', quotechar='\'')
        while tb_reader.has_more_rows():
            for row in tb_reader.next_batch().as_tuples():
                csv_writer.writerow(list(row))
                cnt += 1
            print(f'\r| now writing {cnt} row / '
                  f'elapse time {(datetime.datetime.now() - start_time).total_seconds():.2f} sec', end='\r')
        print(f'| end process / {cnt}')

