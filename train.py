passengers = [
    ["Amit", 35, 450, "SL"],
    ["Sita", 10, 300, "3A"],
    ["Ramesh", 65, 700, "2A"],
    ["Neha", 28, 820, "3A"],
    ["Kunal", 8, 900, "SL"],
    ["Meena", 62, 550, "2A"]
]

rates = {"SL": 1, "3A": 2, "2A": 3}
total_revenue = 0
senior_citizens = 0
children = 0
ticket_fares = []
class_counts = {"SL": 0, "3A": 0, "2A": 0}

for p in passengers:
    name, age, dist, p_class = p
    
    fare = dist * rates[p_class]
    
    if age < 12:
        fare *= 0.5
        children += 1
    elif age >= 60:
        fare *= 0.7
        senior_citizens += 1
        
    if dist > 800:
        fare += 400
    elif dist > 500:
        fare += 200
        
    total_revenue += fare
    ticket_fares.append(fare)
    class_counts[p_class] += 1

print(f"Total Revenue: ₹{total_revenue}")
print(f"Number of Senior Citizens: {senior_citizens}")
print(f"Number of Children: {children}")
print(f"Highest Ticket Fare: ₹{max(ticket_fares)}")
print("Class-wise Passenger Count:")
for cls, count in class_counts.items():
    print(f"  {cls}: {count}")
