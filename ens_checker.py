import requests


def run_query(query):
    url = 'https://api.thegraph.com/subgraphs/name/ensdomains/ens'
    response = requests.post(url, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Query failed with status code {response.status_code}. Query: {query}')

def ens_checker(name):
    query = """
    {
        domains(where: {name: "%s.eth"}) {
            id
            name
            labelName
            labelhash
        }
    }
    """ % (name)
    result = run_query(query)
    if result['data']['domains']:
        return False
    else:
        return True

def main():
    while True:
        name = input("Enter the ENS name to check availability: ").strip().lower()
        try:
            available = ens_checker(name)
            if available:
                print(f'{name}.eth is available for registration.\n')
            else:
                print(f"{name}.eth has been registered.\n")
        except Exception as e:
            print(f'Error occurred: {e}\n')
    

if __name__ == "__main__":
    main()

input()
