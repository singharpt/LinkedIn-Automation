job_interval="*/5 * * * *"
python_path=$(which python)
directory_path=$(pwd)/main.py
job="$job_interval $python_path $directory_path"
echo "$job" | crontab -