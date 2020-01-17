if __name__ == "__main__":
    counted_list_item = []
    counter = 0
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    for item in ar:
        if item not in counted_list_item:
            item_count = ar.count(item)
            if item_count//2 >= 1:
                counter += item_count//2
                counted_list_item.append(item)
    print(counter)
