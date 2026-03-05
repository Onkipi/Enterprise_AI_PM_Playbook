
import pandas as pd

def portfolio_health(projects):
    df = pd.DataFrame(projects)
    return df.describe()

if __name__ == "__main__":
    sample = [
        {"project":"AI Chatbot","budget":300000,"status":"on-track"},
        {"project":"Fraud AI","budget":800000,"status":"at-risk"}
    ]
    print(portfolio_health(sample))
