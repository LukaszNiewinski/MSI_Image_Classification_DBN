import json
with open('data.txt') as f:
    print("\033[1m{:<20}{:<15} {:<15} {:<20} \033[0m".format('Hidden structure', 'Num of epochs', 'Batch size', "Accuracy"))
    json_data = json.load(f)
    for line in json_data:
        if line['batch_size'] == 32 and line['h_structure'] == [32,32]:
            print("{:<5}x  {:<12}{:<15} {:<15} {:<20.10f} ".format(line['h_structure'][0], line['h_structure'][1], line['n_epochs'], line['batch_size'], line['accuracy']))
