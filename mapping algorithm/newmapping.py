import csv

def find_companies_by_raw_material(csv_file, raw_material):
    companies = []
    raw_materials=[]
    best_score=0
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            raw_materials=row['Raw Materials'].split(',')[0]
            by_products = row['By-Products'].split(',')[0]
            cost=int(row['Processing Costs'].split(',')[0])
            producing_company = row['Producing Company'].split(',')[0]
            green_score=int(row['green_score'])
            score=(0.1*cost)+(0.9*green_score)
            if raw_material in raw_materials:
                companies.append({
                    'Producing Company': producing_company,
                    'By-Products': by_products
                })
            
            if(score>best_score):
                best_company=producing_company
                best_cost=str(cost)
                best_green_score=str(green_score)
                best_score=score

         
    print("best option is "+best_company)
    print("Cost is " + best_cost)
    print("Green Score is "+best_green_score)       
    return companies

def main():
    csv_file = 'revisedmap.csv'
    raw_material_input = input('Enter a raw material: ')

    companies_with_byproducts = find_companies_by_raw_material(csv_file, raw_material_input)

    if companies_with_byproducts:
        print(f"\nCompanies producing {raw_material_input} and their by-products:")
        for company in companies_with_byproducts:
            print(f"\nProducing Company: {company['Producing Company']}")
            print(f"By-Products: {company['By-Products']}")
    else:
        print(f"\nNo companies found producing {raw_material_input}.")

if __name__ == "__main__":
    main()
