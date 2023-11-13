def read_ips_from_file(file_name):
    with open(file_name, 'r') as file:
        ip_addresses = [line.strip() for line in file]
    return ip_addresses

def write_results_to_file(file_name, results):
    with open(file_name, 'w') as file:
        for result in results:
            file.write(result + '\n')
