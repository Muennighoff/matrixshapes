import json
import argparse

from generate import generate

def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument("--num", type=int, default=1000, help="Task examples to generate.")
    parser.add_argument("--cont", type=float, default=0.5, help="Percentage of how many examples are allowed to contain the label.")

    args = parser.parse_args()
    return args

def generate_json(num=1000, cont=0.5):
    """
    Generates json files with examples
    args:
      num: number of examples
      cont: how many of the examples are allowed to contain the label (i.e. the output matrix shape) in their string
    """
    max_cont = int(num * contained_rate)
    cur_cont = 0

    data = {}
    data["examples"] = []

    while len(data["examples"]) < num:
      input, target, contained = generate()

      # Handle contained examples / confounders
      if (contained) and (cur_cont >= max_cont):
        continue
      else:
        cur_cont += 1

      data["examples"].append({"input": input, "target": target})

    with open('task.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)
 

if __name__ == "__main__":
    args = parse_args()
    generate_json(args.num, args.cont)
