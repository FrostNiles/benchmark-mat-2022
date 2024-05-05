
skipped = {}

for i in range(1, 13):
    if i in skipped:
        continue
    # check the results if there is a deviation
    for j in [10, 20]:
        for k in range(1, j+1):   
            with open(f'test_data/result/result_data_{i}_dim_{j}_number_of_element_{k}.txt', 'r') as file:
                result = file.read()
            # if not "deviation:" in result:
            # sys.exit()
            result = result.split('deviation:')
            print(i, j, k)
            print(result[1])