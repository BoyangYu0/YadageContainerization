# YadageContainerization
Here is a minimal reproducible example: generate a number N of random numbers with the random seed reading from seed.txt file, calling python script ran_generator.py for N=10 and N=5. Execute the workflow with "yadage-run workdir workflow.yml" for local processing environment, "yadage-run workdir local_image_workflow.yml" for local container environment and "yadage-run workdir py_image_workflow.yml" for python container from Docker Hub. 

The local container is built from Dockerfile and further pushed to local registry with the following commands:
docker build -t container:v1 Dockerfile .
docker run -d -p 5000:5000 --name registry registry:2
docker image tag container:v1 localhost:5000/myfirstimage
docker push localhost:5000/myfirstimage


Running locally was successful on both win11 + Docker + WSL2 and Ubuntu VW with full root access environment. However, the execution in container shows the same error message in both environments:

ERROR | subprocess failed. code: 127,  command docker run --rm   --cidfile /home/boyang/yadage/example/workdir/randomgenerator_1/_packtivity/randomgenerator_1.cid      -v /home/boyang/yadage/example/workdir/randomgenerator_1:/home/boyang/yadage/example/workdir/randomgenerator_1:rw localhost:5000/myfirstimage:latest sh -c './../../ran_generator.py ../../seed.txt 5 /home/boyang/yadage/example/workdir/randomgenerator_1/intermediateResult.txt'
Traceback (most recent call last):
File "/home/boyang/micromamba/envs/workflow/lib/python3.10/site-packages/packtivity/handlers/execution_handlers.py", > line 338, in execute_and_tail_subprocess
   raise subprocess.CalledProcessError(
subprocess.CalledProcessError: Command 'docker run --rm   --cidfile /home/boyang/yadage/example/workdir/randomgenerator_1/_packtivity/randomgenerator_1.cid      -v /home/boyang/yadage/example/workdir/randomgenerator_1:/home/boyang/yadage/example/workdir/randomgenerator_1:rw localhost:5000/myfirstimage:latest sh -c './../../ran_generator.py ../../seed.txt 5 /home/boyang/yadage/example/workdir/randomgenerator_1/intermediateResult.txt'' returned non-zero exit status 127.
2023-07-17 13:24:36,705 | pack.randomgenerator |  ERROR | job execution if job {'name': 'randomgenerator_1', 'wflow_node_id': '8b492a4c-b90c-4972-b2ff-cec5bc86cb49', 'wflow_offset': '', 'wflow_stage': 'randomgenerator', 'wflow_stage_node_idx': 1, 'wflow_hints': {'is_purepub': False}} raise exception exception
