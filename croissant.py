import mlcroissant as mlc

# FileObjects and FileSets define the resources of the dataset.
distribution = [
    # SearchBench is hosted on a GitHub repository:
    mlc.FileObject(
        id="github-repository",
        name="github-repository",
        description="Navigating Labyrinth repository on GitHub.",
        content_url="https://github.com/NasimBorazjani/Navigating_Labyrinth.git",
        encoding_format="git+https",
        sha256="main",
    ),
    # Within that repository, a FileSet lists all JSONL files:
    mlc.FileSet(
        id="jsonl-files",
        name="jsonl-files",
        description="JSONL files are hosted on the GitHub repository.",
        contained_in=["github-repository"],
        encoding_format="application/jsonlines",
        includes="data/*.jsonl",
    ),
]

record_sets = [
    # RecordSets contains records in the dataset.
    mlc.RecordSet(
        id="jsonl",
        name="jsonl",
        # Each record has one or many fields...
        fields=[
            # Fields can be extracted from the FileObjects/FileSets.
            mlc.Field(
                id="jsonl/diff_sorted_id",
                name="diff_sorted_id",
                description="A unique TEXT identifier assigned to each problem instance within a specific problem type.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    # Extract the field from the column of a FileObject/FileSet:
                    extract=mlc.Extract(column="diff_sorted_id"),
                ),
            ),
            mlc.Field(
                id="jsonl/problem_statement",
                name="problem_statement",
                description="A natural language description that outlines the problem to be solved; the only feild of each instance that must be presented to the agent (the LLM).",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="problem_statement"),
                ),
            ),
            mlc.Field(
                id="jsonl/problem_type",
                name="problem_type",
                description="Indicates the problem type, out of 11 problem types in SearchBench, that this particular problem is an instance of.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="problem_type"),
                ),
            ),
            mlc.Field(
                id="jsonl/problem_category",
                name="problem_category",
                description="The specific category, out of the five predefined problem categories in SearchBench, to which this problem belongs.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="problem_category"),
                ),
            ),
            mlc.Field(
                id="jsonl/relative_diff_score",
                name="relative_diff_score",
                description="A TEXT score that indicates the difficulty of this problem instance relative to other instances within the same problem type.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="relative_diff_score"),
                ),
            ),
            mlc.Field(
                id="jsonl/opt_solution",
                name="opt_solution",
                description="A list of actions that, starting from the given initial state, lead to the goal state with the minimum cost as defined in the problem.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="opt_solution"),
                ),
            ),
            mlc.Field(
                id="jsonl/opt_solution_cost",
                name="opt_solution_cost",
                description="The cost of the optimal solution for this problem instance.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="opt_solution_cost"),
                ),
            ),
            mlc.Field(
                id="jsonl/opt_solution_compute_t",
                name="opt_solution_compute_t",
                description="The time, in seconds, that our instance-agnostic A* implementation for the problem type took to solve this specific problem instance.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="opt_solution_compute_t"),
                ),
            ),
            mlc.Field(
                id="jsonl/solution_depth",
                name="solution_depth",
                description="The number of actions required to reach the goal state from the given initial state with the minimum cost.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="solution_depth"),
                ),
            ),
            mlc.Field(
                id="jsonl/max_successor_states",
                name="max_successor_states",
                description="The maximum number of successor states that can be reached from any given state in this problem.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="max_successor_states"),
                ),
            ),
            mlc.Field(
                id="jsonl/num_vars_per_state",
                name="num_vars_per_state",
                description="An upper bound on the number of variables in each state of the problem.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="num_vars_per_state"),
                ),
            ),
            mlc.Field(
                id="jsonl/is_feasible_args",
                name="is_feasible_args",
                description="A list of variables of the problem instance that must be passed to the ‘is_feasible’ function of the evaluation pipeline to determine whether a suggested solution adheres to the rules and constraints of the problem.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="is_feasible_args"),
                ),
            ),
            mlc.Field(
                id="jsonl/is_correct_args",
                name="is_correct_args",
                description="A list of variables in the problem statement of this instance that must be passed as arguments to the 'is_correct' function in the evaluation pipeline, in order to evaluate the correctness of a suggested solution.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="is_correct_args"),
                ),
            ),
            mlc.Field(
                id="jsonl/A*_args",
                name="A*_args",
                description="Variables of this problem instance that must be passed to our A* implementation for the problem type to obtain the optimal solution for the instance.",
                data_types=mlc.DataType.TEXT,
                source=mlc.Source(
                    file_set="jsonl-files",
                    extract=mlc.Extract(column="A*_args"),
                ),
            ),
        ],
    )
]

# Metadata contains information about the dataset.
metadata = mlc.Metadata(
    name="SearchBench",
    # Descriptions can contain plain text or markdown.
    description=(
        "SearchBench is designed to evaluate the performance of LLMs in solving state-based problems that involve combinatorial search and optimization. "
        "It is motivated by the observation that LLMs often struggle with multi-step compositional reasoning, combinatorial problems, and planning. "
        "The problem types included in SearchBench are predominantly NP-hard, requiring systematic exploration of action paths and backtracking to intermediate feasible states for resolution. "
        "As a result, SearchBench targets some of the inherent limitations of the autoregressive architecture of LLMs, which necessitates generating solutions in a sequential manner. "
        "SearchBench provides a rigorous assessment of LLMs' capabilities in designing new algorithms to solve complex problems. "
        "It also investigates the non-linear reasoning capability of LLMs to solve search problems end-to-end using text only."
    ),
    cite_as="in submission",
    url="https://github.com/NasimBorazjani/Navigating_Labyrinth.git",
    license="CC BY-SA",
    distribution=distribution,
    record_sets=record_sets,
)


print(metadata.issues.report())

import json

with open("SearchBench_croissant.json", "w") as f:
  content = metadata.to_json()
  content = json.dumps(content, indent=2)
  print(content)
  f.write(content)
  f.write("\n")  # Terminate file with newline
  