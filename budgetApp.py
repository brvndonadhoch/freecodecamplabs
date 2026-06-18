class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=None):
        if description is None:
            description = ""
        self.ledger.append({'amount': amount, 'description': description})        

    def withdraw(self, amount, description=None):
        if description is None:
            description = ""
            
        if amount <= self.get_balance():
            self.ledger.append({'amount': (amount * -1), 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, destination_category):
        if self.withdraw(amount, f"Transfer to {destination_category.name}"):
            destination_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    
    def __str__(self):
        title = f"{self.name.center(30, '*')}\n"
        
        items = ""
        for item in self.ledger:
            desc = item['description'][:23]
            amount = f"{item['amount']:.2f}"[:7] 
            items += f"{desc:<23}{amount:>7}\n"
            
        total = f"Total: {self.get_balance():.2f}"
        
        return title + items + total

def create_spend_chart(categories):
    spent_per_category = []
    total_spent = 0
    
    for category in categories:
        category_spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent_per_category.append(category_spent)
        total_spent += category_spent

    percentages = []
    for spent in spent_per_category:
        if total_spent > 0:
            percentage = int((spent / total_spent) * 100 // 10) * 10
        else:
            percentage = 0
        percentages.append(percentage)

    chart = "Percentage spent by category\n"
    
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for pct in percentages:
            if pct >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"  
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    
    for i in range(max_len):
        chart += "    "  
        for category in categories:
            if i < len(category.name):
                chart += f" {category.name[i]} "
            else:
                chart += "   " 
        chart += " "
        if i < max_len - 1:
            chart += "\n"

    return chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)