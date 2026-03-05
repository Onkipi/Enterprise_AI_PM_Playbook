
import argparse

def generate_charter(project, industry, budget, timeline):
    charter = f"""# AI Project Charter

Project: {project}
Industry: {industry}

Budget: ${budget}
Timeline: {timeline}

## Objectives
Deploy an AI system to improve operational efficiency.

## Success Metrics
- ROI improvement
- Reduced manual workload
- Improved decision intelligence

## Governance
AI ethics review
Data privacy compliance
"""
    return charter

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project")
    parser.add_argument("--industry")
    parser.add_argument("--budget")
    parser.add_argument("--timeline")
    parser.add_argument("--output")

    args = parser.parse_args()
    result = generate_charter(args.project,args.industry,args.budget,args.timeline)

    with open(args.output,"w") as f:
        f.write(result)
