from collection import (
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category,
    sorted_totals,
    records,
    demo_record_and_pair,
)
if __name__ == "__main__":
    # word_counts
    print("=== word_counts ===")
    print(word_counts("Python, python! SQL"))
    print(word_counts("!!!"))

    # common_topics / all_topics
    print("\n=== topics ===")
    t1 = ["python", "sql", "python"]
    t2 = ["sql", "git"]
    print("common:", common_topics(t1, t2))
    print("all:   ", all_topics(t1, t2))

    # totals_by_category
    print("\n=== totals_by_category ===")
    print(totals_by_category(records))

    # titles_in_category
    print("\n=== titles_in_category ===")
    user_category = input("Введите категорию: ").strip()
    print(titles_in_category(records, user_category))

    # sorted_totals (дополнительно)
    print("\n=== sorted_totals ===")
    for cat, total in sorted_totals(records):
        print(f"{cat}: {total}")

    # demo
    print("\n=== record & pair ===")
    demo_record_and_pair()