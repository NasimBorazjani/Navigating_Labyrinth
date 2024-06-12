import os
import subprocess
from threading import Timer
import time
import ast
import ast
import importlib.util
import re
import os
from openai import OpenAI
from datetime import datetime
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import dataset

stream = False

Zero_shot_text_prompt = """Solve the problem below step-by-step, using only text. The solution should be presented right after the phrase /answer_list/. Ensure there is no text following the reported solution. The solution should be formatted as a Python list, and each element in the list should be of the type specified in the problem.

"""

Text_intro_prompt = """The objective is to solve the problems below step-by-step, using only text. The solution should be presented right after the phrase /answer_list/. Ensure there is no text following the reported solution. The solution should be formatted as a Python list, and each element in the list should be of the type specified in the problem.

"""
Text_8_puzzle = """In the 8-puzzle game, you are given a grid with numbered square tiles arranged randomly and one tile missing. The goal is to arrange the tiles in descending order by sliding them into the empty space. The tiles can move in 4 directions: left, right, up, and down.  Given the initial state of the puzzle below, where the empty spot is represented as “_”, provide the shortest list of tiles that need to be swapped with the empty spot to achieve the goal state. The goal state is when all tiles are in descending order, with the largest number in the top left corner, and the empty spot is in the bottom right corner. The solution should be a list of numbers in Python format, where each number represents the number on the tile that the empty spot is swapped with at each turn. Initial state of the puzzle: [[55, 43, 17], [97, 35, 9], [12, 25, '_']]

The goal state of the puzzle is [[97, 55, 43], [35, 25, 17], [12, 9, '_']].

To achieve this, we need to follow these steps:

1. Swap 9 with '_': [[55, 43, 17], [97, 35, '_'], [12, 25, 9]]
2. Swap 17 with '_': [[55, 43, '_'], [97, 35, 17], [12, 25, 9]]
3. Swap 43 with '_': [[55, '_', 43], [97, 35, 17], [12, 25, 9]]
4. Swap 55 with '_': [['_', 55, 43], [97, 35, 17], [12, 25, 9]]
5. Swap 97 with '_': [[97, 55, 43], ['_', 35, 17], [12, 25, 9]]
6. Swap 35 with '_': [[97, 55, 43], [35, '_', 17], [12, 25, 9]]
7. Swap 25 with '_': [[97, 55, 43], [35, 25, 17], [12, '_', 9]]
8. Swap 9 with '_': [[97, 55, 43], [35, 25, 17], [12, 9, '_']]

So, the list of tiles that need to be swapped with the empty spot to achieve the goal state is [9, 17, 43, 55, 97, 35, 25, 9].

The answer is /answer_list/[9, 17, 43, 55, 97, 35, 25, 9]

"""
Text_color_sorting = """The game of 'Sort It' begins with 3 tubes, each filled with balls of different colors. The goal is to sort the balls by color, with each tube containing balls of only one color. Only one ball can be moved at a time, taken from the top of one tube and placed on top of another. All of the tubes have the same capacity of 6 balls. It is not allowed to place a ball in a tube that is already at capacity. The solution should be a list of tuples, each containing, first, the index of the tube from which a ball is taken and, second, the index of the tube to which it is moved, indexing from 0. Given the initial state of the tubes, represented by the lists below (with the leftmost item being the color of the topmost ball in each tube), what is the shortest list of move tuples that will result in all the balls being correctly sorted? [['Green', 'Red', 'Green', 'Red'], ['Blue', 'Blue', 'Red', 'Green'], ['Red', 'Blue', 'Green', 'Blue']]

The initial state of the tubes is:

Tube 0: ['Green', 'Red', 'Green', 'Red']
Tube 1: ['Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Red', 'Blue', 'Green', 'Blue']

The goal is to sort the balls by color, with each tube containing balls of only one color. The moves are as follows:

1. Move 'Green' from Tube 0 to Tube 2: (0, 2)
The state of the tubes now is:
Tube 0: ['Red', 'Green', 'Red']
Tube 1: ['Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Green', 'Red', 'Blue', 'Green', 'Blue']

2. Move 'Red' from Tube 0 to Tube 1: (0, 1)
Tube 0: ['Green', 'Red']
Tube 1: ['Red', 'Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Green', 'Red', 'Blue', 'Green', 'Blue']

3. Move 'Green' from Tube 0 to Tube 2: (0, 2)
Tube 0: ['Red']
Tube 1: ['Red', 'Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Green', 'Green', 'Red', 'Blue', 'Green', 'Blue']

4. Move 'Red' from Tube 1 to Tube 0: (1, 0)
Tube 0: ['Red', 'Red']
Tube 1: ['Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Green', 'Green', 'Red', 'Blue', 'Green', 'Blue']

5. Move 'Green' from Tube 2 to Tube 1: (2, 1)
Tube 0: ['Red', 'Red']
Tube 1: ['Green', 'Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Green', 'Red', 'Blue', 'Green', 'Blue']

6. Move 'Green' from Tube 2 to Tube 1: (2, 1)
Tube 0: ['Red', 'Red']
Tube 1: ['Green', 'Green', 'Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Red', 'Blue', 'Green', 'Blue']

7. Move 'Red' from Tube 2 to Tube 1: (2, 0)
Tube 0: ['Red', 'Red', 'Red']
Tube 1: ['Green', 'Green', 'Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Blue', 'Green', 'Blue']

8. Move 'Green' from Tube 1 to Tube 0: (1, 0)
Tube 0: ['Green', 'Red', 'Red', 'Red']
Tube 1: ['Green', 'Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Blue', 'Green', 'Blue']

9. Move 'Green' from Tube 1 to Tube 0: (1, 0)
Tube 0: ['Green', 'Green', 'Red', 'Red', 'Red']
Tube 1: ['Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Blue', 'Green', 'Blue']

10. Move 'Blue' from Tube 2 to Tube 1: (2, 1)
Tube 0: ['Green', 'Green', 'Red', 'Red', 'Red']
Tube 1: ['Blue', 'Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Green', 'Blue']

11. Move 'Green' from Tube 2 to Tube 0: (2, 0)
Tube 0: ['Green', 'Green', 'Green', 'Red', 'Red', 'Red']
Tube 1: ['Blue', 'Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Blue']

12. Move 'Blue' from Tube 1 to Tube 2: (1, 2)
Tube 0: ['Green', 'Green', 'Green', 'Red', 'Red', 'Red']
Tube 1: ['Blue', 'Blue', 'Red', 'Green']
Tube 2: ['Blue', 'Blue']

13. Move 'Blue' from Tube 1 to Tube 2: (1, 2)
Tube 0: ['Green', 'Green', 'Green', 'Red', 'Red', 'Red']
Tube 1: ['Blue', 'Red', 'Green']
Tube 2: ['Blue', 'Blue', 'Blue',]

14. Move 'Blue' from Tube 1 to Tube 2: (1, 2)
Tube 0: ['Green', 'Green', 'Green', 'Red', 'Red', 'Red']
Tube 1: ['Red', 'Green']
Tube 2: ['Blue', 'Blue', 'Blue', 'Blue']

15. Move 'Red' from Tube 1 to Tube 2: (1, 2)
Tube 0: ['Green', 'Green', 'Green', 'Red', 'Red', 'Red']
Tube 1: ['Green']
Tube 2: ['Red', 'Blue', 'Blue', 'Blue', 'Blue']

16. Move 'Green' from Tube 0 to Tube 1: (0, 1)
Tube 0: ['Green', 'Green', 'Red', 'Red', 'Red']
Tube 1: ['Green', 'Green']
Tube 2: ['Red', 'Blue', 'Blue', 'Blue', 'Blue']

17. Move 'Green' from Tube 0 to Tube 1: (0, 1)
Tube 0: ['Green', 'Red', 'Red', 'Red']
Tube 1: ['Green', 'Green', 'Green']
Tube 2: ['Red', 'Blue', 'Blue', 'Blue', 'Blue']

18. Move 'Green' from Tube 0 to Tube 1: (0, 1)
Tube 0: ['Red', 'Red', 'Red']
Tube 1: ['Green', 'Green', 'Green', 'Green']
Tube 2: ['Red', 'Blue', 'Blue', 'Blue', 'Blue']

19. Move 'Red' from Tube 2 to Tube 0: (2, 0)
Tube 0: ['Red', 'Red', 'Red', 'Red']
Tube 1: ['Green', 'Green', 'Green', 'Green']
Tube 2: ['Blue', 'Blue', 'Blue', 'Blue']


The final state of the tubes is:

Tube 0: ['Red', 'Red', 'Red', 'Red']
Tube 1: ['Green', 'Green', 'Green', 'Green']
Tube 2: ['Blue', 'Blue', 'Blue', 'Blue']

So, the shortest list of move tuples that will result in all the balls being correctly sorted is [(0, 1), (0, 2), (1, 0), (2, 1), (2, 1), (2, 0), (1, 0), (1, 0), (2, 1), (2, 0), (1, 2), (1, 2), (1, 2), (1, 2), (0, 1), (0, 1), (0, 1), (2, 0)].

The answer is /answer_list/[(0, 1), (0, 2), (1, 0), (2, 1), (2, 1), (2, 0), (1, 0), (1, 0), (2, 1), (2, 0), (1, 2), (1, 2), (1, 2), (1, 2), (0, 1), (0, 1), (0, 1), (2, 0)]

"""
Text_water_jug = """Given 6 labeled water jugs with capacities 37, 133, 38, 72, 41, 23, 122 liters, we aim to fill 3 unlabeled buckets, numbered 1 to 3 and arranged in a line in ascending order, with 195, 224, 268 liters of water respectively. The amount of water in each unlabeled bucket can not at any point in time exceed the amount of water in the bucket placed before it. Jugs can only be filled to the top and emptied completely, and the unlabeled buckets cannot be overfilled. An action, represented as a tuple ('+', X, Y) or ('-', X, Y), involves adding to or removing water from the unlabeled bucket numbered Y, using the jug with capacity X. Determine the shortest sequence of actions needed to fill the buckets as specified, and present the solution as a list of action tuples in Python syntax.


The problem can be solved using a greedy algorithm. The idea is to start filling the last bucket that has not been filled yet in order to not violate the constraint on the relative amount of water in the buckets based on their order. Here are the steps to solve the problem:

1. Start with the last bucket (bucket 3) and find the largest jug that can be used to fill it without overfilling it or making it difficult to fill the remaining capacity using the given jugs. In this case, the largest jug that can be used is the 122-liter jug. So, the first action is ('+', 122, 3).

2. Repeat the process for the same bucket (bucket 3) until it is filled with 268 liters of water. Each time, find the largest jug that can be used without overfilling the bucket. The actions are ('+', 72, 3), ('+', 37, 3), ('+', 37, 3).

3. Move to the next bucket (bucket 2) and repeat the process until the bucket is filled with 224 liters of water. The actions are ('+', 122, 2),('+', 41, 2),('+', 38, 2), ('+', 23, 2).

4. Move to the last bucket (bucket 1) and repeat the process until the bucket is filled with 195 liters of water. The greedy actions are ('+', 122, 1),  ('+', 72, 1).

5. However, the last bucket (bucket 1) is filled with 194 liters, 1 liter less than required. Since there is no 1 liter jug, the 38 liter jug can be used to add water, then 37 liters is removed using the 37 liter jug, adding a net of 1 liter to the bucket. We can not use the 38 liter jug to add water after filling the bucket with 194 liters of water because it will overflow. Thus the order of actions to fill the last bucket is: ('+', 122, 1), ('+', 72, 1), ('-', 37, 1), ('+', 38, 1).

The final sequence of actions is [('+', 122, 3), ('+', 72, 3), ('+', 37, 3), ('+', 37, 3), ('+', 122, 2),('+', 41, 2),('+', 38, 2), ('+', 23, 2), ('+', 122, 1),  ('+', 38, 1), ('-', 37, 1), ('+', 72, 1)].

The answer is /answer_list/[('+', 122, 3), ('+', 72, 3), ('+', 37, 3), ('+', 37, 3), ('+', 122, 2),('+', 41, 2),('+', 38, 2), ('+', 23, 2), ('+', 122, 1), ('+', 72, 1), ('-', 37, 1), ('+', 38, 1)]

"""
Text_traffic = """Using the provided matrix map of a city, where numbers represent travel time in minutes (all numbers are positive integers) and 'x' marks closed workshops, find the quickest route for Ben to travel from his current workshop at index (3, 8) to his destination workshop at index (6, 1), indexing from 0. Ben's car can move north, south, east, or west from a given crossroad, provided there's no x in that direction. Also, there are 3 districts in the city with district 1 covering rows 0 to 3, district 2 covering rows 4 to 5, and district 3 covering rows 6 to 8. Ben has to visit at least 1 workshop in each district on his path to the destination. The roads are bidirectional. The answer should be a list of tuples (in Python syntax) indicating the index of workshops on Ben's path. The start and end workshops must be included in the path.
[19 x 1 x 2 17 x x x]
[x x 14 x 11 x x 18 x]
[19 x 19 7 x 6 x x x]
[6 x x 3 x 8 10 x 16]
[3 7 x 14 x 10 9 6 15]
[13 x 6 1 x x x 12 14]
[x 8 5 16 14 x 10 5 16]
[18 4 9 1 11 9 9 18 13]
[x x 16 13 16 x 17 x 11]


Ben starts at index (3, 8), which is in district 1. The quickest route to his destination at index (6, 1) that includes at least one workshop in the remaining two districts that he hasn’t visited yet, districts 2 and 3, is as follows:

1. Move south to index (4, 8) with a travel time of 15 minutes. Now Ben has visited district 2 as well as district 1.
2. Move west to index (4, 7) with a travel time of 6 minutes.
3. Move south to index (5, 7) with a travel time of 12 minutes.
4. Move south to index (6, 7) with a travel time of 5 minutes. Now Ben has visited all 3 districts.
5. Move west to index (6, 6) with a travel time of 10 minutes.
6. Move south to index (7, 6) with a travel time of 9 minutes.
7. Move west to index (7, 5) with a travel time of 9 minutes.
8. Move west to index (7, 4) with a travel time of 11 minutes.
9. Move west to index (7, 3) with a travel time of 1 minute.
10. Move west to index (7, 2) with a travel time of 9 minutes.
11. Move west to index (7, 1) with a travel time of 4 minutes.
12. Move north to index (6, 1) with a travel time of 8 minutes. This is Ben's destination workshop.

So, the quickest route, that crosses all 3 districts, for Ben to travel from his current workshop at index (3, 8) to his destination workshop at index (6, 1) is [(0, 2), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (5, 2), (6, 2), (7, 2), (7, 1), (7, 0)]. 

The answer is /answer_list/[(3, 8), (4, 8), (4, 7), (5, 7), (6, 7), (6, 6), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1)]

"""
Text_magic_square = """In the magic square problem, a 4x4 grid is filled with unique integers ranging from 29 to 54. Some numbers are already given, while others are unknown and represented as 'x'. The sums of columns 1 to 2 (counting from 0) must be 148, 196 respectively, and the sums of rows 1 to 2 must be 187, 149 respectively. Also, the sum of the numbers in the diagonal from the top left to the bottom right corner of the grid should equal 166. The goal is to find unique integers in the given range to replace with ‘x’s in the grid below such that the sum of the specified rows, columns, and diagonal equals the given amounts and the sum of all of the numbers in the grid is as low as possible. The solution should be provided as a list of tuples in Python syntax. Each tuple should contain three numbers: the row index, the column index (both starting from 0), and the value of the unknown number at that position.\n\nGrid:\n [['47' 'x' 'x' '32']\n ['x' 'x' 'x' '49']\n ['x' '31' '50' 'x']\n ['x' 'x' '52' '30']]

Step 1: The sum of the diagonal is given with only 1 element missing (in index (1, 1)). The sum of the diagonal is 166 and the known values in the diagonal are 47, 50, and 30. So, the missing value is 166 - 47 - 50 - 30 = 39. So, we fill the position (1, 1) with 39.

Grid after Step 1:
 [['47' 'x' 'x' '32']
 ['x' '39' 'x' '49']
 ['x' '31' '50' 'x']
 ['x' 'x' '52' '30']]

Step 2: The sum of the first row is 187 and the known values in the first row are 39 and 49. So, the sum of the missing values is 187 - 49 - 39 = 99. We fill the missing values with the unique integers that sum to 99, which are 46 and 53. So, we fill the positions (1, 0) and (1, 2) with 46 and 53 respectively.

Grid after Step 2:
 [['47' 'x' 'x' '32']
 ['46' '39' '53' '49']
 ['x' '31' '50' 'x']
 ['x' 'x' '52' '30']]

Step 3: The sum of the second column is given with only 1 element missing (in index (0, 2)). The sum of the second column is 196 and the known values in the diagonal are 53, 50, and 52. So, the missing value is 196 - 53 - 50 - 52 = 41. So, we fill the position (0, 2) with 41.

Grid after Step 3:
 [['47' 'x' '41' '32']
 ['46' '39' '53' '49']
 ['x' '31' '50' 'x']
 ['x' 'x' '52' '30']]

Step 4: The sum of the second row is 149 and the known values in the second row are 31 and 50. So, the sum of the missing values is 149 - 31 - 50 = 68. We fill the missing values with the unique integers that sum to 68, which are 33 and 35. So, we fill the positions (2, 0) and (2, 3) with 33 and 35 respectively.

Grid after Step 4:
 [['47' 'x' '41' '32']
 ['46' '39' '53' '49']
 ['33' '31' '50' '35']
 ['x' 'x' '52' '30']]

Step 5: The sum of the first column is 148 and the known values in the first column are 39 and 31. So, the sum of the missing values is 148 - 31 - 39 = 78. We fill the missing values with the unique integers that sum to 78, which are 34 and 44. So, we fill the positions (0, 1) and (3, 1) with 34 and 44 respectively.

Grid after Step 5:
 [['47' '34' '41' '32']
 ['46' '39' '53' '49']
 ['33' '31' '50' '35']
 ['x' '44' '52' '30']]

Step 6: There is 1 unknown number left in the grid at position (3,0). We must fill this cell with the smallest unique integer which is 29.

Grid after Step 6:
 [['47' '34' '41' '32']
 ['46' '39' '53' '49']
 ['33' '31' '50' '35']
 ['29' '44' '52' '30']]

So, the solution is [(0, 1, 34), (0, 2, 41), (1, 0, 46), (1, 1, 39), (1, 2, 53), (2, 0, 33), (2, 3, 35), (3, 0, 29), (3, 1, 44)].

The answer is /answer_list/[(0, 1, 34), (0, 2, 41), (1, 0, 46), (1, 1, 39), (1, 2, 53), (2, 0, 33), (2, 3, 35), (3, 0, 29), (3, 1, 44)]


"""
Text_inst_prompt = """Solve the problem below in the same format, step-by-step, using only text.

####
"""

def get_model_response(system_input, user_input, model_name, 
                        llama_model, tokenizer, openai_key,
                        temp=0, max_tokens=1000):
    if model_name == "gpt4" or model_name == "gpt3.5":
        if model_name == "gpt4":
            model_name = "gpt-4"
        elif model_name == "gpt3.5":
            model_name = "gpt-3.5-turbo"
            
        client = OpenAI(
            api_key=openai_key,
        )
            
        response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": system_input + user_input
            }
        ],
        temperature=temp,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        response = response.choices[0].message.content
    
    elif "llama" in model_name:
        chat = [
        {"role": "system", "content": system_input},
        {"role": "user", "content": user_input},
        ]
        inputs = tokenizer.apply_chat_template(chat, return_tensors="pt").to("cuda")
        output = llama_model.generate(input_ids=inputs, max_new_tokens=max_tokens, temperature=temp)
        output = output[0].to("cpu")
        response = tokenizer.decode(output)
    
    return response


def get_llm_solution(problem, model_name, 
                    prompting_method, max_tokens,
                    llama_model, tokenizer, openai_key):    
    
    if prompting_method == "0shot_text":
        system_input = Zero_shot_text_prompt
        user_input = problem["problem_statement"]
    else:
        system_input = Text_intro_prompt
        if problem["problem_category"] == "puzzle":
            user_input = (Text_color_sorting + Text_water_jug + 
                          Text_traffic + Text_magic_square)
        elif problem["problem_category"] == "sorting":
            user_input = (Text_8_puzzle + Text_water_jug + 
                          Text_traffic + Text_magic_square)
        elif problem["problem_category"] == "subset_sum":
            user_input = (Text_8_puzzle + Text_color_sorting + 
                          Text_traffic + Text_magic_square)
        elif problem["problem_category"] == "pathfinding":
            user_input = (Text_8_puzzle + Text_color_sorting + 
                         Text_water_jug + Text_magic_square)
        elif problem["problem_category"] == "underdetermined_system":
            user_input = (Text_8_puzzle + Text_color_sorting + 
                           Text_water_jug + Text_traffic)
        user_input += Text_inst_prompt.replace("####", '"' + problem["problem_statement"] + '"')
    
    tries = 10
    while tries >= 0:
        try:
            response = get_model_response(system_input, user_input, model_name, 
                                        llama_model, tokenizer, openai_key,
                                        temp=0, max_tokens=max_tokens)
            break
        except Exception as e:
            if tries == 0:
                raise 
            else:
                # Wait a few seconds before retrying 
                time.sleep(6) 
                if "maximum context length" in str(e):
                    num_tokens_context = re.findall(r'-?\b\d+\b', str(e))[3]
                    max_tokens = 8192 - int(num_tokens_context)
                tries -= 1
                continue
    
    error_message = ""
    try:
        matches = re.search(r'/answer_list/\s*(.*)', response).group(1)
        answer_list = ast.literal_eval(matches)
        if answer_list:
            correct_format = True
            answer_llm = answer_list
            
        else:
            correct_format = False
            error_message = "No list of actions in the llm solution"

    except:
        correct_format = False
        error_message = "Failed to map the elements in the list to the indicated problem state data type"
    
    if not correct_format:    
        answer_llm = None
        
    return correct_format, response, answer_llm, error_message

     
def final_record(log_file, count_feasible, count_correct, 
                count_optimal, count_incomplete, count_killed, 
                count_not_executed, dict_llm_sol,
                infeasible_ids, total_number_calls, num_problems):
     #log problems that were not solved due to incorrect formatting
    f = open(log_file, "a")   
    f.write("\n" + "-"*50 + "\n")
    f.write("ID of problems with infeasible solution")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(infeasible_ids))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count feasible solutions")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_feasible) + " \ " + str(num_problems))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count correct solutions")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_correct) + " \ " + str(num_problems))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count correct solutions with optimum cost")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_optimal) + " \ " + str(num_problems))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count program killed")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_killed) + " \ " + str(num_problems))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count program not executed")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_not_executed) + " \ " + str(num_problems))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("count code generation incomplete")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(count_incomplete) + " \ " + str(num_problems))
    
    f.write("\n" + "-"*50 + "\n")
    f.write("""dict {id of the problem: \n
            llm correct solution, cost correct solution, excecution time of the llm code} \n""")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(dict_llm_sol))
    
    #total number of calls to LLM
    f.write("\n\n")
    f.write("\n" + "-"*50 + "\n")
    f.write("total number of calls to LLM")
    f.write("\n" + "-"*50 + "\n")
    f.write(str(total_number_calls))

    
   
def record(id, log_file, llm_solution, problem, reponse_llm, report):
    f = open(log_file, "a")
    f.write("ID: " + str(id) + "\n" + str(problem) + "\n")
    f.write(report + "\n")
    f.write(str(reponse_llm)+ "\n")
    f.write("llm code run result: " + str(llm_solution) + "\n\n\n\n")
    f.close()

def get_solutions(problems, model_name, log_file, 
                problem_types_action_type,
                max_tokens, llama_model, tokenizer,
                prompting_method, print_stats, openai_key):
    count_feasible = 0
    count_correct = 0
    count_optimal = 0
    count_incomplete = 0
    count_killed = 0
    count_not_executed = 0
    dict_llm_sol = {}
    infeasible_ids = []
    total_number_calls = 0
        
    for problem in problems:
                
        (correct_format, response, 
         answer_llm, error_message) = get_llm_solution(problem, model_name, 
                                                        prompting_method, max_tokens,
                                                        llama_model, tokenizer, openai_key)
        
        total_number_calls += 1
        
        id = (problem["problem_type"], problem["diff_sorted_id"])

        #incorrect solution type or code is not executable or format of the llm solution does not fit the expected format:
        if error_message:
            infeasible_ids.append(id)
            record(id, log_file, answer_llm, problem, response, error_message)
            if print_stats:
                print("Id {}: {}".format(id, error_message))
        
        elif (not type(answer_llm) is list or
            not (all(isinstance(item, problem_types_action_type[problem["problem_type"]])
            for item in answer_llm))): 
            infeasible_ids.append(id)
            message = "Incorrect solution type"
            record(id, log_file, answer_llm, problem, response, message)
            if print_stats:
                print("Id {}: {}".format(id, message))
        
        else:
            check = import_from_path("check", './{}/check.py'.format(problem["problem_type"]))
            message = ""
            #check feasibility and correctness and record cost of the solution for given problem
            if check.is_feasible(*problem["is_feasible_args"], answer_llm):
                count_feasible += 1
                message += "LLM solution is feasible!! "
            else:
                message += "LLM solution is NOT feasible "
                infeasible_ids.append(id)
            
            is_correct, cost = check.is_correct(*problem["is_correct_args"], answer_llm)
            if is_correct:
                count_correct += 1
                message += "LLM solution is correct!! "
                
                if cost == problem["opt_solution_cost"]:
                    count_optimal += 1
                    message += "LLM solution is optimal!!"
                else:
                    message += "LLM solution is NOT optimal "
                    
                dict_llm_sol[id] = (answer_llm, cost)

            else:
                message += "LLM solution is NOT correct "
                
            if print_stats:
                print("Id {}: {}".format(id, message))
            record(id, log_file, answer_llm, problem, response, message)
        
    return (count_feasible, count_correct, count_optimal, count_incomplete, 
                    count_killed, count_not_executed, dict_llm_sol,
                    infeasible_ids, total_number_calls) 


def import_from_path(module_name, path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_experiment(prompting_method, model_name, 
                   problems, max_tokens, 
                   problem_types_action_type, 
                   print_stats, openai_key):
    
    #setting directories and files to save results
    dir_name = f"results_{datetime.now().strftime('%Y')[2:]}-{datetime.now().strftime('%m-%d-%H-%M')}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    log_file = dir_name + f"/{model_name}_{prompting_method}_log_file.txt"

    num_problems = len(problems)

    with open(log_file, 'w') as f:
        f.write("model: {} \n".format(model_name))
        f.write("prompting method: {} \n".format(prompting_method))
        f.close()
    
    llama_model = None
    tokenizer = None
    if "llama" in model_name:    
        model_id = "Phind/Phind-CodeLlama-34B-v2"
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        
        llama_model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True
        )
        
        tokenizer.padding_side = "left"
        tokenizer.pad_token = tokenizer.eos_token
        llama_model.config.pad_token_id = llama_model.config.eos_token_id
        
    (count_feasible, count_correct, count_optimal, count_incomplete, 
    count_killed, count_not_executed, dict_llm_sol,infeasible_ids, 
    total_number_calls) = get_solutions(problems, model_name, log_file, 
                                        problem_types_action_type,
                                        max_tokens, llama_model, tokenizer,
                                        prompting_method, print_stats, openai_key)
    
    final_record(log_file, count_feasible, count_correct, 
                 count_optimal, count_incomplete, count_killed, 
                 count_not_executed, dict_llm_sol,
                 infeasible_ids, total_number_calls, num_problems)

def main():
    prompting_method = "0shot_text"  # 0shot_text  CoT_text
    model_name = "gpt4"  #gpt4 #gpt3.5 #llama
    problem_types = ["water_jug"]
    all_problems = True
    print_stats = True
    path_to_searchbench = "SearchBench.jsonl"
    openai_key = ""
    
    max_tokens = 1000

    problem_types_action_type = {"8_puzzle": int, "8_puzzle_words":str,
                                "coin_exchange": int, "water_jug": tuple, 
                                "color_sorting": tuple, "restricted_sorting":tuple,
                                "magic_square": tuple, "consecutive_grid": tuple,
                                "traffic":tuple, "city_directed_graph":tuple, "trampoline_matrix":tuple}
    
    problems = dataset.get_problem_types(all_problems, problem_types, path_to_searchbench)[:11]

    run_experiment(prompting_method, model_name,
                   problems, max_tokens, problem_types_action_type, 
                   print_stats, openai_key)


main()
