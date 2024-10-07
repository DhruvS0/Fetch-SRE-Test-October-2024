import yaml
import requests
import time
import sys
from collections import defaultdict

# Function to load and parse the YAML configuration file
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to perform a health check on a single endpoint
def check_endpoint(endpoint):
    url = endpoint['url']
    method = endpoint.get('method', 'GET')  # Default to GET if method not specified
    headers = endpoint.get('headers', {})
    body = endpoint.get('body')

    try:
        start_time = time.time()
        # Send HTTP request with specified parameters
        response = requests.request(method, url, headers=headers, data=body, timeout=1)
        latency = (time.time() - start_time) * 1000  # Calculate latency in milliseconds

        # Check if response is UP (2xx status code and latency < 500ms)
        return 200 <= response.status_code < 300 and latency < 500
    except requests.RequestException:
        # Any exception means the endpoint is DOWN
        return False

# Main function to run the health check system
def main(config_file):
    # Load endpoints from the configuration file
    endpoints = load_config(config_file)
    # Initialize a defaultdict to track statistics for each domain
    domain_stats = defaultdict(lambda: {'up': 0, 'total': 0})

    # Infinite loop to continuously perform health checks
    while True:
        for endpoint in endpoints:
            # Extract domain from the URL
            domain = endpoint['url'].split('/')[2]
            # Perform health check
            is_up = check_endpoint(endpoint)
            
            # Update statistics for the domain
            domain_stats[domain]['total'] += 1
            if is_up:
                domain_stats[domain]['up'] += 1

        # Calculate and print availability percentage for each domain
        for domain, stats in domain_stats.items():
            availability = round((stats['up'] / stats['total']) * 100)
            print(f"{domain} has {availability}% availability percentage")

        # Wait for 15 seconds before the next cycle
        time.sleep(15)

# Entry point of the script
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <config_file_path>")
        sys.exit(1)
    
    # Get the configuration file path from command-line argument
    config_file = sys.argv[1]
    # Start the main function
    main(config_file)