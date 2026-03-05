
import numpy as np

def calculate_ai_roi(investment, annual_cost_savings, annual_revenue_increase, implementation_months):
    annual_benefit = annual_cost_savings + annual_revenue_increase
    year1_roi = (annual_benefit - investment) / investment * 100

    monthly_benefit = annual_benefit / 12
    payback_months = investment / monthly_benefit

    discount_rate = 0.1
    years = 5
    npv = sum([(annual_benefit / ((1 + discount_rate) ** t)) for t in range(1, years+1)]) - investment

    return {
        "year1_roi_percent": round(year1_roi,2),
        "payback_months": round(payback_months,2),
        "five_year_npv": round(npv,2)
    }

if __name__ == "__main__":
    print(calculate_ai_roi(500000,200000,350000,8))
