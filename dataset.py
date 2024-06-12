import json

def reverse_stringify_top_level_values(obj):
    if isinstance(obj, dict):
        reversed_obj = {}
        for k, v in obj.items():
            if isinstance(v, str):
                try:
                    # Attempt to parse the string back to its original type
                    reversed_obj[k] = json.loads(v)
                except (json.JSONDecodeError, TypeError):
                    # If parsing fails, keep the value as a string
                    reversed_obj[k] = v
            else:
                reversed_obj[k] = v
        return reversed_obj
    return obj


def load_reverse_stringify_searchbench(searchbench_file_path):
    searchbench = []
    with open(searchbench_file_path, 'r') as file:
        for line in file:
            json_obj = json.loads(line)
            reversed_json_obj = reverse_stringify_top_level_values(json_obj)
            searchbench.append(reversed_json_obj)   
    return searchbench     

def get_problem_types(return_all, problem_types, searchbench_file_path = "./SearchBench.jsonl"):
    searchbench_full = load_reverse_stringify_searchbench(searchbench_file_path)
    if return_all:
        return searchbench_full
    searchbench_subset = [instance for instance in searchbench_full if instance["problem_type"] in problem_types]
    return searchbench_subset
            
            
def stringify_top_level_values(obj):
    if isinstance(obj, dict):
        return {k: json.dumps(v) if not isinstance(v, str)
                else v for k, v in obj.items()}
    return obj

def sort_write_searchbench(searchbench_list, searchbench_file_path):
    searchbench_list.sort(key=lambda x: (x['diff_sorted_id'], x['problem_type']))
    with open(searchbench_file_path, 'w') as outfile:
        for problem in searchbench_list:
            stringified_json_obj = stringify_top_level_values(problem)
            outfile.write(json.dumps(stringified_json_obj) + '\n')

    