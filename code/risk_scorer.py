
import pandas as pd

def calculate_risk_score(probability, impact):
    return probability * impact

def generate_risk_report(risks):
    df = pd.DataFrame(risks)
    df["score"] = df.apply(lambda r: calculate_risk_score(r["probability"], r["impact"]), axis=1)
    return df.sort_values("score", ascending=False)

if __name__ == "__main__":
    risks = [
        {"risk":"Model Hallucination","probability":4,"impact":5},
        {"risk":"Data Privacy Breach","probability":2,"impact":5},
        {"risk":"LLM API Outage","probability":3,"impact":4}
    ]
    print(generate_risk_report(risks))
