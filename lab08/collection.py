def word_counts(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        cleaned = word.strip('.,!?;:')
        if cleaned:
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def print_sorted_counts(counts):
    for word in sorted(counts.keys()):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    return sorted(set(first) & set(second))


def all_topics(first, second):
    return sorted(set(first) | set(second))


def totals_by_category(records):
    totals = {}
    for record in records:
        cat = record["category"]
        totals[cat] = totals.get(cat, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    return [record["title"] for record in records if record["category"] == category]


def sorted_totals(records):
    totals = totals_by_category(records)
    return sorted(totals.items(), key=lambda item: (-item[1], item[0]))


#Вариант 5
records = [
    {"title": "Python Basics",   "category": "python", "amount": 12},
    {"title": "SQL для начинающих", "category": "sql",   "amount": 8},
    {"title": "Python Advanced", "category": "python", "amount": 15},
    {"title": "Git и GitHub",    "category": "git",    "amount": 6},
    {"title": "Python Web",      "category": "python", "amount": 10},
]


def demo_record_and_pair():
    course = {"title": "Python Basics", "hours": 12}
    course["hours"] = 15
    course["completed"] = False
    pair = (course["title"], course["hours"])
    title, hours = pair
    print(f"Название: {title}, часов: {hours}")
    return course
