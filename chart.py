import matplotlib.pyplot as plt


def generate_chart(domain_scores):

    domains = list(domain_scores.keys())

    values = list(domain_scores.values())

    plt.figure()

    plt.bar(domains,values)

    plt.xticks(rotation=45)

    plt.ylabel("Score")

    plt.title("Developmental Domain Scores")

    plt.tight_layout()

    path = "chart.png"

    plt.savefig(path)

    plt.close()

    return path