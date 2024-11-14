import os

# base path to the xcc benchmarks folder
BENCHMARK = '../benchmarks/xcc-benchmarks'
# list all the bencmark files available
benchmark_files = os.listdir(BENCHMARK)

def load_benchmark(file_name):
    '''
    load benchmarks file in the format:
    [primery_items, secondery_items(if there is any)], options
    '''
    with open(f'{BENCHMARK}/{file_name}', 'r') as file:
        lines = file.readlines()
        # remove commented lines (lines that start with '|')
        for i,line in enumerate(lines):
            if not line.startswith('|'):
                break
        lines = lines[i:]
        # the first line includes the items and all following rows are the options
        items_str = lines.pop(0).strip()
        # '|' seperates primery and secondery items
        items = [s.split() for s in items_str.split('|')]
        # create the options by splitting the spaces
        options = list(map(lambda s: s.strip().split() ,lines))
    return items, options