import subprocess

# Define the model name
model_name = 'model_ep10'

# Run the subprocess commands for the specified model name
build = subprocess.run(['./evaluate_object', f'exp_runs_{model_name}', f'exp_runs_{model_name}'], check=True, capture_output=True, text=True, cwd='eval_kitti/build/')
evaluate = subprocess.run(['python3', 'parser.py', f'exp_runs_{model_name}'], check=True, capture_output=True, text=True, cwd='eval_kitti')
