"""
Strategic Business Analytics & KPI Modeling Engine
Author: Akash V (@akashvenkey)
"""
class BusinessMetricsEngine:
    @staticmethod
    def calculate_cac(sales_marketing_cost, new_customers):
        return sales_marketing_cost / new_customers if new_customers else 0

    @staticmethod
    def calculate_clv(avg_order_value, purchase_freq, gross_margin_pct, churn_rate):
        if churn_rate <= 0: return 0
        customer_val = avg_order_value * purchase_freq
        return (customer_val * gross_margin_pct) / churn_rate

    @staticmethod
    def break_even_units(fixed_costs, unit_price, unit_variable_cost):
        contribution_margin = unit_price - unit_variable_cost
        return fixed_costs / contribution_margin if contribution_margin > 0 else float('inf')

if __name__ == "__main__":
    engine = BusinessMetricsEngine()
    cac = engine.calculate_cac(50000, 250)
    clv = engine.calculate_clv(120, 4.5, 0.65, 0.15)
    be_units = engine.break_even_units(100000, 50, 20)
    print(f"Customer Acquisition Cost (CAC): ${cac:.2f}")
    print(f"Customer Lifetime Value (CLV):    ${clv:.2f}")
    print(f"CLV / CAC Ratio:                 {clv/cac:.2f}x (Target > 3.0x)")
    print(f"Break-Even Production Units:     {int(be_units)} units")