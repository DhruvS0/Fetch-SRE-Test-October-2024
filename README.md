# Fetch-SRE-Test-October-2024
Fetch Take-Home Exercise — Site Reliability Engineering
## Question - 

Implement a program to check the health of a set of HTTP endpoints. Read an input argument to a file path with a list of HTTP endpoints in YAML format. Test the health of the end points every 15 seconds. Keep track of the availability percentage of the HTTP domain names being monitored by the program. Log the cumulative availability percentage for each domain to the console after the completion of each 15-second test cycle. 

## Solution -

I have written a python script `fetch-script.py` to check the health of each HTTP endpoints present in the `fetch-input.yml` file which will be passed as an argument while executing the script. 

#### Understanding the script -
The Health Checker program reads a YAML configuration file containing a list of HTTP endpoints, performs health checks on these endpoints every 15 seconds, and logs the cumulative availability percentage for each domain to the console.

- The script loads the configuration from the YAML file.
- It performs health checks on each endpoint every 15 seconds.
- An endpoint is considered UP if:
    - The HTTP response code is 2xx (200-299)
    - The response latency is less than 500ms
- The script calculates and logs the availability percentage for each domain.
- The process continues until manually stopped.

#### To implement the solution -
Run the script with the path to your YAML configuration file as an argument:
```py
python fetch-script.py path/to/your/config.yaml
```
#### Example - 
```py
python fetch-script.py fetch-input.yaml
```
