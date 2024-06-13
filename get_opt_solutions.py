import os
import ast
import importlib.util
import os
import dataset
import time
import subprocess
import argparse


def run_code_solution(file_path, problem, execution_time_limit):
    cmd = ['python', file_path] + problem["A*_args"]
    
    killed = False
    not_executed = False
    error_message = None
    stdout, stderr = None, None
    execution_time = None

    try:
        # Run the process with a timeout
        start_time = time.time()
        completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, 
                                           stderr=subprocess.PIPE, 
                                           timeout=execution_time_limit)
        end_time = time.time()
        stdout, stderr = completed_process.stdout, completed_process.stderr
        execution_time = end_time - start_time

    except subprocess.TimeoutExpired:
        killed = True
        error_message = f"A* code was killed because it exceeded the time limit."
    except Exception as e:
        not_executed = True
        error_message = f"A* code returned the following error: " + str(e)

    if not killed and not not_executed:
        if stderr:
            not_executed = True
            error_message = f"A* code returned the following error: " + stderr.decode('ascii')
        elif not stdout:
            error_message = f"A* code executed successfully but no output produced by the LLM code."

    solution = stdout.decode('ascii') if stdout else None
    if not error_message and solution:
        try:
            solution = ast.literal_eval(solution)
        except:
            error_message = f"Error while parsing the output of A* code"

    return solution, killed, not_executed, error_message, execution_time


def get_opt_solutions(problem_type, execution_time_limit,
                      new_bench_file, print_stats):
    
    astar_file = "./{}/Astar_opt_solutions.py".format(problem_type)
    dataset_problem_type = import_from_path("dataset", './{}/dataset.py'.format(problem_type))
    problems = dataset_problem_type.get_problems()
    
    check = import_from_path("check", './{}/check.py'.format(problem_type))
    
    problems_opt_solutions = []
   
    for id, problem in problems.items():        
        (opt_solution, killed, not_executed, 
         error_message, execution_time) = run_code_solution(astar_file, problem,
                                                            execution_time_limit)
        should_halt = False
        message = ""
        # if there's a problem with executing the opt astar script
        if not opt_solution:
            message += "A* program returned None. " + str(error_message)
            should_halt = True 
        else:
            is_correct_opt, opt_cost = check.is_correct(*problem["is_correct_args"], opt_solution)
            if not is_correct_opt:
                message += "The A* program return an incorrect solution"
                should_halt = True
                    
        if should_halt:
            if print_stats:
                print("Id {}: {}".format(id, message))
            if "exceeded the time limit" in error_message:
                continue
            else:
                if print_stats:
                    print("unknown error in getting the optimal solution")
                raise
                
        problem["opt_solution"] = opt_solution
        problem["opt_solution_cost"] = opt_cost
        problem["opt_solution_compute_t"] = execution_time
        problem["solution_depth"] = len(opt_solution)
        if print_stats:
            print("Id {}: {}".format(id, (opt_solution, opt_cost, execution_time)))
            
        problems_opt_solutions.append(problem)
            
    problems_opt_solutions = [x.update(diff_sorted_id=i+1) or x for i, x in enumerate(problems_opt_solutions)]
    
    searchbench = problems_opt_solutions
    if os.path.exists(new_bench_file):
        if os.path.getsize(new_bench_file) > 0:
                searchbench = dataset.load_reverse_stringify_searchbench(new_bench_file)
                searchbench = searchbench + problems_opt_solutions
    dataset.sort_write_searchbench(searchbench, new_bench_file)



def import_from_path(module_name, path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description="Generates the optimal solution for new instances of the SearchBench dataset using a pre-implemented A* algorithm with an admissible and consistent heuristic.")
    parser.add_argument(
        '--Astar_execution_time_limit',
        type=int,
        default=600,
        help="Run time limit for the pre-implemented A* algorithm to find the optimal solution, in seconds."
    )
    parser.add_argument(
        '--problem_type',
        choices=["8_puzzle", "8_puzzle_words", "coin_exchange", "water_jug", "color_sorting", "restricted_sorting", "magic_square", "consecutive_grid", "traffic", "city_directed_graph", "trampoline_matrix"],
        required=True,
        help="The problem type for which new instances are generated. The script calculates the optimal solution for instances of one problem type per run."    )
    
    parser.add_argument(
        '--print_stats',
        type=bool,
        default=True,
        help="Flag to print the optimal solution to each instance after the A* algorithm finishes running."
    )

    parser.add_argument(
        '--path_to_new_instances_jsonl',
        type=str,
        required=True,
        help="Path to the new bench jsonl file that constains the new instances."
    )
    args = parser.parse_args()
    
    
    get_opt_solutions(args.problem_type, args.Astar_execution_time_limit,
                      args.path_to_new_instances_jsonl, args.print_stats)
  
main()      

