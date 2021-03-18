# matrixshapes
This task primes language models to keep track of matrixshapes.

To generate a dataset, run:
`git clone https://github.com/Muennighoff/matrixshapes.git`
& cd into the repository.
<br>
Then run `python generate.py` for an example datum. Feel free to change the hyperparameters, such as more operations or higher dimensions (both will need more RAM).
<br> <br>
To create a json dataset run `python create_json.py --num 1000 --cont 0.5` for 1000 examples where a maximum of 500 shapes is also contained in the operations. 
<br> <br>
See the task.json for an example how a dataset with num 5 and cont 0.5 may look like.

