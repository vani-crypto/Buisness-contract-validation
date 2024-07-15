import random
from faker import Faker

fake = Faker()

def generate_contract():
    parties = f"This agreement is made between {fake.company()} (hereinafter referred to as Party A) and {fake.company()} (hereinafter referred to as Party B)."
    agreement_terms = f"The agreement will commence on {fake.date_this_year()} and will continue until {fake.date_this_year()}."
    confidentiality_clause = f"Both parties agree to keep confidential any proprietary information disclosed during the term of this agreement. The contract will remain in effect for a period of {random.randint(1, 20)} years following the termination of this agreement."
    termination_conditions = f"This agreement can be terminated by either party upon {random.randint(30, 50)} days of written notice."
    liability_statement = f"Neither party shall be liable for any indirect, incidental, or consequential damages arising out of or in connection with the agreement."

    contract = f"{parties}\n\n{agreement_terms}\n\n{confidentiality_clause}\n\n{termination_conditions}\n\n{liability_statement}\n"
    return contract

def generate_contracts(num_contracts):
    contracts = []
    for _ in range(num_contracts):
        contracts.append(generate_contract())
    return contracts

if __name__ == "__main__":
    contracts = generate_contracts(5)
    for i, contract in enumerate(contracts):
        filename = f"contract_{i+1}.txt"
        print(f"Writing contract to {filename}")  # Debugging output
        with open(filename, "w") as file:
            file.write(contract)
    print("Contracts generated successfully.")  # Debugging output
