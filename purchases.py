def add_tax(cost_list, tax_rate):
    taxed_costs=[]
    for cost in cost_list:
        taxed_cost=cost+(cost*tax_rate)
        taxed_costs.append(taxed_cost)
    return taxed_costs
customer_names=[]
item_costs=[]
customer_total_costs={}
num_purchases=int(input("Number of purchases: "))
sales_tax=float(input("Sales tax: "))
for purchases in range(num_purchases):
    customer_name=input(f"Customer: ")
    item_cost=float(input(f"Cost: "))
    if customer_name in customer_total_costs:
        customer_total_costs[customer_name] += item_cost + (item_cost * sales_tax)
    else:
        customer_total_costs[customer_name] = item_cost + (item_cost * sales_tax)
print(customer_total_costs) 
