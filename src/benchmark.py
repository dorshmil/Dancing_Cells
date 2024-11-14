import os

# base path to the xcc benchmarks folder
BENCHMARK = '../benchmarks/xcc-benchmarks'
# list all the bencmark files available
benchmark_files = os.listdir(BENCHMARK)

def option_thirdly(option):
    '''returns all the items that has ':' in them for a given option'''
    result = set()
    for item in reversed(option):  # Start checking from the end
        s = item.split(':')
        if len(s) == 1:
            return result
        else:
            result.add(s[0])

def thirdly_items(options):
    '''
    returns a set of all the thirdly items
    thirdly items are secondery items who has spacific color
    meaning, is some option the item appear like this item:color
    '''
    # join all the thirdly items sets
    return set.union(
        # the * unpack the sets of thirdly
        *map(
            # find the thirdly items in each option
            lambda option: option_thirdly(option), options
            )
        )

def load_benchmark(file_name):
    '''
    load benchmarks file in the format:
    [primery_items, secondery_items(if there is any), thirdly_items], options
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

        # seperate thirdly items if there is any
        if len(items) == 2:
            thirdly = thirdly_items(options)
            # update the secondery items to not inclue the thirdly items
            items[1] = list(thirdly.symmetric_difference(items[1]))
            # add the thirdly items
            items.append(list(thirdly))

    return items, options